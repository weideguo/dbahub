#--encoding=utf-8
'''
import pymongo
conn=pymongo.Connection("mongodb://192.168.1.1:27017")
#没有？
'''

from pymongo import MongoClient

conn=MongoClient("localhost",27017)
db=conn.test					#切换到db
col=db.myc						#切换到collection
dic={"name":"sysu","address":"ggggggg"}
col.insert(dic)                 #insert_one()  insert_many()参数为list

for item in col.find():			#可以传入字典参数进行条件查询 有find_one()
	print item
	
col.update({"name":"wwwwwwww"},{"set":{"name":"sysuuuuu"}})

col.remove({"name":"sysuuuuu"})


is_primary

'''
#使用SCRAM-SHA-1认证时
client=pymongo.MongoClient('mongodb://m_user:m_password@127.0.0.1:27020/admin')
client.admin.command('ismaster')
'''
'''
MongoReplicaSetClient
'''


