#coding:utf8
"""
DB连接池
"""
#PooledDB       application frequently starts and ends threads
#PersistentDB   application keeps a constant number of threads which frequently use the database
#import pymysql
import pgdb  # import used DB-API 2 module
from DBUtils.PooledDB import PooledDB
pool = PooledDB(pgdb, 5, database='mydb')  #有更多参数可以设置


import pgdb  # import used DB-API 2 module
from DBUtils.PersistentDB import PersistentDB
persist = PersistentDB(pgdb, 1000, database='mydb')


#connection may be shared with other threads by defaul
db = pool.connection(shareable=False)
db = pool.dedicated_connection()


db = pool.connection()
cur = db.cursor()
cur.execute(...)
res = cur.fetchone()
cur.close()  # or del cur
db.close()  # or del db
