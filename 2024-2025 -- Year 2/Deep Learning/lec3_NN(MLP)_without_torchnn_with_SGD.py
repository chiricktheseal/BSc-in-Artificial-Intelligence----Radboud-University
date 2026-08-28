import torch

def relu(x): # Определяем функцию ReLU (Rectified Linear Unit): заменяет все отрицательные значения на 0
    return torch.max(torch.tensor([0], dtype=torch.float), x) 

def sigmoid(x): #превращает входные значения в диапазон (0,1)(0,1), что удобно для бинарной классификации.
    return 1 / (1 + torch.exp(-x))

w_1 = torch.randn(5, 3) # w_1 – это матрица весов первого слоя (5 нейронов в скрытом слое, 3 входа).
w_2 = torch.randn(6) # w_2 – это вектор весов второго слоя (6 элементов, включая дополнительный bias-нейрон).

x = torch.tensor([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]], dtype=torch.float) #входные данные, все возможные комбинации 2-битных входов с фиктивной единицей для bias.
y = torch.tensor([0, 1, 1, 0], dtype=torch.int) # y – целевые метки (то, чему должна научиться модель).

eta = 0.1 # коэффициент обучения (learning rate), управляющий скоростью изменения весов.

for i in range(1000):
    #Прямой проход (Forward pass):
    z_1   = torch.matmul(x[i % 4], w_1.T) # вычисляем линейную комбинацию входных данных и весов первого слоя.
    a_1     = torch.cat((torch.tensor([1], dtype=torch.float), relu(z_1))) # применяем ReLU, а затем добавляем bias-нейрон (1).
    z_2   = torch.matmul(a_1, w_2.T) # линейная комбинация выходов скрытого слоя и весов второго слоя.
    y_hat = sigmoid(z_2) # получаем выходной прогноз (вероятность класса 1).

    #Функция ошибки (Binary Cross-Entropy, BCE):
    loss = -(y[i % 4] * torch.log(y_hat) + (1 - y[i % 4]) * torch.log(1 - y_hat)) # Это стандартная функция потерь для бинарной классификации

    #Обратное распространение ошибки (Backpropagation):
    delta_2 = y_hat - y[i % 4] #  градиент ошибки на выходном слое.
    delta_1 = delta_2 * w_2[1:] * (z_1 > 0).float() # градиент ошибки скрытого слоя.

    #Обновление весов по градиенту.
    w_2 -= eta * delta_2 * a_1
    w_1 -= eta * torch.matmul(delta_1.unsqueeze(1), x[i % 4].unsqueeze(0))

#Тестирование обученной модели
z_1   = torch.matmul(x, w_1.T) #Прогоняем все входные данные через обученную сеть.
a_1     = torch.cat((torch.ones(4, 1, dtype=torch.float), relu(z_1)), 1)
z_2   = torch.matmul(a_1, w_2.T)
y_hat = sigmoid(z_2)

print(y - (y_hat > 0.5).float()) # prints tensor([0., 0., 0., 0.]) #Оценка точности: 0. означает, что сеть правильно классифицировала все примеры.
