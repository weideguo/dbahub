#!/bin/env python
import redis

r=redis.Redis(host='127.0.0.1',port=6379,db=0)
#r=redis.StrictRedis(host='127.0.0.1',port=6379)
r.set('name','name_content')
value=r.get('name')


r=redis.StrictRedis(host='127.0.0.1',port=6379,password='redis_password',db=0)
pipe=r.pipeline()
pipe.hset("key_name_test001","field_name4","field_value4")
pipe.hset("key_name_test001","field_name5","field_value5")
pipe.hset("key_name_test001","field_name6","field_value6")
pipe.execute()
