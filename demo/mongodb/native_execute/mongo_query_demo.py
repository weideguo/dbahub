# -*- coding: UTF-8 -*-
import mongo_patch
                    
mongo_patch.p_coll           = "persons"             #  
mongo_patch.p_spec           = {"name": 8}      #   
mongo_patch.p_projection     = {"title": 1}     #    
mongo_patch.p_skip           = None             #
mongo_patch.p_limit          = 1                #
mongo_patch.p_batch_size     = None             #
mongo_patch.p_options        = None             #
mongo_patch.p_read_concern   = None             #
mongo_patch.p_collation      = None             #
mongo_patch.p_session        = None             #
mongo_patch.p_allow_disk_use = None             #

mongo_patch.apply_patch()



from pymongo import MongoClient

mongo_replset=[
"127.0.0.1:27017",
]

mongdb_auth=("root","root")

mongdb_auth_db="admin"

mongo_uri="mongodb://%s:%s@%s/%s" % (mongdb_auth[0], mongdb_auth[1], ",".join(mongo_replset), mongdb_auth_db)

conn = MongoClient(mongo_uri)

conn.list_database_names()

db=conn.mytest					

 
for item in db.personsx.find():			
    print(item)


