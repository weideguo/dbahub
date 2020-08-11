#coding:utf-8

a="aaa"

def f():
    global a    #必须使用关键字global才能指定为全局参数，否则在函数内的修改不影响外部值
    a="bbbb"    #也可以为对象 字典等
    print(a)
    

if __name__=="__main__":
    print(a)
    f()
    print(a)



