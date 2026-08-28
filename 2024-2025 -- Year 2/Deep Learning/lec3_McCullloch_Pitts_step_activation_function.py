import torch
	
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0
	
w = torch.tensor([0.1, 0.2, 0.3], dtype=torch.float)
b = torch.tensor([0.5], dtype=torch.float)
	
x = torch.tensor([1, 2, 3], dtype=torch.float)
	
z     = torch.matmul(w, x) + b
y_hat = step_function(z)
	
print(y_hat)