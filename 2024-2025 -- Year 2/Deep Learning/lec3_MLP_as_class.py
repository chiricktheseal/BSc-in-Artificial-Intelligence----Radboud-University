import torch
import torch.nn as nn

class MLP(nn.Module): # Определяем класс MLP, наследующий nn.Module
    def __init__(self):
        super(MLP, self).__init__() # инициализирует nn.Module
        self.hidden_layer = nn.Linear(3, 2) # Линейный слой (3 входа → 2нейр в скрыт слое). Аналог torch.matmul(x, w_1.T) + b_1
        self.relu         = nn.ReLU() # Готовая ReLU-функция
        self.output_layer = nn.Linear(2, 1) # Линейный выходной слой (2 входа → 1 выходной нейрон).
        self.sigmoid      = nn.Sigmoid() # Готовая сигмоидная функция.

    def forward(self, x): # Вычисляет результат сети аналогично первой реализации.
        z_1   = self.hidden_layer(x) # Матрица весов скрыт слоя, лин комбция вход знач и весов + вектор смещений
        a_1   = self.relu(z_1) # Применяем функцию ReLU для введения нелинейности   a_1 — активированные выходы скрытого слоя.
        z_2   = self.output_layer(a_1)  # z_2 — скаляр, так как выходной слой содержит 1 нейрон
        y_hat = self.sigmoid(z_2) # Применяем сигмоид, чтобы получить финальный выход (значение от 0 до 1).
        return y_hat

mlp = MLP() # Создаем экземпляр MLP.

x = torch.tensor([1, 2, 3], dtype=torch.float).unsqueeze(0) # Входной тензор преобразуется в матрицу размера (1,3) (добавляется размер batch).

y_hat = mlp(x) # Прогоняем входные данные через сеть.

print(y_hat)


"""
Компактный
Гибкость через PyTorch API
Быстрее
Встроенная поддержка  -Использование GPU
"""