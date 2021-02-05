# -*--coding:utf-8 -*--
# @Time : 2020/9/12 17:17
# @Author : BAY
# @File : myflaskvisuallization.py
# @Software : PyCharm
from flask import Flask, render_template
import pandas as pd
# 文件夹名字固定
# 创建一个app
app = Flask(__name__)
# 准备一个函数，来处理浏览器发送过来的请求
# 装饰器 路由

@app.route("/")
def show():
    # 读取到csv文件中的内容
    data = pd.read_csv("后天要用的数据.csv")
    # print(data)
    data = data.rename(columns={"4": "name"})
    data = data.rename(columns={"3": "value"})
    # print(data)
    # {value: 335, name: '直接访问'},
    data = data.to_dict(orient="records")
    return render_template("show.html",data=data)

# 运行app
if __name__ == '__main__':
    app.run()