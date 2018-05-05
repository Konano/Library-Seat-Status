#! python3
# -*- coding:utf-8 -*-

import time
import codecs
import os
from selenium import webdriver
from pyvirtualdisplay import Display


def get_date(str):

	st = str.index('<span id="Label_time" class="time">')+35
	ed = str.index(' ', st)
	return str[st:ed:];

def output(Data):

	file_object = open('./record/'+get_date(driver.page_source)+'.txt', 'a', encoding = 'utf-8') # 使用时需修改路径

	for i in Data:
		file_object.write(str(i)+'\t')

	file_object.write('\n')

	file_object.close()

def get_rest(str, lable):

	st = str.index('20.0pt">', str.index('20.0pt">', str.index(lable)+1)+1)+8
	ed = str.index('</td>', st)
	return int(str[st:ed:])

def get_time(str):

	st = str.index('<span id="Label_time" class="time">')+35
	st = str.index(' ', st)+1
	ed = str.index('</span>', st)
	return str[st:ed:];

def get_data():

	# print ('Now Time: '+get_time(driver.page_source))

	G = get_rest(driver.page_source, 'G层自修室')
	F2A = get_rest(driver.page_source, 'F2A区')
	F2C = get_rest(driver.page_source, 'F2C区')
	F3A = get_rest(driver.page_source, 'F3A区')
	F3B = get_rest(driver.page_source, 'F3B区')
	F3C = get_rest(driver.page_source, 'F3C区')
	F4C = get_rest(driver.page_source, 'F4C区')
	ALL = get_rest(driver.page_source, 'ALL')

	Data = [get_time(driver.page_source), G, F2A, F2C, F3A, F3B, F3C, F4C, ALL]

	output(Data)

if __name__ == '__main__':

	display = Display(visible=0, size=(800,600))
	display.start()
	driver = webdriver.Chrome("chromedriver")
	driver.get("http://seat.lib.tsinghua.edu.cn/roomshow/")

	while True:
		get_data()
		time.sleep(60)

	driver.quit()
	display.stop()
