# -*--coding:utf-8 -*--
# @Time : 2021/1/28 18:25
# @Author : BAY
# @File : 彩票数据简易分析.py
# @Software : PyCharm
import pandas as pd  # 做数据处理和分析、清洗
import matplotlib.pyplot as plt  # 用来做可视化，把数据变成图表
# 引入数据  处理表头 处理行索引
df = pd.read_csv('data.csv', skiprows=1, header=None, index_col=0)
print(df)
# 把红球的号码拿出来
# 列：从1到6 行：所有行
red_ball = df.loc[:, 1:6]
# print(red_ball)
# 把篮球的号码拿出来
blue_ball = df.loc[:, 7]
# print(blue_ball)
# 做数据统计
# 每个号码出现的次数   转为1维数据
red_ball_count = pd.value_counts(red_ball.values.flatten())
# print(red_ball_count)

blue_ball_count = pd.value_counts(blue_ball)
# print(blue_ball_count)
# 可视化展示--制作成图表

# 一次创建很多个图标
# fig, ax = plt.subplots(2, 1)
# 用饼图展示                                             半径         扇形属性
plt.pie(red_ball_count, labels=red_ball_count.index, radius=1, wedgeprops={"width":0.3})

plt.pie(blue_ball_count, labels=blue_ball_count.index, radius=0.5, wedgeprops={"width":0.2})

plt.show()