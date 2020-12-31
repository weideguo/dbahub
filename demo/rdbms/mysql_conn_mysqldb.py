#cofing:utf8

import MySQLdb


#开启一个连接mysql中  show processlist 可以看到
conn=MySQLdb.connect(host="127.0.0.1", port=1039, user="test", passwd="test",db="test1", charset="utf8",connect_timeout=10)

cursor = conn.cursor()     #可以有多个cursor 最好一个conn对应一个cursor以清晰事务模型？
cursor.execute("insert into a123123 values(101)")
#cursor.execute("select * from a123123")
#cursor.fetchall()        #获取结果


conn.commit()             #对应mysql的commit
#conn.rollback()          #rollback
cursor.close()




conversions = MySQLdb.converters.conversions

#进行类型转换
#在此为表的字段类型为bit时，查询的结果进行转换，否则查询的结果为十六进制
conversions[FIELD_TYPE.BIT] = lambda data: data == b'\x01'

MySQLdb.connect(conv=conversions)