from multiprocessing import Pool
import time
import random

def f(x):
    print("%s is runing"% x)
    t=int(random.random()*10)
    time.sleep(t)
    print("%s is end"%x)


def p():
    pool = Pool(2)
    for i in range(10):
        result = pool.apply_async(f, (i,))
    pool.close()
    pool.join()
    if result.successful():
        print('successful')

if __name__ == "__main__":
    p()
