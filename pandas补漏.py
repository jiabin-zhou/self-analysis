

#将列设置为索引  set_index
	DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
	#keys:列名，list（多列或单列）或字符串（单列）
	#drop:默认True，列转换成索引后删除原列
	#append：是否保留原索引，添加新索引到原有索引
	#inplace:修改替换原DataFrame
	#verify_integrity：检查重复的新索引



#多重索引定位
	#IndexSlice获取数据集的索引切片
	idx = pd.IndexSlice
	#假设有3个索引列，DataFrame所有数据
	df.loc[idx[:,:,:],:]
	#指定索引列中指定索引的数据（int/str/list)
	df.loc[idx["第一索引列中的指定索引名",:,['第三索引列中的指定索引名','第三索引列中的指定索引名']],:]



#数据透视
	pd.pivot_table(df,values='D',index=['B'],columns=['A', 'C'],aggfunc=np.sum)  #you know



#单条件/多条件过滤的多种形式
	import pandas as pd
	df = pd.DataFrame([{'col1':'a', 'col2':1}, {'col1':'b', 'col2':2}, {'col1':'c', 'col2':3}])
	#单条件过滤，结果一致
	df.loc[df['col1'] == 'a']
	df[df['col1'] == 'a']
	df.where(df['col1']=='a').dropna()   #where替换数据功能  df.where(df.notnull(), None)  将df中非null数据替换成None
	#多条件过滤，结果一致
	df.loc[df['col1'] == 'c'].loc[df['col2'] > 1]
	df[(df['col1'] == 'c')&(df['col2'] > 1)]


#替换某一列中指定值
df3[1].replace([2,3,4],[200,300,400],inplace=True)#1列