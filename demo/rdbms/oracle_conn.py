#coding:utf8

import cx_Oracle
"""
需要先安装两个包
Oracle Instant Client
cx_Oracle
"""

conn=cx_Oracle.connect("username","password","10.0.0.1:1521/ORCL")
cursor=conn.cursor()
 
sql="select * from a where"
values=()
cursor.execute(sql, values)               
cursor.fetchall() 
 
cursor.close()
conn.commit()
conn.close()
