#coding:utf8

"""
在同一级目录执行，以启动celery
celery -A tasks worker --loglevel=info
"""

from tasks import add
x=add.delay(5,6)    #无阻塞
x.get()             #这一步会阻塞直到调用执行结束

