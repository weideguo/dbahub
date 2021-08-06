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



'''
#使用SCRAM-SHA-1认证时
client=MongoClient('mongodb://m_user:m_password@127.0.0.1:27017/admin')
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

#不一定需要replicaSet参数，只是有些驱动可能需要？
#mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
#mongo_replset_name="my_mongo_replset_name"
#mongo_uri="mongodb://%s:%s@%s/%s?replicaSet=%s" % (mongdb_auth[0], mongdb_auth[1], ",".join(mongo_replset), mongdb_auth_db, mongo_replset_name)


mongo_uri="mongodb://%s:%s@%s/%s" % (mongdb_auth[0], mongdb_auth[1], ",".join(mongo_replset), mongdb_auth_db)

conn = MongoClient(mongo_uri)


conn.list_database_names()


conn.close()    #只释放tcp连接，对象依旧可用，重用之后自动发起tcp连接



#python2
from urllib import quote_plus
#python3
from urllib.parse import quote_plus
#存在特殊字符时，先进行转码，再拼接uri

#存在特殊字符时，先进行转码，再拼接uri

password="!@#$%^&*"
new_password=quote_plus(password)



#读写分离
from pymongo import ReadPreference

db = conn.get_database("my_mongodb", read_preference=ReadPreference.SECONDARY_PREFERRED)


"""
PRIMARY              默认选项，从primary节点读取数据
PRIMARY_PREFERRED    优先从primary节点读取，如果没有primary节点，则从集群中可用的secondary节点读取
SECONDARY            从secondary节点读取数据，没有即报错
SECONDARY_PREFERRED  优先从secondary节点读取，如果没有可用的secondary节点，则从primary节点读取
NEAREST              从集群中可用的节点读取数据

"""
