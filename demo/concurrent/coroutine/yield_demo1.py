#coding:utf8


def A():
    yield 11
    print(1)
    yield 22
    print(2)
    yield 33
    print(3)
    yield 44
    print(4)


def B():
    yield "aa"
    print("a")
    yield "bb"
    print("b")
    yield "cc"
    print("c")
    yield "dd"
    print("d")


if __name__ == "__main__":
    a1=A()
    b1=B()
    ############python 2
    import sys
    if sys.version<(3.0):
        x=a1.next()         #执行第一个yield 只是第一个yield所在的行 之后的行没有执行 可以获取返回值
        x=b1.next()
        
        x=a1.next()
        x=b1.next()
        
        x=a1.next()
        x=b1.next()
        
        x=a1.next()
        x=b1.next()
    
    ###########python3
    else:
        x=next(a1)        #获取yield的返回值，但yield之后的操有不会继续执行
        x=next(b1)
            
        x=next(a1)        #函数由上一次yield之后继续执行到下一次yield，并返回
        x=next(b1)
            
        x=next(a1)
        x=next(b1)
            
        x=next(a1)
        x=next(b1)
    
    
    from inspect import getgeneratorstate
    
    getgeneratorstate(a1)   #获取函数的状态
