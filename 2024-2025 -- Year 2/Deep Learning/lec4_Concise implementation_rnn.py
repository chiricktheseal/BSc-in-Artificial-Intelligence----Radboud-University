"Concise implementation"
#Создаём слой RNN с 256 скрытыми нейронами и инициализируем его.
num_hidden = 256
rnn_layer = rnn.RNN(num_hidden)
rnn_layer.initialize()

#Инициализируем скрытое состояние и проверяем его размеры.
state = rnn_layer.begin_state(batch_size=batch_size)
len(state), state[0].shape

#RNNModel – это класс, который определяет рекуррентную нейронную сеть (RNN).

class RNNModel(nn.Block):
    def __init__(self, rnn_layer, vocab_size, **kwargs):
        super().__init__(**kwargs)
        self.rnn = rnn_layer
        self.vocab_size = vocab_size
        self.dense = nn.Dense(vocab_size)

    def forward(self, inputs, state):
        X =  npx.one_hot(inputs.T, self.vocab_size)
        Y, state = self.rnn(X, state) #сначала прогоняем вход дан через рекуррентный слой (self.rnn
        # The fully-connected layer will first change the shape of 'Y' to
        # ('num_steps'* 'batch_size', 'num_hidden'). Its output shape is
        # ("num_steps * 'batch_size', 'vocab_size').
        
        output = self.dense(Y.reshape(-1, Y.shape[-1])) #через полносвязный слой (self.dense), преобразует выход в форму, пригодную для классификации символов
        return output, state

    def begin_state(self, *args, **kwargs):
        return self.rnn.begin_state(*args, **kwargs)


#Запуск обучения на 500 эпох с определённой скоростью обучения.
num_epochs, lr = 500, 1
d2l.train_ch8(net, train_iter, vocab, lr, num_epochs, device)

#perplexity 1.2, 159260.9 tokens/sec on gpu(0)
#Модель обучилась с перплексией 1.2 и обрабатывала 159260.9 токенов в секунду.



#обучаем RNN за одну эпоху.
def train_epoch_ch8(net, train_iter, loss, updater, device, use_random_iter):
    """Обучение модели в течение одной эпохи."""
    state, timer = None, d2l.Timer() #state хранит скрытое состояние и обновляется между минибатчами
    metric = d2l.Accumulator(2)  # Сумма потерь, количество токенов
    for X, Y in train_iter:
        if state is None or use_random_iter:
            #Initialize 'state' when either is 1st iter or using random sampling
            state = net.begin_state(batch_size=X.shape[0], ctx=device)
        else:
            for s in state:
                s.detach()  # Отключение градиентов detachment

        y = Y.T.reshape(-1)
        X, y = X.as_in_ctx(device), y.as_in_ctx(device)

        with autograd.record():
            y_hat, state = net(X, state)
            l = loss(y_hat, y).mean()
        l.backward()
        grad_clipping(net, 1)  # Ограничение градиента clipping= редотвращает взрыв градиентов
        updater(batch_size=1)  #Since 'mean' func has been invoked
        metric.add(l * y.size, y.size)

    #Возвращает перплексию (измеряет качество модели) и скорость обучения (токенов в секунду).
    return math.exp(metric[0] / metric[1]), metric[1] / timer.stop()
