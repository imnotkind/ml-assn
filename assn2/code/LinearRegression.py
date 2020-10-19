import torch

x = torch.Tensor([[1],[2]])
y = torch.Tensor([[1],[1]])
print(x.size())

X = torch.cat((x, torch.ones_like(x)),1)
print(X)
print(X[1,0])
print(torch.matmul(X, y))


#[Your task1]
##############################
## Fill in the arguments
res1 = torch.lstsq(y, X)
##############################
print("Solution 1:")
print(res1[0]) # tensor([[-0.], [1.]])

# Hint:
print(torch.matmul(torch.transpose(X, 0, 1),X))
print(torch.matmul(torch.transpose(X, 0, 1),y))

#[Your task2]
##############################
## What should l and r be?
## Dimensions: l (2x2); r (2x1)
l = torch.matmul(torch.transpose(X, 0, 1),X) # X^TX
r = torch.matmul(torch.transpose(X, 0, 1),y) # X^Ty
##############################
res2 = torch.solve(r,l) # X^TXw = X^Ty
print("Solution 2:")
print(res2[0]) # tensor([[0.], [1.]])

#[Your task3]
##############################
## What should l and r be?
## Dimensions: l (2x2); r (2x1)
l = torch.matmul(torch.transpose(X, 0, 1),X) # X^TX
r = torch.matmul(torch.transpose(X, 0, 1),y) # X^Ty
##############################
res3 = torch.matmul(torch.inverse(l),r)
print("Solution 3:")
print(res3) # tensor([[-4.7684e-07], [ 1.0000e+00]])
