#coding:utf8

##################################################
file_path="a.txt"
f=open(file_path)
f.read()
f.close()

##################################################
#with上下文管理器  
file_path="a.txt"
with open(file_path) as f:
    f.read()

##################################################
file_path = "a.txt"
with open(file_path,"wb") as f:
    f.write("aaaaa")
    
##################################################
file_path = "a.txt"
f = open(file_path,"wb")
with f:
    f.write("aaaaa")

##################################################

#with的实际作用 
#运行前运行__enter__   退出时运行__exit__
class OpenContext(object):

    def __init__(self, filename, mode="r"):
        self.fp = open(filename, mode)

    def __enter__(self):
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fp.close()


file_path="a.txt"        
with OpenContext(file_path) as file_obj:
    file_obj.read()



##################################################

from contextlib import contextmanager

@contextmanager
def make_open_context(filename, mode="r"):
    fp = open(filename, mode)
    try:
        yield fp
    finally:
        fp.close()

file_path="a.txt"
with make_open_context(file_path) as file_obj:
    file_obj.read()


##################################################

from contextlib import contextmanager

@contextmanager
def html_mark():
    print("<a>")
    yield
    print("</a>")

with html_mark():
    print("jump to url")



##################################################


from contextlib import contextmanager


@contextmanager
def make_cursor(connection):
   cursor = connection.cursor() 
   try:
       cursor.execute('set autocommit=0')
       yield cursor
       connection.commit()
   except:
       connection.rollback()
   
   cursor.close()
   
      
#使用测试
from django.db import connections
connection = connections["default"]
with make_cursor(connection) as cursor:
    sql="insert into a values(999,'xxx');"
    cursor.execute(sql)
    
    #sql="insert into a values(000,'xxx');"
    sql="insert into a values('xxx');"
    cursor.execute(sql)

#模拟都成功则提交 出现任意一个失败则回滚


