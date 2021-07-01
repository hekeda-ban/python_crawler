# _*__coding:utf-8 _*__
# @Time :2021/6/3 19:33
# @Author :bay
# @File download_doc_files.py.py
# @Software : PyCharm
# doc文件下载
import requests
from lxml import etree
from urllib import parse
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.tc260.org.cn/front/bzzqyjList.html?postType=&start=370&length=10'
text = requests.get(url).text
tree = etree.HTML(text)
a_hrefs = tree.xpath('//ul[@class="list-group"]/li/a/@href')
opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=opt)
for a_href in a_hrefs:
    time.sleep(1)
    new_url = parse.urljoin(url, a_href)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    }
    content = requests.get(new_url,).text
    # print(content)
    driver.get(new_url)
    driver.implicitly_wait(10)
    doc_name1 = driver.find_element_by_xpath('//div[@class="col-md-10 "]/span[@id="APP_1"]/a').text
    # print(doc_name1)
    new_link1 = driver.find_element_by_xpath('//div[@class="col-md-10 "]/span[@id="APP_1"]/a').get_attribute('href')
    # print(new_link1)
    down1 = requests.get(new_link1).content
    with open(doc_name1, 'wb') as f:
        f.write(down1)
    print("文件1", doc_name1, "下载成功")
    doc_name2 = driver.find_element_by_xpath('//div[@class="col-md-10 "]/span[@id="APP_3"]/a').text
    new_link2 = driver.find_element_by_xpath('//div[@class="col-md-10 "]/span[@id="APP_3"]/a').get_attribute('href')
    down2 = requests.get(new_link2).content
    with open(doc_name2, 'wb') as f:
        f.write(down2)
    print("文件2", doc_name2, "下载成功")

