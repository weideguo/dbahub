#!/bin/env python
#coding:utf8

from functools import wraps
from traceback import format_exc
import sys
import os

#sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../")
from mylogger import logger

def response_decoration(func):
    """
    被装饰后函数名等函数属性会发生改变，wraps能保留原有函数的名称和docstring。
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        result_dict={}
        result_str=""
        try:
            r=func(*args,**kwargs)
            result_dict["status"]=1
            result_dict["response"]=r
            result_str=str(result_dict)
        except:
            logger.error(format_exc())
            result_str=str({"status":0,"response":""})
        logger.debug(result_str)
        return result_str    
    return wrapper

"""
用于统一捕捉函数的错误以及格式化返回结果

@response_decoration
def test_func():
    ...

"""




#全局错误处理 会终止之后的语句
#如果需要跳过错误 依然需要try ... except语句 跳过则不会调用这个函数
def uncaughtExceptionHandler(type_, value, traceback):
    if type == KeyboardInterrupt:  # Ctrl + C on console
        os._exit(0)

    print("uncaught Exception:", type_, value, traceback)
    with open(os.path.join(data_launcher_path, "error.log"), "a") as fd:
        now = datetime.now()
        time_str = now.strftime("%b %d %H:%M:%S.%f")[:19]
        fd.write("%s type:%s value=%s traceback:%s" % (time_str, type_, value, traceback))
    # sys.exit(1)


sys.excepthook = uncaughtExceptionHandler


try:
    # 可能会发生异常的代码块
except :
    print("do something for execption")


try:
    # 可能会发生异常的代码块
except 异常类型 as 别名:
    print(别名)

    

try:
    # 可能会发生异常的代码块
except (异常类型1,异常类型2,异常类型3) as 别名:
    print(别名) 


def f():
    try:
        raise KeyboardInterrupt
        #print("nothing wrong")
    except:
        print("something wrong happen")     # 出现或者不出现异常都运行这里
    finally:
        print('Goodbye, world!')
    
    print(111)                               # 有正确的异常处理，则会运行这里以及之后的
    

def f():
    try:
        raise KeyboardInterrupt
    finally:
        print('Goodbye, world!')
    
    print(111)                             # 没有的异常处理，则不会运行这里以及之后的
    
    
# 内置异常类型    
Exception
RuntimeError
TypeError
NameError
OSError 
ConnectionError    
ZeroDivisionError   

   