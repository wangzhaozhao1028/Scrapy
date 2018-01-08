#coding=utf-8

import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.cn/gn')
res.encoding = 'utf-8'
# print res.text
print '-1-'
soup = BeautifulSoup(res.text,'html.parser')
print 'soup',soup
for news in soup.select('._f_con_t cm_tit'):
    print '-'*10
    print 'news',news
# print '---1---',soup.text
# header = soup.select('h1')
# 使用select找出所有id为title的元素。id前要加上#
# alink = soup.select('#title')
# print 'header',header
# 使用select找出所有class为link的元素。class前要加上.
# for link in soup.select('.link'):
#   print 'link---',link

# 使用select找出所有tag的href链接。
# alinks = soup.select('.m_f_con_t cm_tit')
# for link in alinks:
#   # print link
#   print (link['href'])



# 工具INFILIte
# http://chrome.google.com/webstore/detail/infolite/ipjbadabbpedegielkhgpiekdlmfpgal


