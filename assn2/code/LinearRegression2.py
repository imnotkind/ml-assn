import torch

# [your task1]
##############################
## Specify the matrix X
## Dimensions: X (3x3)
X = torch.Tensor([[0, 0, 1],[1, 1, 1],[4, 2, 1]])
y = torch.Tensor([[0],[1],[1]])
##############################
print(X)
print(y)

# [your task2]
##############################
## Use one of the ways to compute the result, c.f., LinearRegression.py
res = torch.lstsq(y, X)
##############################
print(res)
