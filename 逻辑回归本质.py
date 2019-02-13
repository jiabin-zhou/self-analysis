import numpy as np

#sigmod
z=thetas.T*x
h=1/(1+np.exp(-z))

#似然函数
if y==1:
    px=h
if y==0:
    px=1-h

px=h**y+(1-h)**(1-y)
p=1
#极大似然估计
p=p*px for xi in x

#两边取对数
np.log(p)=np.log(h**y+(1-h)**(1-y))
         =y*np.log(h)+(1-y*np.log(1-h))


#梯度下降/上升
thetas=thetas-alpha/m*(h-y)*x