# -*- coding: utf-8 -*-
# 连接mysql
import MySQLdb

# 连接数据库
conn = MySQLdb.connect(
	host='127.0.0.1',
	user='root',
	passwd='admin',
	db='test'
	)

cursor = conn.cursor()
cursor.execute('select * from user')  # 表查询
values = cursor.fetchall()
print values

cursor.close()
conn.close()