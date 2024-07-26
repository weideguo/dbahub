#coding:utf8

import time
from celery import Celery

"""
定时任务
celery -A tasks1 worker --loglevel=info
celery -A tasks1 beat --loglevel=info
"""

app = Celery("tasks1",broker="redis://:my_redis_passwd@127.0.0.1:6379/5",backend="redis://:my_redis_passwd@127.0.0.1:6379/6")

@app.task
def funcx(x,y):
    with open("x.txt","a+") as f:
        print(x,y)
        f.write(str(time.time())+"\n")

#def funcx(*args,**kwargs):
#       print(args)
#       print(kwargs)    

app.conf.beat_schedule = {  
    "my_schedule": {  
        "task": "tasks1.funcx",  
        "schedule": 10.0,  # 每n秒执行一次  
        # "schedule": crontab(minute="*/30"),  
        "args": (16, "aaa"),  
    },  
}
