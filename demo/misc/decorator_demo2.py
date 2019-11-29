#coding 
a={}
def route(url):
    def wrapper(func):
        #a.setdefault('GET',{})['/']="hello"     #当使用为装饰器的时候即调用，在主函数调用前参数已经被赋值
        a.setdefault('GET',{})[url]=func
        return func
    return wrapper


@route('/ssss')
def b():
    print("hello")
	

#由此可以实现路由的设置
print(a)	
		
					