# -*--coding:utf-8 -*--
# @Time : 2020/9/12 11:07
# @Author : BAY
# @File : myflask.py
# @Software : PyCharm

# helloworld
from flask import Flask, render_template, request
# 创建应用程序
app = Flask(__name__)
# # 写一个函数来处理浏览器发送过来的请求
# @app.route("/") # 当访问127.0.0.1:5000/
# def index():
#     #这里来处理业务逻辑
#     return "12345678"   #返回的数据 响应
# @app.route("/jay")
# def 周杰伦():
#     return "你好啊，周杰伦"

# 模板 ->html
# @app.route("/")
# def index():
#     return render_template("hello.html")
#  把一个变量发送到一个页面
# @app.route("/")
# def index():
#     # 字符串
#     s = "你好亲"
#     lst = ['周杰伦', '白敬亭', '章节', '李沁']
#     return render_template("hello.html", jay=s, lst=lst)


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login",methods=['post'])
def login():
    # 接收用户名 密码
    username = request.form.get('username')
    pwd = request.form.get("pwd")
    if username == "ban" and pwd == "123":
        return "成功"
    else:
        return render_template("login.html", msg="登陆失败")


# 从页面接收数据
if __name__ == '__main__':  # 程序的入口
    app.run()   # 启动应用程序启动一个flask框架