from multiprocessing import Pool
from time import sleep
import random

def f(x):
	print "%s is runing"%x
	t=int(random.random()*10)
	print "will sleep %s"%t
	sleep(t)
	print "this is %s"%x
def main():
	pool = Pool(20)
	for i in range(100):
        	result = pool.apply_async(f, (i,))
    	pool.close()
    	pool.join()
    	if result.successful():
        	print 'successful'

if __name__ == "__main__":
    main()
