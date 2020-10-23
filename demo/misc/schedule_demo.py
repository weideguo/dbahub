#coding:utf8
#pip install schedule==0.4.3
#计划调度

import time
import threading

import schedule


def job():
    """实际执行的操作"""
    print("I'm running on thread %s" % threading.current_thread())
    

def run_threaded(job_func):
    """自行实现并发，如果不调用线程/进程则相当于普通带参数的普通方法"""
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


schedule.every(10).seconds.do(run_threaded, job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
    """
    相当于将job加入到队列，然后每间隔一段时间（通过time.sleep控制）检查job的状态，符合则运行
    """ 

"""

def job():
    print("I'm working...")
    
    #当只想运行一次时
    return schedule.CancelJob


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
"""
    
   