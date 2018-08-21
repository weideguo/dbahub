#装饰器
#coding=utf-8


def decorator1(func):
	def my_wrapper():
		
		print "bDFGER"
        	func()
    return my_wrapper	


def decorator2():
    def _decorator2(func):
        def my_wrapper():
            
            print "bDFGER"
            func()
        return my_wrapper
    return _decorator2

def decorator3(func): 
    def my_wrapper(*a,**b):
        print a
        print b
        func(*a,**b)
    return my_wrapper


def thread_control(x):
    def _thread_control(func):
        def my_wrapper(*a,**b):
            print a
            print b
            #print x	
            func(*a,**b)
        return my_wrapper
    return _thread_control

@thread_control(x='wert')		
def set_value_by_host(t):
	print t

@decorator2()
def f():
    print "a"
    print "b"

@decorator3
def f3(*a,**b):
    print a
    print b


if  __name__ == '__main__':
    print "%s"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))	
    #set_value_by_host("hello")
    f3('ref','re',rf='rtb',g='r')
    print "%s"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
