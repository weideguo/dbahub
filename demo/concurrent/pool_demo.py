#coding:utf8
import time
import random
from multiprocessing import Pool


def f(n) :
    print("process begin %s" % n)
    x=int(random.random()*5)
    time.sleep(x)
    print("process end %s" % n)



def p(): 
    startTime = time.time()
    print("start :", startTime)
    pool = Pool(3)
    pool.map(f,range(5))
    pool.close()
    pool.join()    
    endTime = time.time()
    print("end :", endTime)
    print("time :", endTime - startTime)
   
   
def p2(): 
    startTime = time.time()
    print("start :", startTime)
    pool = Pool(3)
    for i in range(5):
        pool.apply_async(func=f,args=(i,))
    
    pool.close()
    pool.join()    
    endTime = time.time()
    print("end :", endTime)
    print("time :", endTime - startTime)
    

def p3():
    pool = Pool(3)
    r_list=[]
    for i in range(5):
        r = pool.apply_async(f, (i,))
        r_list.append(r)
     
    pool.close()
    pool.join()
    
    def result_check(r_list):
        for r in r_list:
            if not r.successful():
                return False
        
        return True
    if result_check(r_list):
        print("all success")
    else:
        print("error exist")
    
if __name__ == "__main__" :
    p3()

