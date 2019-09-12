from multiprocessing import Process
from threading import Thread
from Queue import Queue
import time

def func(n,my_queue):
	my_queue.put(1)
	print "the process is %s"%n
	time.sleep(5)
	print "process %s finish"%n
	my_queue.get(1)

if __name__ == "__main__":
	my_queue=Queue(20)
	process_list=[]
	for i in range(100):
		p = Thread(target = func, args = (i,my_queue,))
		process_list.append(p)
	for pro in process_list:
		pro.start()
	for pro in process_list:
		pro.join()
	print "all process finish"
