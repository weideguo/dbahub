from threading import Thread
import time
from Queue import Queue

def func(n,my_queue):
	my_queue.put(1)
	print "the thread is %s"%n
	time.sleep(5)
	print "thread %s finish"%n
	my_queue.get(1)
if __name__ == "__main__":
    	my_queue=Queue(20)
	thread_list=[]
	for i in range(100):
		t = Thread(target = func, args = (i,my_queue))
		thread_list.append(t)
	for th in thread_list:
		th.start()
	for th in thread_list:
		th.join()
	print "all thread finish"
