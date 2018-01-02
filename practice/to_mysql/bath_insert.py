# -*- coding: utf-8 -*-
# 使用脚本对数据库进行批量插入操作
import MySQLdb

conn = MySQLdb.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = 'admin',
	db = 'test'
	)

cur = conn.cursor()

# 一次插入多条记录
sqlstr = 'insert into person (id,name,mobile) values(%s,%s,%s)'
persions = [
	(11,'zhangsan',13512345671),
	(12,'lisi',13512345672),
	(13,'wangwu',13512345673),
	(14,'zhaoliu',13512345674),
	(15,'qinqi',13512345675),
]
res = cur.executemany(sqlstr,persions)
print res
cur.close()
conn.commit()
conn.close()

# cursor主要的方法主要要执行命令和接收返回值
# cursor 用于执行命令的操作
	# callproc(self,procname,args),用于执行存贮过程，接收的参数为存储过程名和参数列表，返回值是影响的行数
	# execute(self,query,args),执行单条的sql语句，接收参数为sql语句和使用的参数列表
	# executemany(self, query, args):执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
　  # nextset(self):移动到下一个结果集
# cursor用来接收返回值的方法:
　  # fetchall(self):接收全部的返回结果行.
　  # fetchmany(self, size=None):接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
　  # fetchone(self):返回一条结果行.
　  # scroll(self, value, mode='relative'):移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一行移动value条.