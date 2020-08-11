#coding:utf-8

from gearman import GearmanClient 

#可以为多个gearman，会自动负载？
g_client = GearmanClient(["127.0.0.1:4730"]) 


#通过任务名向work发出执行消息 默认一直阻塞直至work执行后返回
#submit_job(self, task, data, unique=None, priority=None, background=False, wait_until_complete=True, max_retries=0, poll_timeout=None)
r = g_client.submit_job("echo", "test gearman") 
 
print(r.result) 
