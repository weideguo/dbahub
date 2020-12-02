#coding:utf8
#进程之前默认不共享变量
#可以通过以下方式声明共享变量


import multiprocessing


#三种进程间数据共享方式

#shared memory
#共享内存共享对象
num=multiprocessing.Value("d",10.0) #c_double
#num=multiprocessing.Value("c")     #c_char
#num=multiprocessing.Value("i")     #c_int
arr=multiprocessing.Array("i",[1,2,3,4,5])


#inheritance       
#父进程创建对象
#子进程自动继承了父进程当中的对象，即为不需要通过函数方法传给子进程
queue=multiprocessing.Queue()
lock=multiprocessing.Lock()
#Pipe, Queue, JoinableQueue, 同步对象(Semaphore, Lock, RLock, Condition, Event等)


#server process 
#一个进程负责创建对象，而其他进程连接到该进程，通过代理对象操作服务器进程当中的对象
mydict=multiprocessing.Manager().dict()   
mylist=multiprocessing.Manager().list(range(5))
v=multiprocessing.Manager().Value("aa","ss")
#multiprocessing.managers.SyncManager
#__init__(self, address=None, authkey=None, serializer='pickle')




#x=lock
#x=num
x=arr
#x=mydict
#x=mylist
#x=queue
#x={}  #默认变量不共享

def func(x):  
    #lock
    #x.acquire()
    #lock.acquire()       #继承方式共享可以不必通过函数参数传入
    
    #Value各值类型需要匹配声明时的类型
    #x.value=100  #x.value="sss"  #不能为非float
    
    #Array类型
    x[0]=0
    
    #dict 类型
    #x['a']="aaa"
    
    #list类型
    #x=[1,2,3]   #不能以此覆盖
    #x.append("xx")    
    
    #multiprocessing.Queue
    #x.put(1)


p=multiprocessing.Process(target=func,args=(x,))  
p.start()


#子进程的操作不会改变默认变量
print(x)
    

