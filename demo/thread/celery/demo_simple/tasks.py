#coding:utf8

import time
from celery import Celery

"""
broker/backend 可以使用rabbitMQ
"""

app = Celery("tasks",broker="redis://:my_passwd@127.0.0.1:6379/5",backend="redis://:my_passwd@127.0.0.1:6379/6")

@app.task
def add(x,y):
    time.sleep(10)
    return x+y
    
