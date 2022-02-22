# -*--coding:utf-8 -*--
# @Time : 2020/7/28 18:12
# @Author : BAY
# @File : doubanTop250_all.py
# @Software : PyCharm
import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    # dbpath = "movie.db"
    savepath = "./豆瓣电影TOP250.xls"
    save_excel_Data(datalist, savepath)
    # saveData2DB(datalist, dbpath)


# 创建正则表达式对象，表示规则（字符串模式）
# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)#忽略换行符号，让换行符包含在字符中
# 影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 找到评价人数
findJudge = re.compile(r'<span>(\d+)人评价</span>')
# 找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)


# 爬取网页
def getData(baseurl):
    datalist = []  # 保存一部电影item全部消息
    for i in range(0, 1):  # 调用获取页面信息的函数
        url = baseurl + str(i*25)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item) #测试
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            imgsrc = re.findall(findImgSrc, item)[0]
            data.append(imgsrc)

            titles = re.findall(findTitle, item)  # 片名可能只有一个中文名
            if len(titles) == 2:
                ctitle = titles[0]  # 中文名
                data.append(ctitle)
                otitle = titles[1].replace("/", "")  # 将无关符号去掉 外文名
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')  # 留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append(" ")  # 留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉<br>
            bd = re.sub('/', " ", bd)  # 替换/
            data.append(bd.strip())  # 去掉空格

            # 处理好的一部电影信息
            datalist.append(data)
    # print(len(datalist),datalist)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    # 用户代理，告诉豆瓣服务器，我们是什么类型的机器，浏览器本质上告诉浏览器，我们可以接收什么水平的文件内容
    headers = {
         "User-Agent": "Mozilla/5.0"
    }
    # 模拟浏览器头部信息 #url伪装 封装
    request = urllib.request.Request(url=url,headers=headers)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def save_excel_Data(datalist, savepath):
    workbook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    workseet = workbook.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名字", "影片外文名字", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        workseet.write(0, i, col[i])  # 列名
    for i in range(0, 25):
        print("第%d条" % (i+1))
        data = datalist[i]
        for j in range(0, 8):
            workseet.write(i+1, j, data[j])
    workbook.save(savepath)


def saveData2DB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = '''
            insert into movieT250(
            info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)
            ''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
        create table movieT250
        (id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text);
        '''
    connect = sqlite3.connect(dbpath)  # 打开或创建数据库文件
    c = connect.cursor()  # 获取游标
    c.execute(sql)  # 执行sql语句
    connect.commit()  # 提交数据库操作
    connect.close()  # 关闭数据库连接
    print("建表成功")


if __name__ == '__main__':
    # 调用函数
    main()
    # init_db("movietest.db")
    print("爬取完毕")

