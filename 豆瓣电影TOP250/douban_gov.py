# -*--coding:utf-8 -*--
#@Time : 2020/7/27 21:16
#@Author : BAY
#@File : douban_gov.py
#@Software : PyCharm
import socket
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import time


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
        html_count = response.read().decode('utf-8')
        response.close()
    except urllib.error.URLError as e:
        print(e.reason)
    return html_count


def get_content(html_count):
    soup = BeautifulSoup(str(html_count),"html.parser")
    douban_gov(soup)


def douban_gov(soup):
    content_data = []
    ISOTIMEFORMAT1 = '%Y-%m-%d %X'
    #< span property = "v:itemreviewed" > 肖申克的救赎TheShawshankRedemption < / span >
    movie_name = soup.find("span",property="v:itemreviewed")
    print(movie_name.string)

    pic = soup.find("img",)
    print(pic)


if __name__ == '__main__':
    url ='https://movie.douban.com/subject/1292052/'
    html_count = douban_url(url)
    get_content(html_count)