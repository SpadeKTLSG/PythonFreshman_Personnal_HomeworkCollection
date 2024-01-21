# -*- coding: gbk -*- 
#  ! 实验7 问题一 数据清理
import pandas as pd
from pandas import *
from matplotlib import pyplot as plt

Scor = pd.read_csv('成绩表.csv', encoding='gbk')  # 从csv文件导入,设置行列值
Info = pd.read_csv('信息表.csv', encoding='utf-8')  # 从csv文件导入,设置行列值

# 清理异常数据: 这里将缺考的对象赋值为0分., type处理
ty = list(Scor['线代'])
j = 0
for i in ty:
    if i == '缺考':
        Scor.at[j, '线代'] = 0
    j += 1

for i in list(Scor.columns):
    if Scor[i].dtype == 'O':  # 若某列全部是 int 则显示该列为 int 类型，否则为 object 
        print(i)  # 发现线代由于有一个 '缺考'数据而出现了类型异常
Scor['线代'] = to_numeric(Scor['线代'])  # 使用了toNum方法改为int属性.

# 将处理好的成绩单样本保存一份副本
Scor_copy = Scor.copy()

# !1: 1）给成绩表加上姓名列；
Scor['姓名'] = Info['姓名']

# !2: 2）给成绩表加上字段“总分”列，并求出总分；
Scor['总分'] = Scor.iloc[:, 1:4].sum(axis=1)

# !3: 3）增加列字段“等级”，标注每人的“优、良、中、及格、差”（90≤优，80≤良，70≤中，及格≤60，差≤60）；
tem = Scor[['C#', '线代', 'python']]  # ? 提取列
Scor['总分'] = tem.sum(axis=1)  # 求和总分结果(270<=优，240良，210中，及格180，差<=180)
Scor['等级'] = cut(Scor['总分'], [0, 180, 210, 240, 270, 999], right=False, labels=['差', '及格', '中', '良', '优'])

# !4: 4）计算各门课程的平均成绩以及标准差；
mean = Scor_copy.mean()
std = Scor_copy.std()  # 使用副本,并去除学号输出

print(Scor, "三科的平均成绩分别为", ''.join(str(([x for x in mean if x != mean[0]]))), "三科的平均成绩标准差分别为", ''.join(str(([x for x in std if x != std[0]]))))

# ! 5: 5）做一总分成绩分布图，纵坐标表示成绩，横坐标表示学号，画出总分的 均分横线 和每人的 总分圆点图。
meanAll = Scor.mean()  # 总分平均分:index==4

plt.rcParams['font.sans-serif'] = ['Simhei']  # 导入字体
plt.title('总分成绩分布图')
plt.bar(range(len(Scor['总分'])), Scor['总分'], width=0.8)  # 柱状图
plt.plot(range(len(Scor['总分'])), Scor['总分'], color='b', alpha=0.5, linestyle='--', linewidth=5, marker='o', markeredgecolor='r', markersize='10', markeredgewidth=2)  # 折线图加圆点
plt.axhline(meanAll[4], color='red', linestyle='--')  # 均分横线
plt.xticks(range(len(Scor['学号'])), Scor['学号'])  # 横坐标

plt.show()
