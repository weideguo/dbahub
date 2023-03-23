#!/bin/env python
# -*- coding: utf-8 -*-
#python2.7 
#mongoshake v2.4.22 

import time
import json
import requests
import subprocess

monitor_conf=[
("all.progress","http://127.0.0.1:9101/progress"),       #全量进度展示
("incr.repl","http://127.0.0.1:9100/repl"),              #增量复制的整体信息
]

loop_dict={}
for tag,url in monitor_conf:
    try:
        r=requests.get(url)
        loop_dict[tag]=json.loads(r.text)
        loop_dict["alive"]=1
    except:
        loop_dict["alive"]=0


def loop_dict_to_flat(loop_dict,flat_dict,key_prefix=""):
    for item in loop_dict.keys():
        if isinstance(loop_dict[item],dict):
            loop_dict_to_flat(loop_dict[item],flat_dict,key_prefix+item+".")
        else:
            flat_dict_key=key_prefix+item
            flat_dict[flat_dict_key]=loop_dict[item]

flat_dict={}
loop_dict_to_flat(loop_dict,flat_dict)


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
port = "9100_9101_9200"



#忽略不上传的参数
ignore_metric=[
"incr.repl.lsn.time"     ,     
"incr.repl.lsn_ckpt.time",
"incr.repl.who"          ,          
"incr.repl.tag"          ,          
"incr.repl.lsn_ack.time" , 
"incr.repl.now.time"     ,     
"incr.repl.replset"      ,      
"incr.repl.log_size_avg" ,
"incr.repl.log_size_max" ,
]

#为COUNTER的参数，默认为GAUGE
counter_metric=[

]

#指标说明
metric_comment={
"all.progress.progress":                       "全量同步进度",                                       
"all.progress.total_collection_number":        "全量同步一共有多少个表",                               
"all.progress.wait_collection_number":         "全量同步等待同步的表的数目",                                                     
"all.progress.finished_collection_number":     "全量同步已经完成同步表的数目",                          
"all.progress.processing_collection_number":   "全量同步正在同步的表的数目",                                    
"incr.repl.lsn.ts":                            "已经拉取的checkpoint位点（不一定写入）", 
"incr.repl.lsn.unix":                          "已经拉取的checkpoint位点（不一定写入）",                                       
"incr.repl.lsn_ack.ts":                        "已经成功写入目的端的checkpoint位点（已经成功写入，但是不一定持久化）", 
"incr.repl.lsn_ack.unix":                      "已经成功写入目的端的checkpoint位点（已经成功写入，但是不一定持久化）",                                        
"incr.repl.lsn_ckpt.ts":                       "已经成功持久化的checkpoint位点", 
"incr.repl.lsn_ckpt.unix":                     "已经成功持久化的checkpoint位点",                                                                                                                     
"incr.repl.logs_get":                          "拉取的oplog的个数",                                                   
"incr.repl.logs_success":                      "成功写入的oplog个数",                                                                                                 
"incr.repl.logs_repl":                         "尝试写入目的端的oplog总个数",                                                              
"incr.repl.now.unix":                          "当前时间戳",                                                                                            
"incr.repl.tps":                               "同步的oplog速率",     
"incr.repl.lsn_behind":                        "同步滞后的时间s",                              
}

#指标转换 '111'这种不需要转换
metric_trans={
'all.progress.progress': lambda x: int(x.split(".")[0]) ,                #'100.00%'
}   
                    
trans_dict={}

for k in flat_dict:
    if k in metric_trans:
        try:
            trans_dict[k]=metric_trans[k](flat_dict[k])
        except:
            pass
    else:
        trans_dict[k]=flat_dict[k]
try:
    trans_dict["incr.repl.lsn_behind"] = int(trans_dict["incr.repl.lsn.unix"]) - int(trans_dict["incr.repl.lsn_ack.unix"])
except:
    pass

metric_pre="mongoshake."
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


openfalcon_url="http://127.0.0.1:1988/v1/push"
r=requests.post(openfalcon_url,json=openfalcon_data)


