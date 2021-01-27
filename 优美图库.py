# -*--coding:utf-8 -*--
# @Time : 2021/1/26 21:46
# @Author : BAY
# @File : 优美图库.py
# @Software : PyCharm

# 技术点1、requests发送请求
# 2、BeautifulSoup解析整个页面源代码
# 爬取图片网站 发送请求到服务器
import requests
from bs4 import BeautifulSoup


def get_page(url):
    resp = requests.get(url)  # 从页面到源码
    resp.encoding = 'utf-8'
    # 解析html
    main_page = BeautifulSoup(resp.text, 'html.parser')
    return main_page


def get_next_url(main_page):
    # 从页面中找到某些东西 find_all
    a_lists = main_page.find('div', class_="TypeList").find_all('a',class_="TypeBigPics")
    n = 1
    for a in a_lists:
        # 发送请求到子页面
        href = a.get('href')
        child_page = get_page(href)

        href_split = href.split('.')
        href_next = href_split[0] + '.' + href_split[1] + '.' + href_split[2] + '_.htm'

        # 拿到script里面的文本
        num_page = child_page.find('div', class_="ImageBody").find_next("script").next
        num = num_page.split(',')[1].strip("\"")
        for i in range(1, int(num)+1):
            if i == 1:
                # 找到图片的真实路径
                src = child_page.find('div', class_="ImageBody").find('img').get('src')
                f = open("D:\my programs\myhtml\pic\\tu_%s.jpg" % n, mode="wb")  # wb表示写入的内容是非文本文件
                # 向外拿出图片的数据
                f.write(requests.get(src).content)
                print('恭喜你下载了' + str(n) + '张图片')
                n += 1  # n自增1
            else:
                href_next_split = href_next.split('.')
                # 拼接新的子页面地址
                href_next_num = href_next_split[0] + '.' + href_next_split[1] + '.' + href_next_split[2] + str(i) + '.' + href_next_split[3]
                child_page1 = get_page(href_next_num)
                src = child_page1.find('div', class_="ImageBody").find('img').get('src')
                # 创建文件
                # 发送请求到服务器，把图片保存到本地
                f = open("D:\my programs\myhtml\pic\\tu_%s.jpg" % n, mode="wb")  # wb表示写入的内容是非文本文件
                # 向外拿出图片的数据
                f.write(requests.get(src).content)
                print('恭喜你下载了' + str(n) + '张图片')
                n += 1  # n自增1


if __name__ == '__main__':
    url = 'https://www.umei.cc/meinvtupian/meinvxiezhen/'
    main_page = get_page(url)
    get_next_url(main_page)



