#--encoding=utf-8


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
client=pymongo.MongoClient('mongodb://m_user:m_password@127.0.0.1:27017/admin')
client.admin.command('ismaster')
'''


'''
MongoReplicaSetClient
'''
mongo_replset=[
"127.0.0.1:27017",
"127.0.0.2:27017",
"127.0.0.3:27017"
]


mongdb_auth=("my_mongo_user","my_mongo_password")

mongdb_auth_db="admin"
mongo_replset_name="my_mongo_replset_name"

mongo_uri="mongodb://%s:%s@%s/%s?replicaSet=%s" % (mongdb_auth[0], mongdb_auth[1], ",".join(mongo_replset), mongdb_auth_db, mongo_replset_name)


conn = pymongo.MongoClient(mongo_uri)

