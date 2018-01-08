#coding=utf-8
"""
-lesson 2-
    下载图片
"""
import requests
from bs4 import BeautifulSoup
import os
import urllib

# 下载图片
# url = 'http:www.baidu.com/*.jpg'
# urllib.urlretrieve(url,filename='test.jpg')
# 指定图片下载路径以及命名
# url = 'https://ws1.sinaimg.cn/bmiddle/9150e4e5ly1fn0b2vayxhj2028028a9u.jpg'
# split_list = url.split('/')
# filename = split_list.pop()
# path = os.path.join('images',filename)
# urllib.urlretrieve(url,filename=path)

def  download_image(url):
    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('images',filename)
    urllib.urlretrieve(url,filename=path)

response = requests.get('https://www.doutula.com/photo/list/?page=1')
content = response.content
print content
soup = BeautifulSoup(content,'lxml')
img_list = soup.find_all('img',attrs={'class':'img-responsive lazy image_dta'})
for img in img_list:
    url = 'https:'+img['data-original']
    download_image(url)