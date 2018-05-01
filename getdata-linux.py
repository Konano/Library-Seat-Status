#! python3
# -*- coding:utf-8 -*-

import time,platform
import codecs
import os
from selenium import webdriver
from pyvirtualdisplay import Display


def output(Data):

	file_object = open('record.txt', 'a', encoding = 'utf-8') # 使用时需修改路径

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
	ed = str.index('</span>', st)
	return str[st:ed:];

def get_data():

	print ('Now Time: '+get_time(driver.page_source))

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

def funzione():

	display = Display(visible=0, size=(800,600))
	display.start()
	driver = webdriver.Chrome("chromedriver")
	driver.get("http://seat.lib.tsinghua.edu.cn/roomshow/")

	while True:
		get_data()
		time.sleep(60)

	driver.quit()
	display.stop()

def createDaemon():
	# fork进程
	try:
		if os.fork() > 0: os._exit(0)
	except OSError, error:
		print 'fork #1 failed: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)
	os.chdir('/')
	os.setsid()
	os.umask(0)
	try:
		pid = os.fork()
		if pid > 0:
			print 'Daemon PID %d' % pid
			os._exit(0)
	except OSError, error:
		print 'fork #2 failed: %d (%s)' % (error.errno, error.strerror)
		os._exit(1)
	# 重定向标准IO
	sys.stdout.flush()
	sys.stderr.flush()
	si = file("/dev/null", 'r')
	so = file("/dev/null", 'a+')
	se = file("/dev/null", 'a+', 0)
	os.dup2(si.fileno(), sys.stdin.fileno())
	os.dup2(so.fileno(), sys.stdout.fileno())
	os.dup2(se.fileno(), sys.stderr.fileno())

	# 在子进程中执行代码
	funzione() # function demo

if __name__ == '__main__':
	if platform.system() == "Linux":
		createDaemon()
	else:
		os._exit(0)