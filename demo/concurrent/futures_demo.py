#coding:utf8
#使用futures模块实现多线程调用

import time
import random
from concurrent import futures


MAX_WORKERS = 3


def do_one(cc):
    i=random.random()*10
    print(str(cc)+" will sleep "+str(i))
    time.sleep(random.random()*10)
    print(cc)
    return cc


def do_many(cc_list):
    """多线程调度"""
    workers = min(MAX_WORKERS,len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(do_one, sorted(cc_list))
    
    return res


def do_many1(cc_list):
    """多进程调度"""
    workers = min(MAX_WORKERS,len(cc_list))
    with futures.ProcessPoolExecutor(workers) as executor:
        res = executor.map(do_one, sorted(cc_list))
    
    return res


"""
def submit(self, fn, *args, **kwargs):

def map(self, fn, *iterables, **kwargs):

def shutdown(self, wait=True)
#################

f=executor.submit(do_one,cc=123)
f.result() 
#result(self, timeout=None)  默认一直阻塞直至获取到返回值

executor.shutdown()          #等待后台调度运行结束 之后不能再进行调度
"""


if __name__ == '__main__':
    #res=do_many(["aa","bb","cc","dd"])    #返回一个迭代器generator
    res=do_many1(["aa","bb","cc","dd"])    
    
    print("concurrent result:")
    for r in res:
        print(r)