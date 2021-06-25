#!/bin/env python
# -*- coding: utf-8 -*-

from threading import Thread
from multiprocessing import Queue,Process
from traceback import format_exc

share_queue = Queue()  

class ProcessControlThread(object):
    """
    多进程控制的线程并发，用于充分利用CPU
    """
    def __init__(self, target, process_num=1, thread_num=1, arg_type="single", queue_end_flag="EOF", is_join=True):
        """
        target          调用的函数
        arg_type        如何处理队列传数据到调用的函数 single list dict， single当成单个参数 list通过*list转换 dict通过**dict
        process_num     进程数 
        thread_num      单个进程的线程数
        queue_end_flag  队列的结束标识，用于结束进程
        """
        
        self.target = target
        
        self.process_num = process_num
        self.thread_num = thread_num
        
        self.queue_end_flag = queue_end_flag
        self.arg_type = arg_type
        
        if arg_type not in ["single","list","dict"]:
            raise Exception("arg_type must one of [ single list dict ]")
        
        self.process_list = []
        self.is_join = is_join
        
    
    def __single_thread_exe(self, thread_queue, thread_control_queue):
        """
        单个线程的操作
        """
        arg = thread_queue.get()
        try:
            print("begin function use [ %s ]" % arg)
            if self.arg_type == "list":
                self.target(*arg)
            elif self.arg_type == "dict":
                self.target(**arg)
            else:
                self.target(arg)
                
            print("end function use [ %s ]" % arg)
        except:
            print(format_exc())
            print("fail function use [ %s ]" % arg)
        finally:
            try:
                thread_control_queue.get(block=False) 
            except:
                pass
        
    
    def __process_thread_generate(self):
        """
        每个进程的操作 调用多线程备份
        """
        global share_queue
        try:
            from queue import Queue
        except:
            from Queue import Queue
        thread_queue = Queue(self.thread_num)              #传递信息给线程
        thread_control_queue = Queue(self.thread_num)      #线程并发控制
        
        while True:
            arg = share_queue.get()
            if arg == self.queue_end_flag:
                print("single processs exit, backgound thread contiune")
                break
            thread_control_queue.put(arg)             #超过会被阻塞
            thread_queue.put(arg)
            t = Thread(target = self.__single_thread_exe, args = (thread_queue, thread_control_queue))
            t.start()    
    
    
    def start(self):
        
        for i in range(self.process_num): 
            p = Process(target = self.__process_thread_generate, args = ())
            self.process_list.append(p)
        
        for p in self.process_list:
            p.start()
        
        if self.is_join:
            self.join()
       
    def join(self):   
        for p in self.process_list:
            p.join()
            
            
            
if __name__ == "__main__":
    import time    
    import random
    def download_file(url,b=0):
        print("---------%s %s -----------" % (url,b))
        time.sleep(random.random()*10)     
        
    
    process_num = 2
    thread_num  = 3
    
    for i in range(20):
        share_queue.put(i)
    
    for i in range(process_num): 
        share_queue.put("EOF")                           #队列尾部设置结束标识符    
    
    pct=ProcessControlThread(download_file, process_num, thread_num, arg_type="single")
    pct.start()
    
    print("----------------------------------------------------")
    
    for i in range(20):
        share_queue.put([i,2])
        
    for i in range(process_num): 
        share_queue.put("EOF")                    
        
    pct=ProcessControlThread(download_file, process_num, thread_num, arg_type="list")
    pct.start()
    
    print("----------------------------------------------------")
    
    for i in range(20):
        share_queue.put({"url":i,"b":"bbb"})
    
    for i in range(process_num): 
        share_queue.put("EOF")
    
    pct=ProcessControlThread(download_file, process_num, thread_num, arg_type="dict")
    pct.start()
    
    print("---------------------all done-------------------------------")



