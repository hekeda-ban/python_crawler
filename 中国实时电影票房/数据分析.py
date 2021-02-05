# -*--coding:utf-8 -*--
# @Time : 2020/9/11 17:24
# @Author : BAY
# @File : 数据分析.py
# @Software : PyCharm
# 用pandas分析数据
import pandas as pd
# 不能让第一行作为列名
data = pd.read_csv("电影票房.csv", encoding="gbk", header=None)
# 从data中 拿到第2列 和第3列的数据
# 每一行都要
data = data.loc[:, [2, 3]]
# print(data)
# 拆分类别数据
# 将魔幻/动作拆成魔幻 动作


def func1(item):
    # 把每一个类别进行处理 #魔幻/动作
     return item.split("/")[0]


def func2(item):
    if "/" in item:
        return item.split("/")[1]
    else:
        return "ban"


data[4] = data[2].map(func1)
data[5] = data[2].map(func2)

data_1 = data.loc[:, [4, 3]]
data_2 = data.loc[:, [5, 3]]
# 把data_2 里面是ban 的数据干掉
data_2 = data_2.loc[data[5] != "ban"]
# 把5号改为4号列名
data_2 = data_2.rename(columns={5: 4})
data = data_1.append(data_2)
# 计算每一种类型票房的平均值
data = data.groupby(4).mean().round(2)
# 保存数据
data.to_csv("后天要用的数据.csv")