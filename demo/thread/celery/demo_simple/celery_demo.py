#coding:utf8
from tasks import add
x=add.delay(5,6)    #无阻塞
x.get()             #这一步会阻塞直到调用执行结束

