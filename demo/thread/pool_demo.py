#coding:utf8
import time
from multiprocessing import Pool


def run(n) :
    print("process begin %s" % n)
    time.sleep(2)
    print("process end %s" % n)


def p(): 
    startTime = time.time()
    print("start :", startTime)
    pool = Pool(3)
    pool.map(run,[1,2,3,4,5])
    pool.close()
    pool.join()    
    endTime = time.time()
    print("end :", endTime)
    print("time :", endTime - startTime)
   
   
def p2(): 
    startTime = time.time()
    print("start :", startTime)
    pool = Pool(3)
    for i in [1,2,3,4,5]:
        pool.apply_async(func=run,args=(i,))
    
    pool.close()
    pool.join()    
    endTime = time.time()
    print("end :", endTime)
    print("time :", endTime - startTime)
        
    
if __name__ == "__main__" :
    p2()
