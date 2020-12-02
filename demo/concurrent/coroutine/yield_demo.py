#coding:utf8
#生成器 generator

def f(n):
    for i in range(n):
        yield i*i

			
if __name__ == "__main__":			
    a=f(10)
    for x in a:
        print(x)



