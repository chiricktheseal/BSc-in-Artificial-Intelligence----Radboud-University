def grad_clipping(net, theta):  #@save
    """Ограничение градиента"""
    if isinstance(net, gluon.Block):
        params = [p.data() for p in net.collect_params().values()]
    else:
        params = net.params
    norm = math.sqrt(sum((p.grad ** 2).sum() for p in params))
    if norm > theta: #норма градиента превышает заданный порог theta
        for param in params:
            param.grad[:] *= theta / norm #то градиент масштаб до theta, предотвращая его взрыв
