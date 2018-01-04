# -*-coding:utf-8-*-

import urllib2

response = urllib2.urlopen("https://www.zhihu.com/collection/28114256")
print response.read()