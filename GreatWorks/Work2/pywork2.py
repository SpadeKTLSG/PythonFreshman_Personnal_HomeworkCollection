# -*- coding: gbk -*- 
#  ! 实验7 问题二 数据清理
import pandas as pd
from pandas import *

df = pd.read_csv('学习成绩.csv', encoding='gbk')  # 从csv文件导入,设置行列值
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)  # 显示所有行列

# ! 0)有效清洗去除重复值，异常值，空值，以及多余的空格等问题。
# 去除重复行
# print(df.shape)  # (18,10列)
df = df.drop_duplicates()  # 删除重复数据行  

# 去除缺失值
# print(df1[df1.isnull().values == True])  # 显示存在缺失值的行 --未发现

# 去除空格
df['英语'] = df['英语'].astype(str).map(str.strip)
df['军训'] = df['军训'].astype(str).map(str.strip)
df['体育'] = df['体育'].astype(str).map(str.strip)
df['数分'] = df['数分'].astype(str).map(str.strip)
df['高代'] = df['高代'].astype(str).map(str.strip)
df['解几'] = df['解几'].astype(str).map(str.strip)

# 去除缺考等异常值
ty = list(df['军训'])
j = 0
for i in ty:
    if i == '缺考':
        df.at[j, '军训'] = 0
    j += 1

ty = list(df['体育'])
j = 0
for i in ty:
    if i == '作弊':
        df.at[j, '体育'] = 0
    j += 1

"""print("修改类型前")
for i in list(df.columns):
    if df[i].dtype == 'O':  # 若某列全部是 int 则显示该列为 int 类型，否则为 object 
        print(i)
        print(df[i].dtype)
"""
df['体育'] = to_numeric(df['体育'])  # 使用了toNum方法改为int属性.
df['军训'] = to_numeric(df['军训'])  # 使用了toNum方法改为int属性.
df['英语'] = to_numeric(df['英语'])  # 使用了toNum方法改为int属性.
df['数分'] = to_numeric(df['英语'])  # 使用了toNum方法改为int属性.
df['高代'] = to_numeric(df['英语'])  # 使用了toNum方法改为int属性.
df['解几'] = to_numeric(df['英语'])  # 使用了toNum方法改为int属性.

"""print("修改类型后")
for i in list(df.columns):
    if df[i].dtype == 'O':  # 若某列全部是 int 则显示该列为 int 类型，否则为 object 
        print(i)
        print(df[i].dtype)
"""

# 将处理好的样本保存一份副本
df_copy = df.copy()

# ! 1）、将数据表添加两列：各科成绩总分(score)和每位同学的整体情况（类别）类别按 照[df.score.min()-1,400,450,df.score.max()+1]分为"一般","较好","优秀"三种情况。
tem = df[['英语', '体育', '军训', '数分', '高代', '解几']]  # 同前,抽取列
df['总分'] = tem.sum(axis=1)

L1 = min(df['总分']) - 1
L2 = max(df['总分']) + 1
df['类别'] = cut(df['总分'], [L1, 400, 450, L2], right=False, labels=['一般', '较好', '优秀'])

print(df, '处理')

# ! 2）、“军训”差异较大，请将各科成绩标准化再汇总，标出"一般","较好","优秀"三种 类别。标准化解释:将数据的最大最小值记录下来，并通过Max-Min作为基数（即Min=0，Max=1）进行数据的归一化处理。x = (x - Min) / (Max - Min)
for i in df_copy.columns[4:11]:
    H1 = max(df_copy[i]) - min(df_copy[i])
    for k in df_copy.index:
        df_copy.at[k, i] = (df_copy.at[k, i] - min(df_copy[i])) / H1

# 重新设计区间,根据范例获取如下分割
tem = df_copy[['英语', '体育', '军训', '数分', '高代', '解几']]  # 同前,抽取列
df_copy['总分'] = tem.sum(axis=1)

L1 = min(df_copy['总分']) - 1
L2 = max(df_copy['总分']) + 1

df_copy['新类别'] = cut(df_copy['总分'], [L1, 8, 14, L2], right=False, labels=['一般', '较好', '优秀'])
print(df_copy, '标准化处理')
