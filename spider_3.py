#coding=utf-8
"""
-lesson 3-

"""
import requests
from bs4 import BeautifulSoup
import os
import urllib

PAGE_URL_LIST = []
BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
for x in range(1,1266):
    url = BASE_PAGE_URL + str(x)
    PAGE_URL_LIST.append(url)

def  download_image(url):
    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('images',filename)
    urllib.urlretrieve(url,filename=path)

def get_page(page_url):
    response = requests.get(page_url)
    content = response.content
    print content
    soup = BeautifulSoup(content,'lxml')
    img_list = soup.find_all('img',attrs={'class':'img-responsive lazy image_dta'})
    for img in img_list:
        url = 'https:'+img['data-original']
        download_image(url)

def main():
    for page_url in PAGE_URL_LIST:
        get_page(page_url)


if __name__ == '__main__':
    main()