# -*- coding:utf-8 -*-

# 记录在使用python连接数据库的主要知识要点
# 
# python标准的数据库连接接口为Python DB-API，不同的数据需要安装对应的实现模块
# 使用的流程：
# 	1. 引入API模块
# 	2. 获取与数据库的连接
# 	3. 执行sql语句和存储过程
# 	4. 关闭数据库连接
# 
# python在连接数据库时需要下载各自数据库的驱动
# 	1. cx_Oracle  --连接oracle数据库的
# 	2. MySQLdb    --连接mysql数据库的连接实现

# 一、基本用法：示例使用mysql进行连接测试

# 1. 通过驱动模块进行获取数据库连接对象
db = MySQLdb.connect('localhost','testuser','password','dataname')

# 2. 使用连接对象进行获取游标
cursor = db.cursor()

# 3. 使用游标的cursor进行执行sql
cursor.execute('select * from user')

# 4. 通过游标进行获取值
data = cursor.fetchone()

# 5. 关闭数据库
db.close()

# 二、各个数据对象详细说明
# 	数据库和 Python 语言之间的网关是connect连接对象。它包含制作数据库驱动的应用程序所需的全部组件
# 	在多线程的程序中，模块和连接可以在不同线程间共享，但是不支持游标共享。共享游标可能带来死锁风险。
# 
#   1. 连接对象connection：
#     	创建连接对象：不同的数据实现需要的参数不太一样，在oracle中
#     	>>> import cx_Oracle
#		>>> db = cx_Oracle.connect('hr', 'hrpwd', 'localhost:1521/XE')
#		>>> db1 = cx_Oracle.connect('hr/hrpwd@localhost:1521/XE')
#		>>> dsn_tns = cx_Oracle.makedsn('localhost', 1521, 'XE')
#		>>> print dsn_tns
#		(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521)))(CONNECT_DATA=(SID=XE)))
#		>>> db2 = cx_Oracle.connect('hr', 'hrpwd', dsn_tns)
#     
#     	连接对象的作用
#     	a. 创建游标    				conn.cursor()
#     	b. commit()提交事务
#     	c. rollback() 				在try...catch...异常中进行数据回滚
#
#	2. 游标对象
#		创建游标对象：connection.cursor()
#		可以使用连接对象的 cursor() 方法定义任意数量的游标。简单的程序使用一个游标就可以了，该游标可以一再地重复使用。
#		但较大的项目可能要求几个不同的游标。
#		
#		游标对象的作用：
#		a. 解析sql --Cursor.parse([statement]) 该方法可以用于在执行语句前对其进行验证
#		b. 执行sql --Cursor.execute(statement,[parameters],**keyword_parameters) --入口(参数sql,数组参数/多个单参数)
#		c. 批量sql --Cursor.executemany(statement,parameters)    -- 入参(sql,参数集合list/tuple)
#	
#	3. 获取执行的结果（可选，用于查询语句，ddl/dcl语句不反悔结果，在非查询语句上执行会报错）
#		一次获取所有的结果：
#			a. 其也是游标中的方法Cursor.fetchall(),其可以通过设置游标的arraysize属性进行底层调整请求从数据库返回的行数
#		一次获取多个结果：
#			b. 指定获取接下来的行数，Cursor.fetchmany([rows_no]), 如果未指定，默认使用arraysize
# 		一次获取一个结果
# 		
# 三、在使用数据库中需要注意的问题：
# 
# 	1. 字符集的设置，防止进行查询插入数据库的时候插入乱码数据：

# 		a. 编写的python脚本中需要加入如下几句：
		import os
		os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
		#或者os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AL32UTF8'  
# 		这样可以保证select出来的中文显示没有问题。
# 		
#  		b. 要能够正常的insert和update中文，还需要指定python源文件的字符集密码和oracle一致。
#		 -*- coding: utf-8 -*-

#   2. 客户端的NLS_LANG设置和编码转换
#   	a. 在Oracle客户端向服务器端提交SQL语句时，Oracle客户端根据NLS_LANG和数据库字符集;
#   	   对从应用程序接传送过来的字符串编码进行转换处理。如果NLS_LANG与数据库字符集相同，不作转换;
#   	
#   	b. 如果NLS_LANG与数据库字符集相同,要转换成数据库字符集并传送到服务器。服务器在接收到字符串编码之后，
#   	   对于普通的CHAR或VARCHAR2类型，直接存储;对于NCHAR或NVARCHAR2类型，服务器端将其转换为国家字符集再存储。
#   	  
#   	c. 我们通过设置当前系统的NLS_LANG，保持和数据库一致，可以让数据不用进行处理，保持保存到数据库中的数据和
#   	   当前客户端所在的字符环境一样，保持数据的一致性
#   	