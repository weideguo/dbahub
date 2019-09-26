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


import msgpack
var={'a':'aaa','b':'bbb'}

bit_var=msgpack.dumps(var)         #将字典类型转成二进制格式的str
r.set('a',bit_var)                 #直接以二进制存到redis

x=r.get('a')                       #
msgpack.loads(x)                   #二进制还原为字典

