#!/bin/env python
#coding:utf8

from functools import wraps
from traceback import format_exc
import sys
import os

#sys.path.append(os.path.dirname(os.path.realpath(__file__))+"/../")
from mylogger import logger

def response_decoration(func):
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


