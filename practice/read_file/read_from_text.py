#!/usr/bin/python  
#-*-coding:utf-8-*- 
# autor qinheqing
import time,json

def getInfoFromFile(url):
	file = open(url)
	lines = file.readlines()
	text = ''
	for line in lines:
		text = text + line.strip()
		
	begin = text.index('begin')
	end = text.index('end')
	slicestr = text[begin+5:end]
	print slicestr

	jsonList = json.loads(slicestr)
	return jsonList

def getNextId(t=None):
	if t is None:
		t = time.time()

	return '%s%013d' %('201712',int(t*1000))   # 当前时间的15位和uuid之后加上000作为用户的userId

print getNextId()
getInfoFromFile('source.txt')

