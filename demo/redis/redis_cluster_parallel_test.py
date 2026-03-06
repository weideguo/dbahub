#!/bin/env python
# -*- coding: utf-8 -*-
# 并发读写redis cluster测试
#
import sys
import logging
import threading
import time
from threading import Thread

from rediscluster import RedisCluster


startup_nodes = [{"host": "127.0.0.1", "port": "11101"}, 
                 {"host": "127.0.0.1", "port": "11102"},
                 {"host": "127.0.0.1", "port": "11103"},
                 {"host": "127.0.0.1", "port": "11104"},
                 {"host": "127.0.0.1", "port": "11105"},
                 {"host": "127.0.0.1", "port": "11106"},
                ]

redis_password = "my_redis_passwd"    

THREAD_NUM = 3


logger = logging.getLogger("standard")
logger.setLevel(logging.DEBUG)

format = logging.Formatter("%(asctime)s - %(message)s")     
sh = logging.StreamHandler(stream=sys.stdout)               
sh.setFormatter(format)
logger.addHandler(sh)


def operation(n):
    i = 0
    t = "thead"+str(n)
    rc = RedisCluster(startup_nodes=startup_nodes, password=redis_password, decode_responses=True)
    while True:
        try:
            key_name = "k"+str(i*THREAD_NUM+n)
            rc.set(key_name, "")
            logger.info("%s set %s success" % (t, key_name ))
            i = i+1
            time.sleep(0.1)
            rc.get(key_name)
            logger.info("%s get %s success" % (t, key_name ))
            
        except:
            rc = RedisCluster(startup_nodes=startup_nodes, password=redis_password, decode_responses=True)
            logger.warn("error on %s when operate %s , now reconnect" % (t, key_name ))
        
        time.sleep(0.1)


# 多线程操作捕获不同redis节点的状态信息
thread_list = []
for i in range(THREAD_NUM):
    t = Thread(target = operation, args = (i, ))
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print("all thread finish")

