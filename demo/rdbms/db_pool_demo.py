#coding:utf8
"""
DB连接池
"""
#PooledDB       application frequently starts and ends threads 可用于控制连接数
#PersistentDB   application keeps a constant number of threads which frequently use the database 只用于自动重连，连接数不能控制
#import pymysql as mydb
import pgdb as mydb # import used DB-API 2 module
from DBUtils.PooledDB import PooledDB             
pool = PooledDB(mydb,  db='mydb')  #有更多参数可以设置


import pgdb as mydb # import used DB-API 2 module
from DBUtils.PersistentDB import PersistentDB     #1.0+
#from dbutils.persistent_db import PersistentDB   #2.0+
persist = PersistentDB(mydb, db='mydb')


#connection may be shared with other threads by defaul
conn = pool.connection(shareable=False)                       #如果发生cur执行出现错误则需要重新调用该操作？ 由此创建tcp连接
conn = pool.dedicated_connection()


cur = conn.cursor()
cur.execute(...)
res = cur.fetchone()
cur.close()    # or del cur
conn.close()  # or del db        不会关闭实际tcp连接

#PooledDB
#逻辑释放，其他线程可以复用tcp连接


