#coding 
a={}
def route(url):
    def wrapper(func):
        a.setdefault('GET',{})['/']="hello"     #当使用为装饰器的时候即调用，在主函数调用前参数已经被赋值
        return func
    return wrapper

@route('/ssss')
def b():
    print "hello"
	
	
		
		
def dec(dec_a,dec_b):            #接收装饰器的参数
    def w1(func_name):           #接收主函数名
        def w2(*a,**b):          #接收主函数的参数    x("xxxx",b="ssss")
            print dec_a,dec_b						  
            print a									#('xxxx',)
            print b 								#{'b':"ssss"}
            func_name(a,b)
        return w2
    return w1
	
@dec("drfhlkhlk","kajdfkjkj")
def x(a,b):
	print "xxxxx"
			
		
		
		
		
		
		