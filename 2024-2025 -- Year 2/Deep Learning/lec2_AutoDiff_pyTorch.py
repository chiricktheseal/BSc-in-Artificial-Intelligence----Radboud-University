import torch

#Automatic Differentiation with torch.autograd

#simplest one-layer neural network, with input x, parameters w and b, and some loss function
x = torch.ones(5)  # input tensor
y = torch.zeros(3)  # expected output
w = torch.randn(5, 3, requires_grad=True) #w and b are parameters, which we need to optimize
b = torch.randn(3, requires_grad=True)
z = torch.matmul(x, w)+b
loss = torch.nn.functional.binary_cross_entropy_with_logits(z, y) #need be able compute gradients of loss func with respect to those vars


#---------------------------------------------------------------------------
print("--------------------------\n\n\nComp graph")
#Tensors, Functions and Computational graph
#You can set the value of requires_grad when creating a tensor, or later by using x.requires_grad_(True) method
print(f"Gradient function for z = {z.grad_fn}") #reference to backward propagation func is stored in grad_fn property of a tensor
print(f"Gradient function for loss = {loss.grad_fn}")



#---------------------------------------------------------------------------
print("--------------------------\n\n\nCOMPUTING GRADIENTS")
#Computing Gradients
#To optimize weights of params in the NN, need compute derivs of loss func with respect to params,  
#                                       need ∂loss\∂w and ∂loss\∂b under some fixed values of x and y
#To compute those derivatives, we call loss.backward(), and then retrieve the values from w.grad and b.grad
loss.backward()
print(w.grad)
print(b.grad)
#obtain grad properties for the leaf(GOAL) nodes of comp graph, which have requires_grad property set to True. 
#                                       For all other nodes in graph, gradients will not be available.
#can only perform gradient calculations using backward once on a given graph, for performance reasons. 
#If need do several backward calls on the same graph, we need to pass retain_graph=True to the backward call



#---------------------------------------------------------------------------
print("--------------------------\n\n\nDISABLING GRAD TRACK")
#Disabling Gradient Tracking
#По умолчанию все тензоры с requires_grad=True отслеживают историю своих вычислений и поддерживают вычисление градиента
#когда не нужно этого делать= когда обучили модель и хотим применить ее к некоторым входным данным, те хотим выполнять только прямые вычисления по сети.
z = torch.matmul(x, w)+b
print(z.requires_grad)

with torch.no_grad(): # stop tracking computations by surrounding our computation code with torch.no_grad() block:
    z = torch.matmul(x, w)+b
print(z.requires_grad)

z = torch.matmul(x, w)+b
z_det = z.detach() #same result is to use the detach() method on the tensor:
print(z_det.requires_grad)

"""

There are reasons you might want to disable gradient tracking:
1-To mark some parameters in your neural network as frozen parameters.
2-To speed up computations when you are only doing forward pass, because computations on tensors that do not track gradients would be more efficient.

"""