import torch
import torch.optim as optim

torch.manual_seed(1)
X = torch.Tensor([[-1, 1, 2],[1, 1, 1]])
y = torch.Tensor([-1, 1, 1])
w = torch.Tensor([[0.1],[0.1]])
w.requires_grad = True
alpha = 1

optimizer = optim.SGD([w], lr=alpha)
optimizer.zero_grad()

for iter in range(100):
    tmp = torch.exp(torch.matmul(torch.transpose(w,0,1),X)*(-y))


    # [your task1]
    ##############################
    ## loss is the same as f in LogisticRegression.py
    ## Dimensions: loss (scalar)
    loss = torch.mean(torch.log(1+tmp))
    ##############################

    loss.backward()
    print("Loss: %f; ||g||: %f" % (loss, torch.norm(w.grad)))


    # [your task2]
    ##############################
    ## Use two functions within the optimizer instance to perform the update step
    optimizer.step()
    optimizer.zero_grad()
    ##############################

print(w)
