# -*- coding: gbk -*- 
#  ! ʵ��7 ����� ��������
import pandas as pd
from pandas import *

df = pd.read_csv('ѧϰ�ɼ�.csv', encoding='gbk')  # ��csv�ļ�����,��������ֵ
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)  # ��ʾ��������

# ! 0)��Ч��ϴȥ���ظ�ֵ���쳣ֵ����ֵ���Լ�����Ŀո�����⡣
# ȥ���ظ���
# print(df.shape)  # (18,10��)
df = df.drop_duplicates()  # ɾ���ظ�������  

# ȥ��ȱʧֵ
# print(df1[df1.isnull().values == True])  # ��ʾ����ȱʧֵ���� --δ����

# ȥ���ո�
df['Ӣ��'] = df['Ӣ��'].astype(str).map(str.strip)
df['��ѵ'] = df['��ѵ'].astype(str).map(str.strip)
df['����'] = df['����'].astype(str).map(str.strip)
df['����'] = df['����'].astype(str).map(str.strip)
df['�ߴ�'] = df['�ߴ�'].astype(str).map(str.strip)
df['�⼸'] = df['�⼸'].astype(str).map(str.strip)

# ȥ��ȱ�����쳣ֵ
ty = list(df['��ѵ'])
j = 0
for i in ty:
    if i == 'ȱ��':
        df.at[j, '��ѵ'] = 0
    j += 1

ty = list(df['����'])
j = 0
for i in ty:
    if i == '����':
        df.at[j, '����'] = 0
    j += 1

"""print("�޸�����ǰ")
for i in list(df.columns):
    if df[i].dtype == 'O':  # ��ĳ��ȫ���� int ����ʾ����Ϊ int ���ͣ�����Ϊ object 
        print(i)
        print(df[i].dtype)
"""
df['����'] = to_numeric(df['����'])  # ʹ����toNum������Ϊint����.
df['��ѵ'] = to_numeric(df['��ѵ'])  # ʹ����toNum������Ϊint����.
df['Ӣ��'] = to_numeric(df['Ӣ��'])  # ʹ����toNum������Ϊint����.
df['����'] = to_numeric(df['Ӣ��'])  # ʹ����toNum������Ϊint����.
df['�ߴ�'] = to_numeric(df['Ӣ��'])  # ʹ����toNum������Ϊint����.
df['�⼸'] = to_numeric(df['Ӣ��'])  # ʹ����toNum������Ϊint����.

"""print("�޸����ͺ�")
for i in list(df.columns):
    if df[i].dtype == 'O':  # ��ĳ��ȫ���� int ����ʾ����Ϊ int ���ͣ�����Ϊ object 
        print(i)
        print(df[i].dtype)
"""

# ������õ���������һ�ݸ���
df_copy = df.copy()

# ! 1���������ݱ�������У����Ƴɼ��ܷ�(score)��ÿλͬѧ����������������� ��[df.score.min()-1,400,450,df.score.max()+1]��Ϊ"һ��","�Ϻ�","����"���������
tem = df[['Ӣ��', '����', '��ѵ', '����', '�ߴ�', '�⼸']]  # ͬǰ,��ȡ��
df['�ܷ�'] = tem.sum(axis=1)

L1 = min(df['�ܷ�']) - 1
L2 = max(df['�ܷ�']) + 1
df['���'] = cut(df['�ܷ�'], [L1, 400, 450, L2], right=False, labels=['һ��', '�Ϻ�', '����'])

print(df, '����')

# ! 2��������ѵ������ϴ��뽫���Ƴɼ���׼���ٻ��ܣ����"һ��","�Ϻ�","����"���� ��𡣱�׼������:�����ݵ������Сֵ��¼��������ͨ��Max-Min��Ϊ��������Min=0��Max=1���������ݵĹ�һ������x = (x - Min) / (Max - Min)
for i in df_copy.columns[4:11]:
    H1 = max(df_copy[i]) - min(df_copy[i])
    for k in df_copy.index:
        df_copy.at[k, i] = (df_copy.at[k, i] - min(df_copy[i])) / H1

# �����������,���ݷ�����ȡ���·ָ�
tem = df_copy[['Ӣ��', '����', '��ѵ', '����', '�ߴ�', '�⼸']]  # ͬǰ,��ȡ��
df_copy['�ܷ�'] = tem.sum(axis=1)

L1 = min(df_copy['�ܷ�']) - 1
L2 = max(df_copy['�ܷ�']) + 1

df_copy['�����'] = cut(df_copy['�ܷ�'], [L1, 8, 14, L2], right=False, labels=['һ��', '�Ϻ�', '����'])
print(df_copy, '��׼������')
