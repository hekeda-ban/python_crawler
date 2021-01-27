# -*--coding:utf-8 -*--
# @Time : 2021/1/27 15:21
# @Author : BAY
# @File : 拉勾网.py
# @Software : PyCharm

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
# 创建浏览器
web = Chrome()
# 打开浏览器，请求到拉钩
web.get('https://lagou.com')

# 找到❌号,点击
web.find_element_by_xpath('//*[@id="cboxClose"]').click()
# 来一个延迟
time.sleep(2)
# 找到文本框，输入python，输入回车
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)
time.sleep(2)
# 点击给也不要
web.find_element_by_xpath('/html/body/div[8]/div/div[2]').click()
# web.find_elements_by_xpath('//*[@id="s_position_list"]/ul/li[1]/div[1]/div[1]/div[1]/a/h3')
a_lists = web.find_elements_by_class_name('position_link')
n = 1
for a in a_lists:
    # 找到h3并点击
    a.find_element_by_tag_name('h3').click()
    # 窗口的转换
    web.switch_to.window(web.window_handles[-1])  # 跳转到倒数第一个窗口
    # 拿到招聘信息
    text = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text  # 拿文本
    # 把招聘信息保存在文件中
    f = open('D:\my programs\myhtml\\recruitmentinformation\需求_%s.txt' % n, mode="w")
    f.write(text)
    f.close()

    # 关闭窗口
    web.close()
    # 调整窗口到最开始的那个页面
    web.switch_to.window(web.window_handles[0])
    time.sleep(1)

    n += 1



