# -*--coding:utf-8 -*--
#@Time : 2020/7/27 20:18
#@Author : BAY
#@File : doubanmovie_url.py
#@Software : PyCharm
#爬取豆瓣电影Top250的基本信息，包括电影的名称、豆瓣评分、
# 评价数、电影概况、电影链接等

import socket
import urllib.request #制定URL，获取网页数据
import urllib.error
from bs4 import BeautifulSoup#网页解析、获取数据
import xlwt#进行excel操作
import re#正则表达式，进行文字匹配
import sqlite3 #进行sqlite3数据库操作


def douban_url(url):
    socket.setdefaulttimeout(20)
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    try:
        request = urllib.request.Request(url,headers=headers)
        response = urllib.request.urlopen(request)
        if response.getcode() != 200:
            return None
        html_count = response.read()
        response.close()
    except urllib.error.URLError as e:
        print(e.reason)
    return html_count


def get_newurls(html_count):
    new_links = []
    soup = BeautifulSoup(str(html_count),"html.parser")
    #<a href="https://movie.douban.com/subject/1292052/">
    #<a href="https://movie.douban.com/subject/1291546/">
    if len(soup.find_all('a',href=re.compile(r'^https://movie.douban.com/subject/\d+/')))>0:
        links = soup.find_all('a',href=re.compile(r'^https://movie.douban.com/subject/\d+/'))
        for link in links:
            link1=link['href']
            new_links.append(link1)

    print(len(new_links),new_links)


if __name__ == '__main__':
    url = "https://movie.douban.com/top250"
   # https: // movie.douban.com / top250?start = 25 & filter =
   # https: // movie.douban.com / top250?start = 50 & filter =
    #每页的URL不同之处最后的数值=（页数-1）*25
    html_count = douban_url(url)
    get_newurls(html_count)
