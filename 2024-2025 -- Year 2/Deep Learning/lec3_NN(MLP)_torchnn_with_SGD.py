import torch
import torch.nn as nn

class MLP(nn.Module): # Подключаем модуль для создания нейросетей.
    def __init__(self):
        super(MLP, self).__init__()
        self.hidden_layer = nn.Linear(2, 5) #первый слой (вход из 2 переменных, выход из 5 нейронов).
        self.relu         = nn.ReLU() #функция активации
        self.output_layer = nn.Linear(5, 1) #выходной слой.
        self.sigmoid      = nn.Sigmoid() #функция активации для выхода.

    def forward(self, x): #Метод forward() определяет проход данных через слои.
        z_1   = self.hidden_layer(x)
        a_1   = self.relu(z_1)
        z_2   = self.output_layer(a_1)
        y_hat = self.sigmoid(z_2)
        return y_hat

mlp = MLP() #Создаем экземпляр модели.

criterion = nn.BCELoss() #функция потерь (Binary Cross Entropy).
optimizer = torch.optim.SGD(mlp.parameters(), lr=0.1) #градиентный спуск.

x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float) #Входные данные (x) и метки (y).
y = torch.tensor([0, 1, 1, 0], dtype=torch.float).unsqueeze(1)

#Обучение модели
for i in range(1000):
    y_hat = mlp(x[i % 4]) #вычисляем предсказание.

    loss = criterion(y_hat, y[i % 4]) #считаем ошибку.
    
    optimizer.zero_grad() #обнуляем градиент
    loss.backward() #вычисляем градиенты.
    optimizer.step() #обновляем веса.

y_hat = mlp(x)

print(y - (y_hat > 0.5).float()) # prints tensor([[0.],[0.],[0.],[0.]]) #Оцениваем результат.  100% точности
