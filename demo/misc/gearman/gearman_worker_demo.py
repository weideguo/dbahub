#coding:utf-8

import gearman 

class MyGearmanWorker(gearman.GearmanWorker): 
    def on_job_execute(self, current_job): 
        print("===================job start")
        return super(MyGearmanWorker, self).on_job_execute(current_job) 

#work的回调函数
def task_callback(gearman_worker, gearman_job): 
    #print(gearman_worker)  #g_worker 对象
    print(gearman_job.data) 
    print("-----------\n")
    return gearman_job.data 


g_worker = MyGearmanWorker(['127.0.0.1:4730']) 

#注册任务
g_worker.register_task("echo", task_callback) 

#阻塞等待 每次接收client发出的任务时调用on_job_execute一次然后再实际运行
g_worker.work() 
