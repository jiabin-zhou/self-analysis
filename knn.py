import numpy as np
import pandas as pd
import random

#加权k临近
def weight_knn(x, dateset, k):
    x=np.array(x)
    #欧式距离array
    distance=euclidean(x, dataset)
    #距离array插入dataset末尾列
    dataset_distance=np.c_[dataset,distance]
    dataset_sort=dataset_distance[np.lexsort(dataset_distance.T[-1,None])][:k,:]
    #计算权重值
    dataset_gaussian=gaussian(dataset_sort)
    df=pd.DataFrame(dataset_gaussian)
    dataset_pivot=pd.pivot_table(df,index=df.columns[-2],values=df.columns[-1],aggfunc=np.sum)
    #排序
    dataset_pivot=dataset_pivot[3].sort_values(ascending=False)
    #获得权重和最大的lable为预测值
    dataset_lable=dataset_pivot.index[0]
    return dataset_lable


#创建数据集(x,y,lable)
def create_data(n,lable):
    data=[]
    for i in range(n):
        data.append([random.uniform(0, 100),random.uniform(0, 100),random.choice(list(range(lable)))])
    return np.array(data)

#计算数据集各点与目标点的欧式距离
def euclidean(x,dataset):
    b=map(lambda a:np.sqrt(pow((a[0]-x[0]),2)+pow((a[1]-x[1]),2)),dataset)
    return np.array(list(b))


#权重 高斯函数
def gaussian(dataset_sort,a=1,b=0,c=0.3):
    d=dataset_sort[:,-1]
    for i in range(len(d)):
        dataset_sort[i,-1]=a*np.exp(-(d[i]-b)**2/(2*c**2))
    return dataset_sort



dataset=create_data(100,3)
weight_knn([50,50],dataset,10)