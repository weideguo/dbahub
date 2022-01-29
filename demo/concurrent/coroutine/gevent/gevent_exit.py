import time
from gevent import monkey
#monkey.patch_socket()
import gevent

x=100

def f(n):
    global x
    for i in range(n):
        x += 1
        print(gevent.getcurrent(), i, x, time.time())
        gevent.sleep(1)
    
    return 100000

def f1(n):
    global x
    for i in range(n):
        x += 2
        print(gevent.getcurrent(), i, x, time.time())
        gevent.sleep(2)
        #exit(1)
        #raise Exception("some error")
        return 1



def ft1():
    try:
        g1 = gevent.spawn(f, 6)
        g2 = gevent.spawn(f1,3)
        g2.join()
        if g1.value == 1 :
            gevent.kill(g1)

    except:
        from traceback import format_exc
        print(format_exc())
    

def ft2():
    i=0
    while i<100:
        i += 1
        print(i)
        time.sleep(1)


from threading import Thread

t1 = Thread(target = ft1)
t2 = Thread(target = ft2)
t1.start() 
t2.start()
t1.join() 
t2.join()
 