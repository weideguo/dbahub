#coding:utf8

import pymysql


conn = pymysql.connect(host='127.0.0.1', user='test', passwd='test',
                       db='test', port=1039, charset="utf8mb4")

"""
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql="select * from xxx where a=%s and b=%s"
values=(11,22)
cursor.execute(sql, values)   #参数化语句防止注入


cursor.callproc('proc_name', args=())

"""