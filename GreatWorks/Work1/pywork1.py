# -*- coding: gbk -*- 
#  ! ʵ��7 ����һ ��������
import pandas as pd
from pandas import *
from matplotlib import pyplot as plt

Scor = pd.read_csv('�ɼ���.csv', encoding='gbk')  # ��csv�ļ�����,��������ֵ
Info = pd.read_csv('��Ϣ��.csv', encoding='utf-8')  # ��csv�ļ�����,��������ֵ

# �����쳣����: ���ｫȱ���Ķ���ֵΪ0��., type����
ty = list(Scor['�ߴ�'])
j = 0
for i in ty:
    if i == 'ȱ��':
        Scor.at[j, '�ߴ�'] = 0
    j += 1

for i in list(Scor.columns):
    if Scor[i].dtype == 'O':  # ��ĳ��ȫ���� int ����ʾ����Ϊ int ���ͣ�����Ϊ object 
        print(i)  # �����ߴ�������һ�� 'ȱ��'���ݶ������������쳣
Scor['�ߴ�'] = to_numeric(Scor['�ߴ�'])  # ʹ����toNum������Ϊint����.

# ������õĳɼ�����������һ�ݸ���
Scor_copy = Scor.copy()

# !1: 1�����ɼ�����������У�
Scor['����'] = Info['����']

# !2: 2�����ɼ�������ֶΡ��ܷ֡��У�������ܷ֣�
Scor['�ܷ�'] = Scor.iloc[:, 1:4].sum(axis=1)

# !3: 3���������ֶΡ��ȼ�������עÿ�˵ġ��š������С����񡢲��90���ţ�80������70���У������60�����60����
tem = Scor[['C#', '�ߴ�', 'python']]  # ? ��ȡ��
Scor['�ܷ�'] = tem.sum(axis=1)  # ����ֽܷ��(270<=�ţ�240����210�У�����180����<=180)
Scor['�ȼ�'] = cut(Scor['�ܷ�'], [0, 180, 210, 240, 270, 999], right=False, labels=['��', '����', '��', '��', '��'])

# !4: 4��������ſγ̵�ƽ���ɼ��Լ���׼�
mean = Scor_copy.mean()
std = Scor_copy.std()  # ʹ�ø���,��ȥ��ѧ�����

print(Scor, "���Ƶ�ƽ���ɼ��ֱ�Ϊ", ''.join(str(([x for x in mean if x != mean[0]]))), "���Ƶ�ƽ���ɼ���׼��ֱ�Ϊ", ''.join(str(([x for x in std if x != std[0]]))))

# ! 5: 5����һ�ֳܷɼ��ֲ�ͼ���������ʾ�ɼ����������ʾѧ�ţ������ֵܷ� ���ֺ��� ��ÿ�˵� �ܷ�Բ��ͼ��
meanAll = Scor.mean()  # �ܷ�ƽ����:index==4

plt.rcParams['font.sans-serif'] = ['Simhei']  # ��������
plt.title('�ֳܷɼ��ֲ�ͼ')
plt.bar(range(len(Scor['�ܷ�'])), Scor['�ܷ�'], width=0.8)  # ��״ͼ
plt.plot(range(len(Scor['�ܷ�'])), Scor['�ܷ�'], color='b', alpha=0.5, linestyle='--', linewidth=5, marker='o', markeredgecolor='r', markersize='10', markeredgewidth=2)  # ����ͼ��Բ��
plt.axhline(meanAll[4], color='red', linestyle='--')  # ���ֺ���
plt.xticks(range(len(Scor['ѧ��'])), Scor['ѧ��'])  # ������

plt.show()
