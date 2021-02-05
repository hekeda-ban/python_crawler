# -*--coding:utf-8 -*--
# @Time : 2020/9/2 17:09
# @Author : BAY
# @File : 电影票房.py
# @Software : PyCharm
# 2021/2/5发现用此链接爬取内容已出错，该网站网页结构发生变化
# 此链接已失效但是其中的数据处理可以参考
import requests
import json


def down(year):
    url = 'https://www.endata.com.cn/API/GetData.ashx'
    data = {
        'year': year,
        'MethodName': 'BoxOffice_GetYearInfoData'
    }
    # 动态加载 有参数
    response = requests.get(url, data=data)
    resdict = json.loads(response.text)
    print(resdict)
    cards = resdict['Data']['Table']
    # a表示append 追加 把之前爬取的数据保留
    f = open("电影票房.csv", mode="a")
    for card in cards:
        Movieid = card['Movieid']
        # 影片名称
        MovieName = card['MovieName']
        # 类型
        Genre_Main = card['Genre_Main']
        # 总票房（万）
        BoxOffice = card['BoxOffice']
        f.write(str(Movieid))
        f.write(",")
        f.write(MovieName)
        f.write(",")
        f.write(Genre_Main)
        f.write(",")
        f.write(str(BoxOffice))
        f.write(",")
        f.write("\n")


years = range(2017, 2021)
for year in years:
    down(year)