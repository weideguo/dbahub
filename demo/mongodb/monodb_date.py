#!/bin/env python
# -*- coding: utf-8 -*-
# mongodb 对时间的处理

from pymongo import MongoClient
from pymongo import ReadPreference

mongo_replset=[
"127.0.0.1:27017",
]

dbname="dba_opt"

mongdb_auth_db="admin"

mongo_uri="mongodb://%s/%s" % (",".join(mongo_replset), mongdb_auth_db)

conn = MongoClient(mongo_uri,connectTimeoutMS=5000)

db = conn.get_database(dbname)

# mongodb都以utc+0存储，即从mongodb获取到的时间都是utc+0的时间

########方案一 不设置时区信息，直接把当前的时间当成utc+0存储于数据库，好处是不用转换，但业务涉及多个时区可能会导致混乱
dt=datetime.strptime("2020-08-11 10:38:54","%Y-%m-%d %H:%M:%S")

db.db_history.insert({"d": dt})

for i in db.db_history.find():
    _datetime=i["d"]
    print(_datetime.strftime('%Y-%m-%d %H:%M:%S'))
    



#########方案二 当前时间设置时区信息，读取时需要按照utc+0转换成本地时间
import pytz
from datetime import datetime

tz=pytz.timezone("Asia/Shanghai")

dt=datetime.strptime("2020-08-11 10:38:54", "%Y-%m-%d %H:%M:%S").replace(tzinfo=tz)         # 设置时区信息

db.db_history.insert({"d": dt})                                                             # pymongo将根据时间的时区转换成utc0的时间传递给mongodb


for i in db.db_history.find():
    utc_now=i["d"]              
    utc_now=utc_now.replace(tzinfo=pytz.timezone("UTC"))                                    # 获取到的时间是utc+0时间，因此设置时区
    local_datetime=utc_now.astimezone(tz)                                                   # 转换成本地的时区
    print(local_datetime.strftime('%Y-%m-%d %H:%M:%S'))
    



