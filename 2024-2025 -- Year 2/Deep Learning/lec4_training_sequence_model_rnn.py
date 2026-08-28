"Обучение моделей последовательностей"
from d2l import mxnet as d2l
from mxnet import autograd, np, npx, gluon, init
from mxnet.gluon import nn
npx.set_np()

#создаётся шумная синусоида, на основе которой будем обучать модель предсказывать будущие значения.
T = 1000  # Генерация 1000 точек
time = np.arange(1, T + 1, dtype=np.float32)
x = np.sin(0.01 * time) + np.random.normal(0, 0.2, (T,))
d2l.plot(time, [x], 'time', 'x', xlim=[1, 1000], figsize=(6, 3))

"Подготовка данных"
#формируем обучающие данные, используя прошлые 4 точки (xt−4​,xt−3​,xt−2​,xt−1​) для предсказания xt​.
tau = 4
features = np.zeros((T - tau, tau))  # T - tau примеров с tau признаками
for i in range(tau):
    features[:, i] = x[i:T - tau + i]
labels = x[tau:].reshape((-1, 1))  # Следующее значение в качестве метки

batch_size, n_train = 16, 600
train_iter = d2l.load_array((features[:n_train], labels[:n_train]), batch_size, is_train=True)

"Создание нейросети"
#Простая полносвязная нейросеть (MLP) с одним скрытым слоем из 10 нейронов и активацией ReLU.
#simple MLP
def get_net():
    net = nn.Sequential()
    net.add(nn.Dense(10, activation='relu'), nn.Dense(1))
    net.initialize(init.Xavier())
    return net
#Square loss
loss = gluon.loss.L2Loss()

"Обучение модели"
#Обучаем сеть с оптимизатором Adam и функцией потерь MSE (L2 Loss).
def train(net, train_iter, loss, epochs, lr):
    trainer = gluon.Trainer(net.collect_params(), 'adam', {'learning_rate': lr})
    
    for epoch in range(epochs):
        for X, y in train_iter:
            with autograd.record():
                l = loss(net(X), y)
            l.backward()
            trainer.step(batch_size)
        print(f'epoch {epoch + 1}, loss: {d2l.evaluate_loss(net, train_iter, loss):f}')

net = get_net()
train(net, train_iter, loss, 5, 0.01)



"Предсказание - One-step prediction"
#Построение графика однократного предсказания.
one_step_preds = net(features)
d2l.plot([time, time[tau:]], [x.asnumpy(), one_step_preds.asnumpy()], 'time', 'x',
         legend=['data', '1-step preds'], xlim=[1, 1000], figsize=(6, 3))



"Предсказание - Multi-step prediction"
#Многошаговое предсказание
multistep_preds = np.zeros(T)
multistep_preds[:n_train + tau] = x[:n_train + tau] #Первые n_train + tau значений берутся из исходных данных x
for i in range(n_train + tau, T): #оставшиеся предсказ с помощ нейросети net, использ tau предыдущих значений
    multistep_preds[i] = net(multistep_preds[i - tau:i].reshape((1, -1))) #[i - tau:i] = Predict tau steps forward in time

#График предсказаний:
d2l.plot([time, time[tau:], time[n_train + tau:]], [
    x.asnumpy(),
    one_step_preds.asnumpy(), 
    multistep_preds[n_train + tau:].asnumpy()
],
         'time',
         legend=['data', '1-step preds', 'multi-step preds'],
         xlim=[1, 1000],
         figsize=(6, 3))

"1-step prediction       предсказывает одно значение, используя предыдущие данные."
"multi-step prediction   строит прогноз, используя уже предсказанные значения, что приводит к накоплению ошибок."