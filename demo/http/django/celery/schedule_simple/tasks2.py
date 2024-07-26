#coding:utf8

import time
from celery import Celery
from celery.task import periodic_task
from celery.schedules import crontab


"""
定时任务
celery -A tasks2 worker --loglevel=info
celery -A tasks2 beat --loglevel=info
"""

app = Celery("tasks2",broker="redis://:my_redis_passwd@127.0.0.1:6379/5",backend="redis://:my_redis_passwd@127.0.0.1:6379/6")

#(minute='*', hour='*', day_of_week='*', day_of_month='*', month_of_year='*', **kwargs)
@periodic_task(run_every=crontab(minute="*", hour="*", day_of_week="*"))
def funcx():
    with open("x.txt","a+") as f:
        f.write(str(time.time())+"\n")
    

