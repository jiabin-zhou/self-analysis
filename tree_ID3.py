import pandas as pd
from math import log
import numpy as np

#信息熵计算函数
def math_entropy(entropy):
    entropy=[-(i/sum(entropy))*log(i/sum(entropy),2) for i in entropy if i!=0]
    entropy=sum(entropy)
    return entropy


#性别统计 存入字典
def count_sex_num(df):
    classList=[example for example in df[df.columns[-1]]]
    classdict={}
    for i in range(len(classList)):
        classdict[classList[i]]=classList.count(classList[i])
    return classdict


#判断最大互信息
def great_gain(df):
    # 性别统计字典
    classdict = count_sex_num(df)
    # 计算总信息熵
    entropy = [values for key, values in classdict.items()]
    entropy = math_entropy(entropy)
    # 开始判断最优特征
    gain=0
    c=df.columns
    c=[i for i in c]
    t=None
    for i in range(len(c)-1):
        #index属性,columns男女 数据透视表
        df1=df[[c[i],c[-1]]]
        df1=pd.pivot_table(df1,values=c[-1],index=c[i],columns=c[-1],aggfunc=len).fillna(0)
        #计算联合概率p
        p=[sum(df1.iloc[k,:]) for k in range(len(df1))]
        p=[k/sum(p) for k in p]
        #计算条件概率list1
        p2 = [df1.iloc[k, :] for k in range(len(df1))]
        list1=[]
        for x in p2:
            list2=[]
            for k in range(len(df1.columns)):
                list2.append(x[k]/sum(x))
            list1.append(list2)
        entropy2=[math_entropy(k) for k in list1]
        #计算条件熵
        ETX=[p[k]*entropy2[k] for k in range(len(entropy2))]
        ETX=sum(ETX)
        #判断互信息在最大值作为分支的节点
        if entropy-ETX>gain:
            gain=entropy-ETX
            t=c[i]
    return t


#生成决策树
def createtree(df):
    all_sexcount_list=[k for k in df[df.columns[-1]]]
    #如果全为一个性别，返回性别
    if all_sexcount_list.count(all_sexcount_list[0])==len(all_sexcount_list):
        return all_sexcount_list[0]
    #当仅剩一列（为性别），则按性别数量多少判断返回结果
    if len(df.columns)==1:
        all_sexcount_disc={}
        for k in all_sexcount_list:
            all_sexcount_disc[k]=all_sexcount_list.count(k)
            return max(all_sexcount_disc)
    #判断最优分支
    t=great_gain(df)
    myTree = {t:{}}
    # print(myTree)
    uniqueVals=set(df[t])
    uniqueVals=list(uniqueVals)
    #回调
    for value in uniqueVals:
        df2=df[df[t]==value]
        del df2[t]
        myTree[t][value]=createtree(df2)

    return myTree


df=pd.read_excel('data.xlsx')
print(createtree(df))