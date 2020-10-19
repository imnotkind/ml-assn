# 1

(x1, y1) = (1,1) and (x2, y2) = (2,1)

## a

(x,y) = (1,1), (2,1)

w1 = 0.5, w2 = 0

w = [0.5 0]^T

## b

equation (1)  : $\frac 1 2 [(y_1-(w_1x_1 + w_2))^2 + (y_2 - (w_1x_2 + w_2))^2]$

when (x1, y1) = (1,1) and (x2, y2) = (2,1)

y = [y1 y2]^T

X = [ [x1 , 1] , [x2 , 1] ]

## c

$\frac 1 2 ||y - Xw||_2^2 $ w에 대해서 미분

$w = (X^TX)^{-1}X^Ty$

(x1, y1) = (1,1) and (x2, y2) = (2,1) 이니까 대입

놀랍게도 w = [0, 1] 이 나옴 (실제로 error는 없지!)



# 2

## a

$argmin_w f = argmin_w \sum_{n=1}^3 log(1+exp(-y_n w^T [x_n, 1]^T))$



## b

$g = \nabla_w f = \sum_{n=1}^3 \frac{-y_n exp(-y_n w^T [x_n, 1]^T)}{1+exp(-y_n w^T [x_n, 1]^T)}[x_n, 1]^T$

$w_{t+1} = w_t - \alpha g(w_t)$



## c

  f = torch.mean(torch.log(1 + tmp))

  g = torch.mean( (((-y) * tmp) / (1 + tmp)) * X, dim=1)



## d



# 3

## a

4 constraints i=1,2,3,4



## f

```python
loss = (torch.square(torch.norm(list(net.parameters())[0].data)) * C / 2) + torch.sum(torch.clamp(1 - y*net(torch.transpose(X,0,1)).squeeze(), min=0))
```

loss actually increases when doing gradient descent!

found out that gradient computation is not working in `(torch.square(torch.norm(list(net.parameters())[0].data)) * C / 2)`

