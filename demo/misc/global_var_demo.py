#coding:utf-8

a="aaa"

def f():
    global a    #必须使用关键字global才能指定为全局参数，否则在函数内的修改不影响外部值
    a="bbbb"    #也可以为对象 字典等
    print(a)




a1={}

def f1():
    #a1={"a":"aaa"}       #这种赋值不会改变全局 如果当成全局使用 需要先设置为 global
    a1["a"]="aaa"         #这种默认即可当成全局参数使用
    print(a1)
    

if __name__=="__main__":
    print(a)
    f()
    print(a)

    print(a1)
    f1()
    print(a1)

