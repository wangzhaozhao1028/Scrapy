#coding=utf-8
"""
 多线程爬取表情包
 tools:
    requests
    beautifulsoup4,解析图片
"""
import requests
from bs4 import BeautifulSoup

# 全局变量
# PAGE_URL_LIST = []
# BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='


# for x in range(1,12):
#     url = BASE_PAGE_URL + str(x)
    # print url

# def range(start=None, stop=None, steep=None):
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

response = requests.get('https://www.doutula.com/photo/list/?page=12')
content = response.content
print content
soup = BeautifulSoup(content,'lxml')

# class = 'img-responsize lazy image_dta' 标签特征
img_list = soup.find_all('img',attrs={'class':'img-responsive lazy image_dta'})
print '---1--',img_list
for img in img_list:
    print img
    print '-'*30