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
"""
maxPoolSize  连接池的大小
"""

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
#get_database(name=None, codec_options=None, read_preference=None, write_concern=None, read_concern=None) 
#必须要在uri中配置这里才能切换使用？否则即使加入集群这里也不用
#即使配置节点数不够也依旧对所有节点有连接

"""
PRIMARY              默认选项，从primary节点读取数据
PRIMARY_PREFERRED    优先从primary节点读取，如果没有primary节点，则从集群中可用的secondary节点读取
SECONDARY            从secondary节点读取数据，没有即报错
SECONDARY_PREFERRED  优先从secondary节点读取，如果没有可用的secondary节点，则从primary节点读取
NEAREST              从集群中可用的节点读取数据




read_concern 决定到某个读取数据时，能读到什么样的数据。
local       能读取任意数据，这个是默认设置
majority    只能读取到“成功写入到大多数节点的数据”
available
linearizable
snapshot


write_concern 表示写入后得到多少个 Secondary 的确认后再返回

w
数字      确切的个数
majority  n/2 + 1
tag set   标签组：即制定哪几个 tag 的 Secondary

j 设置为 true，表示等数据已经写入了磁盘上的 journal 后再返回，这时候即便数据库挂掉，也是能从 journal 中恢复

wtimeout 防止超时

from pymongo import WriteConcern
WriteConcern(w=None, wtimeout=None, j=None, fsync=None)
"""







