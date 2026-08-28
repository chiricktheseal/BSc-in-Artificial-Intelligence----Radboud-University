from copy import deepcopy  # Импорт для глубокого копирования объектов
from typing import cast  # Для явного преобразования типов

import networkx as nx  # Для работы с графами
import numpy as np  # Для численных операций
import sympy  # Для символьной математики
from ncpol2sdpa import SdpRelaxation, generate_variables  # Для SDP-релаксации

from graphi_RU import generate_graph

class SDPRelaxationSolver:
    # Приватные атрибуты класса
    _graph: nx.Graph  # Граф, который будем решать
    _objective: sympy.Expr  # Целевая функция для оптимизации (гармония H)
    _inequalities = sympy.Le | sympy.Ge | sympy.Lt | sympy.Gt  # Типы неравенств
    _sdp_relaxation: SdpRelaxation  # Объект SDP-релаксации
    _solved: bool  # Флаг: решена ли задача

    def __init__(self, graph: nx.Graph) -> None:
        """Инициализация SDPRelaxationSolver.

        Args:
            graph (networkx.Graph): Граф для решения.
        """
        self._graph = graph  # Сохраняем граф
        self._parse_graph()  # Парсим граф: строим целевую функцию и ограничения
        self._solved = False  # Пока не решено

    def _parse_graph(self) -> None:
        """Парсит self._graph и обновляет self._objective, self._inequalities, и self._sdp_relaxation."""
        # Настройка переменных: создаём символьные переменные для активаций и валентностей
        num_nodes = len(self._graph.nodes)  # Количество узлов
        a = generate_variables('a', num_nodes, commutative=True)  # a0, a1, a2... (активации)
        v = generate_variables('v', num_nodes, commutative=True)  # v0, v1, v2... (валентности)

        # Настройка целевой функции (гармонии H)
        self._objective = 0  # Начинаем с нуля
        
        # ПРОБЛЕМА №1: Цикл по рёбрам графа
        for edge in list(self._graph.edges(data=True)):
            # edge = (узел_i, узел_j, {данные})
            # Добавляем вклад ОТ узла i К узлу j
            self._objective += self._objective_term(
                a[edge[0]],  # a_i
                a[edge[1]],  # a_j
                v[edge[0]],  # v_i
                v[edge[1]],  # v_j
                self._graph.nodes[edge[0]]['w_a'],  # ПРОБЛЕМА: Это w_vj в теории!
                self._graph.nodes[edge[0]]['w_v'],  # ПРОБЛЕМА: Это w_aj в теории!
                edge[2]['w_a'],  # w_aij (когнитивная связь между узлами)
                edge[2]['w_v'],  # w_vij (эмоциональная связь между узлами)
            )
            # Добавляем вклад ОТ узла j К узлу i (симметрично)
            self._objective += self._objective_term(
                a[edge[1]],  # a_j
                a[edge[0]],  # a_i
                v[edge[1]],  # v_j
                v[edge[0]],  # v_i
                self._graph.nodes[edge[1]]['w_a'],  # w_vj для узла j
                self._graph.nodes[edge[1]]['w_v'],  # w_aj для узла j
                edge[2]['w_a'],  # w_aij
                edge[2]['w_v'],  # w_vij
            )

        # Добавляем внутреннюю валентность (inherent valence) в целевую функцию
        for node in self._graph.nodes(data=True):
            # node = (индекс, {данные})
            if node[1]['w_inherent_valence'] != 0:  # Если у узла есть врождённая эмоция
                # УПРОЩЁННАЯ ВЕРСИЯ: w_inherent_valence * (v_i + w_a_i * a_i)
                # ПРОБЛЕМА: w_a здесь на самом деле w_vj!
                self._objective += node[1]['w_inherent_valence'] * (v[node[0]] + node[1]['w_a'] * a[node[0]])

        # Инвертируем целевую функцию (потому что библиотека минимизирует, а мы хотим максимизировать)
        self._objective = - self._objective

        # Настройка ограничений: -1 ≤ a_i ≤ 1 и -1 ≤ v_i ≤ 1
        self._inequalities = (
            [a_i <= 1 for a_i in a] +  # a_i ≤ 1
            [v_i <= 1 for v_i in v] +  # v_i ≤ 1
            [a_i >= -1 for a_i in a] +  # a_i ≥ -1
            [v_i >= -1 for v_i in v]   # v_i ≥ -1
        )

        # Создаём объект SDP-релаксации со всеми переменными
        self._sdp_relaxation = SdpRelaxation(a + v)

    def _objective_term(
        self,
        a_i: sympy.Symbol,  # Активация узла i
        a_j: sympy.Symbol,  # Активация узла j
        v_i: sympy.Symbol,  # Валентность узла i
        v_j: sympy.Symbol,  # Валентность узла j
        w_aj: np.floating,  # НА САМОМ ДЕЛЕ: w_vj! Влияние v_j на a_j
        w_vj: np.floating,  # НА САМОМ ДЕЛЕ: w_aj! Влияние a_j на v_j
        w_aij: np.floating,  # w_aij: когнитивная связь i→j
        w_vij: np.floating,  # w_vij: эмоциональная связь i→j
    ) -> sympy.Add:
        # ФОРМУЛА ГАРМОНИИ ИЗ ТЕОРИИ МИРЫ:
        # w_aij * a_i * (a_j + w_vj * v_j) + w_vij * v_i * (v_j + w_aj * a_j)
        # НО: w_aj и w_vj здесь ПЕРЕПУТАНЫ относительно их реального смысла!
        return w_aij * a_i * (a_j + w_vj * v_j) + w_vij * v_i * (v_j + w_aj * a_j)  # type: ignore[reportReturnType]

    def solve(self, level: int = 2) -> bool: 
        """Получает SDP-релаксацию и вызывает решатель.

        Params:
            level (int): Уровень релаксации. Увеличивайте для более точного решения.  level=2 - уровень релаксации (чем выше, тем точнее, но медленнее)

        Returns:
            bool: `True` если успешно, `False` в противном случае. Попробуйте увеличить `level` если возвращает `False`.
        """
        # Строим SDP-релаксацию с заданным уровнем
        self._sdp_relaxation.get_relaxation(level, self._objective, self._inequalities)
        # Решаем с помощью Mosek (быстрый решатель)
        self._sdp_relaxation.solve('mosek')
        self._solved = True
        return self._sdp_relaxation.status == 'optimal'

    @property
    def primal(self) -> float:
        """Значение primal SDP, вычисленное решателем.

        Верхняя граница задачи оптимизации (максимально возможная гармония).
        """
        if not self._solved:
            raise RuntimeError("Граф ещё не решён. `primal` доступен только после вызова `solve`.")
        # Берём значение и меняем знак (потому что мы инвертировали целевую функцию)
        return - cast('float', self._sdp_relaxation.primal)

    @property
    def dual(self) -> float:
        """Значение dual SDP, вычисленное решателем.

        Нижняя граница задачи оптимизации (гарантированная гармония).
        """
        if not self._solved:
            raise RuntimeError("Граф ещё не решён. `dual` доступен только после вызова `solve`.")
        # ВНИМАНИЕ: здесь ошибка! Должно быть self._sdp_relaxation.dual, а не .primal!
        return - cast('float', self._sdp_relaxation.dual)  # ОШИБКА!

    @property
    def graph(self) -> nx.Graph:
        """Глубокая копия графа, который решается/решили."""
        return deepcopy(self._graph)

    @graph.setter
    def graph(self, graph: nx.Graph) -> None:
        if not isinstance(graph, nx.Graph):
            raise TypeError(f"Ожидался аргумент типа `networkx.Graph`, но получен `{type(graph)}`.")
        self._graph = graph  # Обновляем граф
        self._parse_graph()  # Перестраиваем задачу
        self._solved = False  # Сбрасываем флаг решения

    @property
    def solved(self) -> bool:
        """Была ли задача решена."""
        return self._solved
    
if __name__ == "__main__":
    # Example
    graph = generate_graph(6, 10, 1)
    solver = SDPRelaxationSolver(graph)
    
    if solver.solve(level=2):
        print(f"Upper bound (primal): {solver.primal:.4f}")
        print(f"Lower bound (dual): {solver.dual:.4f}")
        print(f"Optimal value is in: [{solver.dual:.4f}, {solver.primal:.4f}]")
    else:
        print("Failed to solve")