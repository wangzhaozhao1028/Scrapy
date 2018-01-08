#coding=utf-8
"""
-lesson 5-
 结合生产者,消费者模型,爬取表情包,4个线程作为消费者,
 访问全局变量就要上所,解锁
"""
from bs4 import BeautifulSoup
import threading
import requests
import time
import random

# 页面url列表
PAGE_URL_LIST = []
# 表情包url列表
FACE_URL_LIST =[]
BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
gLock = threading.Lock()
for x in range(1,1266):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

def procuder():
    while True:
        gLock.acquire()
        if len(PAGE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PAGE_URL_LIST.pop()
            gLock.release()
            response = requests.get(page_url)
            content = response.content
            soup = BeautifulSoup(content, 'lxml')
            img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            #上锁
            gLock.acquire()
            for img in img_list:
                src = img['data-original']
                if not src.startswith('http'):
                    src = 'https:' + img['data-original']
                FACE_URL_LIST.append(url)
            #解锁
            gLock.release()

def customer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            face_url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = face_url.split('/')
            filename = split_list.pop()
            path = os.path.join('images', filename)
            urllib.urlretrieve(url, filename=path)


def main():
    for x in range(4):
        th = threading.Thread(target=procuder)
        th.start()


    for x in range(4):
        th = threading.Thread(target=customer)
        th.start()


if __name__ == '__main__':
    main()