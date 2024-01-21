# -*- coding: gbk -*- 
# ! py数据分析实战练习


import pandas as pd  # 导入pandas库
from pandas import *  # 导入pandas库

# * Series 基础

# 手动输入:
A = Series(['织田', '岛津', '武田', '今川', '北条', '毛利', '上杉', '伊达'], index=[1, 2, 3, 4, 5, 6, 7, 8])

# 列表输入(Good): 索引直接加上了可以下标访问
B = Series(['洛阳', '大都', '建邺'], index=range(1, 4))

# 链接:
# A = A.append(B)

A = concat([A, B])  # 可以重新设定参数等 左右拼接axis=1

# 判断存在: in , 数字逻辑不用'' ,需要用.values找值,不然一直是找不到
print('岛津' in A.values, '\n\n\n')

# 切片
print(A[1:3], '\n\n\n')

# 删除: 按Index 和 按位置 和 按值 , 需要返回s
B = B.drop(1)
B = B.drop(B.index[1])
B = B['大都' != B.values]
# 删光了

# ! 通过值访问index: 
print(A.index[A.values == '岛津'], '\n\n\n')

# 更改index : 整齐右移几位.
A.index = range(11, len(A) + 11)

# ? 字典转Series :
C = Series({'a': 1, 'b': 2, 'c': 3})

# ! 排序: 改成降序--> ascending
C = C.sort_index(ascending=False)

print(A, '\n\n\n')

print(B, '\n\n\n')

print(C, '\n\n\n')

# * Dataframe 基础

df1 = DataFrame({'age': Series([24, 25, 26]), 'name': Series(['李田所', '浩二', '先辈'])})

# * 四种访问

# 访问列 -- 列名

print(df1['name'], '\n\n\n\n')

# 访问行 --切片表

print(df1[1:2], '\n\n\n\n')  # 访问 第二行(1)

# 访问块 --iloc双重切片[:,:]
print(df1.iloc[0:1, 0:2], '\n\n\n\n')  # 签名是列, 后面是行

# 访问位置,输出值--at定位[,], 前面是行, 后面是列名字
print(df1.at[1, 'name'], '\n\n\n\n')

# 更改列名 :直接

# 访问指定列的值: 
print(df1[df1.columns[0:1]], '\n\n\n\n')

# 删除: 行索引 , 列索引, 需要axis

# df1 = df1.drop(1, axis=0)  # 0 == 行轴
# df1 = df1.drop('name', axis=1)  # 1== 列轴
# print(df1)

# 另外删除列:
del df1['name']
print(df1, '\n\n\n\n')

# 增加列: 
df1['体重'] = [114, 514, 1919]
print(df1, '\n\n\n\n')

# 合并两个, 生成新的索引:
df2 = df1

df3 = df1.append(df2, ignore_index=True)
print(df3)

# *CSV 导入:

df = pd.read_csv('TestDataSourse.csv', names=['汉化', '狠狠', '哄哄'])  # 从csv文件导入,设置行列值

print(df)
