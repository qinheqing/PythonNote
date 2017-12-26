# -*- coding: utf-8 -*-
# 连接数据库指定库并创建数据库中的表
import MySQLdb

conn = MySQLdb.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'admin',
	db = 'test'
	)
# 获取数据库连接
cur = conn.cursor()

# cur.execute('create table person (id varchar(20) primary key,name varchar(20),mobile varchar(20))')  # 建表
cur.execute('insert into person (id,name,mobile) values(%s,%s,%s)',['1','liming','13712345678']) # 插入语句
print cur.rowcount

conn.commit()
cur.close()
