#coding=utf-8
from urllib import parse
import requests
from lxml import etree
import time
import random
import codecs



def get_html(url):
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 '}
	html = requests.get(url, headers=header)
	html.encoding = 'gb2312'
	html = html.text
	return html


def get_quote(data):
	idiom = parse.quote(data,encoding = 'gb2312')
	return idiom


def check(q):
	# value = get_quote(q)
	url = 'http://chengyu.t086.com/chaxun.php?q={}&t=ChengYu'.format(get_quote(q))
	datas = etree.HTML(get_html(url)).xpath('//tr/td/a/font/text()')
	# print( datas)
	try:
		if datas[0]:
			return True
	except:
		return 


def get_idiom(q):
	url = 'http://chengyu.t086.com/chaxun.php?q1={}&q2=&q3=&q4='.format(get_quote(q))
	datas = etree.HTML(get_html(url)).xpath('//tr/td/a/text()')
	if len(datas)==1:
		answer = q+datas[0]
		print("*"*10)
		print(answer)
		return answer
	elif len(datas)>1:
		answer = q+datas[random.randint(0,len(datas)-1)]
		print("-"*20)
		print(answer)
		return answer
	else:
		return False



def main():
	entry = input("input chengyu!")
	# entry = '三心二意'
	idiom_list = []
	if check(entry):
		k = 1
		while 1:
			if entry not in idiom_list:
				idiom_list.append(entry)
			else:
				print("used! you lose!")
				break
			q4 = entry[-1]
			result = get_idiom(q4)
			if result:
				if k==1:
					print("begin")
				else:
					print('you answer right %s'%k)
				print('let`s thinking',end = '',flush=1)
				for i in range(int(round(random.random()*10))):
					time.sleep(0.5)
					print(".",end = '',flush=1)
				print("\n, get:",result)
				k+=1
			else:
				print('you are very good ,I am lose')
				break
			time_now = time.time()
			entry2 = input("turn you")
			time2 = time.time()
			time3 = time2 - time_now
			try:
				if entry2[0] == result[-1]:
					if check(entry2):
						entry = entry2
					else:
						print("your wrong idiom! your lose!")
						break
				else:
					print("first word must same")
					break
			except:
				print("your answer is not idiom! you lose")
				break

			if time3>10:
				print("pasted %s s,too slow"%round(time3))
			else:
				print("it used %s s,wOoO!"%round(time3))



	else:
		print("bushi chengyu,again!")


if __name__ == '__main__':
	main()
