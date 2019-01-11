import numpy as np
from matplotlib import pyplot as plt
from math import *

#待聚类散点图
x=np.random.random(100)*10
y=np.random.random(100)*cos(np.random.rand(1))*15
xy=np.array([x,y]).T
plt.scatter(x,y)
# plt.show()

#随机初始质心
def random_point(k,xy):
    first_point_list=[]
    for i in range(k):
        xyrange=[]
        for columns_xy in range(len(xy[0,:])):
            xyrange.append(min(xy[:,columns_xy]) + (max(xy[:,columns_xy]) - min(xy[:,columns_xy])) * np.random.rand(1)[0])
        first_point_list.append(xyrange)
    return first_point_list


#k聚类数  xy点坐标  z最大迭代次数 k_point初始聚类点
def kmeans_euclidean(k,xy,z=1000,k_point=None):
    #聚类质心数组
    if not k_point:
        k_point=random_point(k,xy)
    #存放质心、欧式距离的数组
    k_point_array=np.zeros([len(xy),2])
    #聚类
    for i in range(len(xy)):
        d=inf
        for point in range(len(k_point)):
            #欧式距离
            euclidean=sqrt(pow(xy[i,0]-k_point[point][0],2)+pow(xy[i,1]-k_point[point][1],2))
            if euclidean<d:
                d=euclidean
                aim=point
        k_point_array[i,:]=aim,d
    #重新计算质心
    for k_2 in range(k):
        item=True
        k_point_meanx = np.mean(xy[k_point_array[:, 0] == k_2][:, 0])
        k_point_meany = np.mean(xy[k_point_array[:, 0] == k_2][:, 1])
        if k_point[k_2][0]!=k_point_meanx or k_point[k_2][1]!=k_point_meany:
            k_point[k_2]=[k_point_meanx,k_point_meany]
            item=False
    #质心是否发生变化
    if item:
        return k_point,k_point_array
    else:
        #是否超过最大迭代次数
        if z>0:
            return kmeans_euclidean(k,xy,z-1,k_point)
        else:
            return k_point,k_point_array


#二分k均值函数
def bisecting_kmeans(k,xy,z=1000):
    #初始一个质心
    point_list=random_point(1, xy)
    #质心、sse数组
    sse_array = np.zeros([len(xy),2])
    #初始误差
    for xy_i in range(len(xy)):
        sse_array[xy_i,1] = pow(xy[xy_i,0] - point_list[0][0], 2) + pow(xy[xy_i,1] - point_list[0][1], 2)

    while len(point_list)<k:
        sse=inf
        for bisecting in range(len(point_list)):
            sse_array_copy=sse_array.copy()
            #分成2类
            k_point, k_point_array=kmeans_euclidean(2,xy[sse_array_copy[:,0]==bisecting])
            for k_1 in range(len(k_point_array)):
                k_point_array[k_1,1]=pow(k_point_array[k_1,1],2)
            k_point_array[k_point_array[:, 0] == 1, 0] = len(point_list)
            k_point_array[k_point_array[:, 0] == 0, 0] = bisecting
            sse_array_copy[sse_array_copy[:,0]==bisecting]=k_point_array
            #是否为最小误差
            if sse>sum(sse_array_copy[:,1]):
                k_point_array_copy=k_point_array
                bisecting_copy=bisecting
                k_point_copy=k_point
                sse=sum(sse_array_copy[:, 1])
        #最小误差聚类
        sse_array[sse_array[:, 0] == bisecting_copy] = k_point_array_copy
        point_list[bisecting_copy]=k_point_copy[0]
        point_list.append(k_point_copy[1])

    return point_list,sse_array



a,b=bisecting_kmeans(4,xy)
print(b[b[:,0]==0].shape[0])
print(b[b[:,0]==1].shape[0])
print(b[b[:,0]==2].shape[0])
print(b[b[:,0]==3].shape[0])

a=np.array(a)
plt.scatter(a[:,0],a[:,1],color='red',marker='x')
plt.scatter(xy[b[:,0]==0,0], xy[b[:,0]==0,1],c='blue')
plt.scatter(xy[b[:,0]==1,0], xy[b[:,0]==1,1],color='green')
plt.scatter(xy[b[:,0]==2,0], xy[b[:,0]==2,1],color='black')
plt.scatter(xy[b[:,0]==3,0], xy[b[:,0]==3,1],color='yellow')
plt.show()