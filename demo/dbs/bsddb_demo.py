#/bin/env python3
"""
berkeleydb 嵌入kv数据库
https://www.linuxfromscratch.org/blfs/view/svn/server/db.html  安装berkeleydb
pip install berkeleydb                                         安装python模块
"""
#import bsddb
#在python2中是标准库

import berkeleydb as bsddb

db = bsddb.btopen('demo.db', 'c')
"""
'r' (read only), 
'w' (read-write), 
'c' (read-write - create if necessary; the default) 
'n' (read-write - truncate to zero length)

hashopen Open the hash format file
btopen   Open the btree format file
rnopen   Open a DB record format file 
"""
db[b'key1'] = b'value1'
db[b'key2'] = b'value2'
db.get(b'key1')
db.keys()
db.first()
db.next()
db.last()
db.set_location(b'key1')
db.previous()

db.pop(b'key1')   # 获取值并删除key

db.sync()

