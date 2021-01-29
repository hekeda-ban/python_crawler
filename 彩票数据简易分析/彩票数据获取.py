# -*--coding:utf-8 -*--
# @Time : 2021/1/28 18:40
# @Author : BAY
# @File : 彩票数据获取.py
# @Software : PyCharm
import requests
from lxml import etree
import pandas as pd

url = 'http://datachart.500.com/ssq/history/history.shtml'
resp = requests.get(url)
resp.encoding = 'gb2312'
# print(resp.text)
tree = etree.HTML(resp.text)

tds = tree.xpath('//*[@id="tdata"]/tr[@class="t_tr1"]/td/text()')

qi_hao = tds[0::16]
red_1 = tds[1::16]
red_2 = tds[2::16]
red_3 = tds[3::16]
red_4 = tds[4::16]
red_5 = tds[5::16]
red_6 = tds[6::16]
blue = tds[7::16]
bonus = tds[9::16]
yi_zhu_shu = tds[10::16]
yi_bonus = tds[11::16]
er_zhu_shu = tds[12::16]
er_bonus = tds[13::16]
total_bonus = tds[14::16]
kai_jiang = tds[15::16]
data = pd.DataFrame({'期号':qi_hao, '红球号码1':red_1, '红球号码2':red_2,
                     '红球号码3':red_3, '红球号码4':red_4, '红球号码5':red_5,
                     '红球号码6':red_6, '蓝球':blue, '奖池奖金':bonus,
                     '一等奖注数':yi_zhu_shu,'一等奖奖金':yi_bonus,
                     '二等奖注数':er_zhu_shu, '二等奖奖金':er_bonus,
                     '总投注额':total_bonus, '开奖日期':kai_jiang})
data.to_csv("D:\my programs\myhtml\data.csv", index=False, sep=',')






