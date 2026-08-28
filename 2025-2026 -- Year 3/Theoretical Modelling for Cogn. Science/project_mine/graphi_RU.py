from collections.abc import Callable  # Импорт типа Callable

import networkx as nx  # Импорт библиотеки для работы с графами
import numpy as np     # Импорт библиотеки для численных операций


def generate_graph(
    # Определение функции create_graph с параметрами:
    num_nodes: int,  # Количество узлов, которое должен иметь граф.
    num_edges: int,  # Количество ребер, которое должен иметь граф.
    num_inherent_valence: int,  # Количество ребер, к которым прикреплена внутренняя валентность.
    initial_value: float | np.float64 = 0,  # Начальное значение, присваиваемое активациям и валентностям. По умолчанию `0`.
    distribution: Callable[[tuple[int] | int | None], np.ndarray] | None = None,  # Распределение, из которого берутся веса. Значения должны быть в диапазоне [-1, 1]. Для w_ai и w_vi они переносятся в [0, 1]. `Callable` должен принимать форму (shape) и возвращать `np.ndarray` этой формы со случайными значениями. Если `None`, выборка из равномерного распределения.
    seed: int | None = None,  # Сид (начальное значение) для воспроизводимости. По умолчанию `None` (непредсказуемая энтропия от ОС).
) -> nx.Graph:  # Функция возвращает объект типа networkx.Graph.
    """Create a random graph with `num_nodes`, `num_edges` and weights drawn from `distribution`.

    Params:
        num_nodes (int): Number of nodes the graph should have.
        num_edges (int): Number of edges the graph should have.
        num_inherent_valence (int): Number of  edges that have inherent valence attached to them.
        initial_value (float): Initial value assigned to activations and valences. Defaults to `0`.
        distribution (Callable[[tuple[int] | int | None], np.ndarray] | None): Distributions to draw the weights from.
            The values should be in range [-1, 1]. For w_ai and w_vi, they are rescaled to [0, 1]. The `Callable` should
            take a shape and return an `np.ndarray` of that shape with random values. If `None`, sample from uniform
            distribution.
        seed (int): Seed for reproducibility. Defaults to `None`(unpredictable entropy from OS).

    Returns:
        networkx.Graph: The random graph.
    """
    # Создать случайный граф с `num_nodes`, `num_edges` и весами, взятыми из `distribution`.
    # Параметры:
    #     num_nodes (int): Количество узлов, которое должен иметь граф.
    #     num_edges (int): Количество ребер, которое должен иметь граф.
    #     num_inherent_valence (int): Количество ребер, к которым прикреплена внутренняя валентность.
    #     initial_value (float): Начальное значение, присвоенное активациям и валентностям. По умолчанию `0`.
    #     distribution (Callable[[tuple[int] | int | None], np.ndarray] | None): Распределения, из которых берутся веса.
    #         Значения должны быть в диапазоне [-1, 1]. Для w_ai и w_vi они переносятся в [0, 1]. `Callable` должен
    #         принимать форму и возвращать `np.ndarray` этой формы со случайными значениями. Если `None`, выборка из равномерного
    #         распределения.
    #     seed (int): Сид для воспроизводимости. По умолчанию `None` (непредсказуемая энтропия от ОС).
    # Возвращает:
    #     networkx.Graph: Случайный граф.

    # Проверка: если количество ребер больше или равно максимально возможному для полного графа...
    if num_edges >= (m := num_nodes * (num_nodes - 1) // 2):
        # ...вызвать ошибку с пояснением.
        raise ValueError(
            f"num_edges must be at most {m} for {num_nodes} nodes but was {num_edges}. Graph can have at"  \
                "most (|V| (|V| - 1)) / 2 edges, in which case it is complete."
        )
        # "num_edges должно быть не более {m} для {num_nodes} узлов, но было {num_edges}. Граф может иметь
        # не более (|V| (|V| - 1)) / 2 ребер, и в этом случае он является полным."

    # Если распределение не задано (None), создать лямбда-функцию для равномерного распределения от -1 до 1.
    if distribution is None:
        distribution = lambda s: np.random.default_rng(seed).uniform(-1, 1, s)  # noqa: E731

    # Создать случайный граф с помощью networkx: gnm_random_graph создает граф с num_nodes узлами и num_edges ребрами.
    graph: nx.Graph = nx.gnm_random_graph(num_nodes, num_edges, seed=seed)


    # Назначить веса ребер
    #   между узлами (для связей между разными идеями)
    #   w_a - вес для когнитивной (активационной) связи между узлами
    nx.set_edge_attributes(graph, dict(zip(graph.edges, distribution(graph.number_of_edges()), strict=True)), 'w_a')
    #   w_v - вес для эмоциональной (валентностной) связи между узлами
    nx.set_edge_attributes(graph, dict(zip(graph.edges, distribution(graph.number_of_edges()), strict=True)), 'w_v')

    #   внутри узлов (для связи между активацией и валентностью ОДНОЙ идеи)
    #   w_a - вес влияния валентности узла на его собственную активацию (w_vj в формуле)
    #   Значения из distribution делятся на 2 и прибавляется 1, чтобы попасть в диапазон [0, 1].
     # Логические  провода  (когнитивные связи)
    nx.set_node_attributes(
        graph, dict(zip(graph.nodes, (distribution(graph.number_of_nodes()) + 1) / 2 , strict=True)), 'w_a'
    )
    #   w_v - вес влияния активации узла на его собственную валентность (w_aj в формуле)
     # Эмоциональные провода (эмоциональные связи)  
    nx.set_node_attributes(
        graph, dict(zip(graph.nodes, (distribution(graph.number_of_nodes()) + 1) / 2 , strict=True)), 'w_v'
    )

    # Назначить начальные веса активации/валентности
    #   a - начальная активация (уверенность) для каждого узла
    nx.set_node_attributes(graph, np.float64(initial_value), 'a')  # type: ignore[reportArgumentType, reportCallIssue]
    #   v - начальная валентность (эмоциональный заряд) для каждого узла
    nx.set_node_attributes(graph, np.float64(initial_value), 'v')  # type: ignore[reportArgumentType, reportCallIssue]

    # Назначить внутреннюю валентность (inherent valence)
    #   w_inherent_valence - вес связи с гипотетическим общим источником валентности (VALENCE)
    #   Сначала всем узлам присваивается значение 0.
    nx.set_node_attributes(graph, np.float64(0), 'w_inherent_valence')  # type: ignore[reportArgumentType, reportCallIssue]
    #   Затем случайно выбирается `num_inherent_valence` узлов, которым присваивается ненулевой вес.
    selected_nodes = np.random.default_rng(seed).choice(np.array(graph.nodes), num_inherent_valence, replace=False)
    #   Этим выбранным узлам назначаются случайные веса из distribution.
    nx.set_node_attributes(
        graph, dict(zip(selected_nodes, distribution(len(selected_nodes)), strict=True)), 'w_inherent_valence'
    )

    # Вернуть созданный граф
    return graph
  
  

    
    # Основная часть программы
if __name__ == "__main__":
    graph = generate_graph(6, 10, 2)
    print("Nodes:")
    for node, data in graph.nodes(data=True):
        print(f"    Node {node}:\t{data}")
    print("Edges:")
    for node1, node2, data in graph.edges(data=True):
        print(f"    Edge ({node1}, {node2}):\t{data}")