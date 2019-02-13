import numpy as np

#梯度下降
def Linear_regression(x,y,alpha=0.01,max_count=10000,min_error=0.00001):
    x = Standardization(x)
    thetas = np.ones((x.shape[1], 1))
    while max_count>0:
        max_count-=1
        print(max_count)
        a_cost=cost(x,y,thetas)
        #更新权重
        thetas=thetas-alpha/x.shape[0]*x.T.dot(x.dot(thetas)-y)
        b_cost=cost(x,y,thetas)
        #差值在一定范围内
        if np.abs(b_cost-a_cost)<min_error:
            break
    return thetas


#创建数据集
def create_dataset():
    x=np.random.rand(1000,5)*5*np.log(np.random.rand(1000,1)*10)
    y=np.random.rand(1000,1)*5*np.log(np.random.rand(1000,1))
    return x,y


#标准化
def Standardization(x):
    x_avg=np.zeros((1,x.shape[1]))
    x_std=np.zeros((1,x.shape[1]))
    for i in range(x.shape[1]):
        x_avg[0,i]=np.average(x[:,i])
        x_std[0,i]=np.std(x[:,1])
    x_c=(x-x_avg)/x_std
    # x=pd.DataFrame(x)
    # print(x.corr())
    return x_c


#代价函数 误差平方和
def cost(x,y,thetas):
    error=x.dot(thetas)-y
    m=x.shape[0]
    cost_error=error.T.dot(error)/(2*m)
    return cost_error[0,0]







x,y=create_dataset()

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y)

# import pandas as pd
print(Linear_regression(x_train,y_train))