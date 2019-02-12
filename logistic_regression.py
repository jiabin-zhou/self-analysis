import numpy as np


# x.shape (100,4)  y.shape （100,1)
def Logistic_regression(x,y,alpha=0.01,max_count=10000,min_error=0.00001):
    #构造常数项
    x=np.insert(x,0,1,axis=1)
    #初始化
    thetas=np.mat(np.full(x.shape[1],1)).T
    while max_count>0:
        max_count-=1
        a_cost_sum=cost(x,y,thetas)
        #更新权重
        thetas=thetas-alpha/x.shape[0]*np.mat(x).T*(sigmod(np.mat(x)*thetas)-np.mat(y).T)
        b_cost_sum=cost(x,y,thetas)
        if a_cost_sum==b_cost_sum or np.abs(b_cost_sum-a_cost_sum)<min_error:
            print('达可接受误差内')
            break
    return thetas


def sigmod(xi):
    return 1/(1+np.exp(-xi))


def cost(x,y,theats):
    cost_sum=0
    for i in range(x.shape[0]):
        xa=sigmod(np.mat(x[i])*theats)[0,0]
        if xa==1 or xa==0:
            return float('inf')
        #极大似然估计
        cost_sum+=y[i]*np.log(xa)+(1-y[i])*np.log(1-xa)
    return -1/x.shape[0]*cost_sum





from sklearn.model_selection import train_test_split
from sklearn import datasets

iris = datasets.load_iris()

X = iris['data']

y = iris['target']

X = X[y != 2]

y = y[y != 2]

X_train, X_test, y_train, y_test = train_test_split(X, y)
Logistic_regression(X_train,y_train)