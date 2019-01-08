import numpy as np
from matplotlib import pyplot as plt
from math import *

#待聚类散点图
x=np.random.random(100)*10
y=np.random.random(100)*cos(np.random.rand(1))*15
plt.scatter(x,y)
plt.show()

#k聚类数  k_point初始聚类点  x点坐标x  y点坐标y  z最大迭代次数
def kmeans_euclidean(k,k_point,x,y,z):
    #聚类list
    k_point_list=[]
    for k_1 in range(k):
        k_point_list.append([])
    #聚类
    for i in range(len(x)):
        d=float('inf')
        for point in range(len(k_point)):
            #欧式距离
            euclidean=sqrt(pow(x[i]-k_point[point][0],2)+pow(y[i]-k_point[point][1],2))
            if euclidean<d:
                d=euclidean
                aim=point
        k_point_list[aim].append([x[i],y[i]])
    #重新计算质心
    for k_2 in range(len(k_point_list)):
        item=True
        k_point_meanx = np.mean(np.array(k_point_list[k_2])[:,0])
        k_point_meany = np.mean(np.array(k_point_list[k_2])[:,1])
        if k_point[k_2][0]!=k_point_meanx or k_point[k_2][1]!=k_point_meany:
            k_point[k_2]=[k_point_meanx,k_point_meany]
            item=False
    #质心是否发生变化
    if item:
        return k_point,k_point_list
    else:
        #是否超过最大迭代次数
        if z>0:
            return kmeans_euclidean(k,k_point,x,y,z-1)
        else:
            return k_point,k_point_list


a,b=kmeans_euclidean(3,[[2,3],[4,5],[6,7]],x,y,1000)

a=np.array(a)
plt.scatter(a[:,0],a[:,1],color='red',marker='x')
b0=np.array(b[0])
plt.scatter(b0[:,0], b0[:,1],c='blue')
b1=np.array(b[1])
plt.scatter(b1[:,0], b1[:,1],color='green')
b2=np.array(b[2])
plt.scatter(b2[:,0], b2[:,1],color='black')
plt.show()