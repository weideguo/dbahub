#cofing:utf8
"""
pip install MySQL-python==1.2.5   #暂时只支持python2  
pip install mysqlclient           #支持python3
"""
import MySQLdb

connect=MySQLdb.connect

"""
#mysql提供的连接库
import mysql.connector
connect=mysql.connector.connect
"""


"""
#pip install PyMySQL            #python3的支持 与MySQLdb兼容
#pip install cryptography       #使用caching_sha2_password格式的密码则必须安装这个包（mysql8默认使用）

import pymysql
connect = pymysql.connect
"""


#开启一个连接mysql中  show processlist 可以看到
conn=connect(host="127.0.0.1", port=1039, user="test", passwd="test",db="test1", charset="utf8",connect_timeout=10)

cursor = conn.cursor()     #可以有多个cursor 最好一个conn对应一个cursor以清晰事务模型？


sql="select * from a where id=%s and site=%s"
values=(111,"xxxx")
cursor.execute(sql, values)                      #参数化防止sql注入
cursor.fetchall() 



sql="update a set id=%s where id=%s and site=%s"
values=(111,33333333,"xxxx")
cursor.execute(sql, values)  


#cursor.execute("insert into a123123 values(101)")
sql="insert into a(id,site) values(%s,%s);"
values=(444,"xxxx")
cursor.execute(sql, values)  



conn.commit()             #对应mysql的commit
#conn.rollback()          #rollback
cursor.close()


#执行存储过程
cursor.callproc('proc_name', args=())        


######################################################################
conversions = MySQLdb.converters.conversions

#进行类型转换
#在此为表的字段类型为bit时，查询的结果进行转换，否则查询的结果为十六进制
conversions[FIELD_TYPE.BIT] = lambda data: data == b'\x01'

MySQLdb.connect(conv=conversions)


######################################################################
conn.thread_id()         #对应show processlist的id，binlog记录每个id的执行语句，由此可以确定每个连接的执行语句


