#coding:utf-8
#
# signal只适用于unix/linux系统
# kill -l 					##列出所有信号名称
# stty -a					###查看信号对应的操作
#

import signal
from functools import wraps

 
def timeout(seconds=10, error_message="timeout message"):
    def decorator(func):
        def signal_handler(signum, frame):
            print(signum)
            print(frame)
            raise Exception(error_message)
        
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, signal_handler)    #后台捕获alarm信号 
            signal.alarm(seconds)                            #多少秒后发出alarm信号 
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)                              #取消发出alarm信号
            return result
        
        return wraps(func)(wrapper)
        
    return decorator



import time
@timeout(3)
def f(n):
    time.sleep(n)
    return 1


if __name__=="__main__":
    f(10)
    f(2)

