import threading

# 创建全局ThreadLocal对象 线程之前的的local值不互相影响
local_school = threading.local()


import time
import random


def process_student(name):
    #也可以使用一个对象赋值
    local_school.name = name  
    do_task()


def do_task():
    x=round(random.random()*3)
    time.sleep(x)
    print(threading.current_thread().name, local_school.name, str(x))



if __name__ == '__main__':
    t1 = threading.Thread(target=process_student, args=("aaaa",), name="T1")
    t2 = threading.Thread(target=process_student, args=("bbbb",), name="T2")
    t1.start()
    t2.start()
    