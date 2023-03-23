#!/bin/env python
# -*- coding: utf-8 -*-
# python2.7
import pymongo
import bson
import time
import subprocess
import requests

#这个信息泄露 尽量不要使用
mongodb_url="mongodb://admin:my_passwd@127.0.0.1:27017/admin"

try:
    client=pymongo.MongoClient(mongodb_url , serverSelectionTimeoutMS=3000)
    #client.database_names()
    loop_dict=client.admin.command("serverStatus")
    loop_dict["alive"]=1
except:
    loop_dict["alive"]=0

flat_dict={}
def loop_dict_to_flat(loop_dict,flat_dict,key_prefix=""):
    for item in loop_dict.keys():
        if isinstance(loop_dict[item],dict):
            loop_dict_to_flat(loop_dict[item],flat_dict,key_prefix+item+".")
        else:
            flat_dict_key=key_prefix+item
            flat_dict[flat_dict_key]=loop_dict[item]

loop_dict_to_flat(loop_dict,flat_dict)
trans_dict={}            
for k in flat_dict.keys():  
    if type(flat_dict[k]) in [int,float,long,bool,bson.int64.Int64]:
        trans_dict[k]=int(flat_dict[k])
            


##########################################openfalcon数据转换#######################################################
#读取配置文件获取 endpoint
cmd= "cat /usr/local/XXXXyw/agent/cfg.json | grep hostname"
x=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout.read()
endpoint=x.split("\"")[3]

if not endpoint:
    raise Exception("get endpoint error, check cmd [%s]" % cmd)

timestamp = int(time.time())

#计算间隔 需要跟脚本调度的间隔一致
step=300

#占用的端口号
port = str(loop_dict["repl"]["me"].split(":")[-1])

#忽略不上传的参数
ignore_metric=[

]

#为COUNTER的参数，默认为GAUGE
counter_metric=[
"opcounters.command" ,
"opcounters.delete"  ,
"opcounters.getmore" ,
"opcounters.insert"  ,
"opcounters.query"   ,
"opcounters.update"  ,
"network.bytesIn"    ,
"network.bytesOut"   ,
"wiredTiger.cache.bytes dirty in the cache cumulative" ,
]

#指标说明
metric_comment={
"repl.ismaster":"是否为主",
"mem.resident": "常驻内存单位M",
"mem.virtual": "虚拟内存单位M" ,
}
metric_pre="mongodb."
openfalcon_data=[]
for k in trans_dict:
    counterType= "GAUGE"
    tags="port=%s" % port 
    
    if k in ignore_metric:
        continue
    
    if k in counter_metric:
        counterType="COUNTER"
    
    if k in metric_comment:
        tags=tags+",comment="+metric_comment[k]
    
    
    d={ "endpoint": endpoint,
        "tags": tags,             
        "timestamp": timestamp,
        "metric": metric_pre+str(k),
        "value": trans_dict[k],
        "counterType": counterType,
        "step": step}
    openfalcon_data.append(d)


#counterType: 是Open Falcon定义的数据类型，取值只能是COUNTER或者GAUGE二选一，前者表示该数据采集项为计时器类型，后者表示其为原值 (注意大小写)
#  - GAUGE：即用户上传什么样的值，就原封不动的存储
#  - COUNTER：指标在存储和展现的时候，会被计算为speed，即（当前值 - 上次值）/ 时间间隔


openfalcon_url="http://127.0.0.1:1988/v1/push"
r=requests.post(openfalcon_url,json=openfalcon_data)
#r.text
