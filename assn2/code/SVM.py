import torch
import torch.optim as optim
import torch.nn as nn
import matplotlib.pyplot as plt

torch.manual_seed(1)
X = torch.Tensor([[1, 0, 0, -1],[0, 1, 0, -1]])
y = torch.Tensor([1, 1, -1, -1])
alpha = 0.001
C = 1

class ShallowNet(nn.Module):
    def __init__(self):
        super(ShallowNet, self).__init__()
        self.fc1 = nn.Linear(2,1, bias=True)
    
    def forward(self, X):
        return self.fc1(X)

net = ShallowNet()
print(net)

print(net(torch.transpose(X,0,1)).squeeze())

optimizer = optim.SGD(net.parameters(), lr=alpha, weight_decay=0)
optimizer.zero_grad()

params = list(net.parameters())
params[0].data = torch.Tensor([[2, 2]])
params[1].data = torch.Tensor([-1])

farr = []

for iter in range(10000):
    if iter==0:
        print(1 - y*net(torch.transpose(X,0,1)).squeeze())
    
    #[Your task]
    ##############################
    ## Complete this single line which is our cost function
    ## Dimensions: loss (scalar)
    l2 = 0
    for f in net.parameters():
        if f.shape == torch.Size([1, 2]): # only weight, not bias
            l2 += torch.sum(torch.square(f))
    loss = l2 * C / 2 + torch.sum(torch.clamp(1 - y*net(torch.transpose(X,0,1)).squeeze(), min=0))

    loss_wrong = (torch.sum(torch.square(list(net.parameters())[0].data)) * C / 2) + torch.sum(torch.clamp(1 - y*net(torch.transpose(X,0,1)).squeeze(), min=0)) # this code doesn't calculate the gradient of regularizer term
    ##############################
    
    loss.backward()
    gn = 0
    for f in net.parameters():
        if iter==0:
            print("Test")
            print(f.grad)
        gn = gn + torch.norm(f.grad)
    print("Iter: %d; Loss: %f; ||g||: %f" % (iter, loss, gn))
    optimizer.step()
    optimizer.zero_grad()

    farr.append(loss.item())

    for f in net.parameters():
        print(f)

plt.plot(farr)
plt.show()
