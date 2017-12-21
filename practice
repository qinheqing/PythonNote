# -*- coding: utf-8 -*-
import cx_Oracle

dsn = cx_Oracle.makedsn('10.186.120.152','1521','zsbz')

# 开发环境1库
conn1 = cx_Oracle.connect('verify1','rzpt_data',dsn)
conn2 = cx_Oracle.connect('verify2','rzpt_data',dsn)
conn3 = cx_Oracle.connect('verify3','rzpt_data',dsn)
conn4 = cx_Oracle.connect('verify4','rzpt_data',dsn)
conn5 = cx_Oracle.connect('verify5','rzpt_data',dsn)
conn6 = cx_Oracle.connect('verify6','rzpt_data',dsn)
conn7 = cx_Oracle.connect('verify7','rzpt_data',dsn)
conn8 = cx_Oracle.connect('verify8','rzpt_data',dsn)
conn9 = cx_Oracle.connect('verify9','rzpt_data',dsn)
conn10 = cx_Oracle.connect('verify10','rzpt_data',dsn)

# 定义获取连接对象的方法
def getConn(mobile):
	if mobile%10 == 0:
		return conn1
	elif mobile%10 == 1:
		return conn2
	elif mobile%10 == 2:
		return conn3
	elif mobile%10 == 3:
		return conn4
	elif mobile%10 == 4:
		return conn5
	elif mobile%10 == 5:
		return conn6
	elif mobile%10 == 6:
		return conn7
	elif mobile%10 == 7:
		return conn8
	elif mobile%10 == 8:
		return conn9
	elif mobile%10 == 9:
		return conn10

# 定义获取表名的方法：
def getTempTabName(userId):
	num = userId % 100 + 1
	return "T_TEMP_USER"+ str(num)

def getTempUserRef(mobile):
	num1 = mobile % 100 + 1
	return "T_REF_TMPUSER_PHONE"+ str(num1)

def executeSql(mobile,baseTempUserId):
	tabNRef = getTempUserRef(phone)
	tempRefConn = getConn(phone)
	
	tempConn = getConn(baseTempUserId)
	sql1 = 'insert into '+ tabNRef + '(MOBILE,TMPUSER_ID) values ('+str(mobile)+','+ str(baseTempUserId)+')'
	print sql1
	cursorRef = tempRefConn.cursor()
	cursorRef.execute(sql1)
	cursorRef.close()
	tempRefConn.commit()


	tabNtemp = getTempTabName(baseTempUserId)
	paramsTuple = (str(baseTempUserId),str(mobile),'123456','test33','01','452225199811025784','1','1','003')
	sql2 = 'insert into '+ tabNtemp + '(TMPUSER_ID,MOBILE,USER_PASSWORD,CUSTOMER_NAME,CARDTYPE,CARDNO,VERIFY_LEVEL,VALID_FLG,TMPUSER_SYS_SOURCE) values (:1,:2,:3,:4,:5,:6,:7,:8,:9)'
	print sql2
	cursor = tempConn.cursor()
	cursor.execute(sql2,paramsTuple)
	cursor.close()
	tempConn.commit()



# 一个手机号对应一个身份信息
phoneList = [13799881001,13799881002,13799881003,13799881004,13799881005,13799881006]
i = 1000000
for phone in phoneList:
	baseTempUserId = 2017122190000000110 + i
	executeSql(phone,baseTempUserId)
	i = i + 1
	print 'success count:',str(i)

conn1.close()
conn2.close()
conn3.close()
conn4.close()
conn5.close()
conn6.close()
conn7.close()
conn8.close()
conn9.close()
conn10.close()





