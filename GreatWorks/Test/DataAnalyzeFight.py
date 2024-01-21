# -*- coding: gbk -*- 
# ! py���ݷ���ʵս��ϰ


import pandas as pd  # ����pandas��
from pandas import *  # ����pandas��

# * Series ����

# �ֶ�����:
A = Series(['֯��', '����', '����', '��', '����', 'ë��', '��ɼ', '����'], index=[1, 2, 3, 4, 5, 6, 7, 8])

# �б�����(Good): ����ֱ�Ӽ����˿����±����
B = Series(['����', '��', '����'], index=range(1, 4))

# ����:
# A = A.append(B)

A = concat([A, B])  # ���������趨������ ����ƴ��axis=1

# �жϴ���: in , �����߼�����'' ,��Ҫ��.values��ֵ,��Ȼһֱ���Ҳ���
print('����' in A.values, '\n\n\n')

# ��Ƭ
print(A[1:3], '\n\n\n')

# ɾ��: ��Index �� ��λ�� �� ��ֵ , ��Ҫ����s
B = B.drop(1)
B = B.drop(B.index[1])
B = B['��' != B.values]
# ɾ����

# ! ͨ��ֵ����index: 
print(A.index[A.values == '����'], '\n\n\n')

# ����index : �������Ƽ�λ.
A.index = range(11, len(A) + 11)

# ? �ֵ�תSeries :
C = Series({'a': 1, 'b': 2, 'c': 3})

# ! ����: �ĳɽ���--> ascending
C = C.sort_index(ascending=False)

print(A, '\n\n\n')

print(B, '\n\n\n')

print(C, '\n\n\n')

# * Dataframe ����

df1 = DataFrame({'age': Series([24, 25, 26]), 'name': Series(['������', '�ƶ�', '�ȱ�'])})

# * ���ַ���

# ������ -- ����

print(df1['name'], '\n\n\n\n')

# ������ --��Ƭ��

print(df1[1:2], '\n\n\n\n')  # ���� �ڶ���(1)

# ���ʿ� --iloc˫����Ƭ[:,:]
print(df1.iloc[0:1, 0:2], '\n\n\n\n')  # ǩ������, ��������

# ����λ��,���ֵ--at��λ[,], ǰ������, ������������
print(df1.at[1, 'name'], '\n\n\n\n')

# �������� :ֱ��

# ����ָ���е�ֵ: 
print(df1[df1.columns[0:1]], '\n\n\n\n')

# ɾ��: ������ , ������, ��Ҫaxis

# df1 = df1.drop(1, axis=0)  # 0 == ����
# df1 = df1.drop('name', axis=1)  # 1== ����
# print(df1)

# ����ɾ����:
del df1['name']
print(df1, '\n\n\n\n')

# ������: 
df1['����'] = [114, 514, 1919]
print(df1, '\n\n\n\n')

# �ϲ�����, �����µ�����:
df2 = df1

df3 = df1.append(df2, ignore_index=True)
print(df3)

# *CSV ����:

df = pd.read_csv('TestDataSourse.csv', names=['����', '�ݺ�', '���'])  # ��csv�ļ�����,��������ֵ

print(df)
