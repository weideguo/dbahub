#在代码中执行python代码

s="""
for i in range(10):
    print(i)
"""

exec(s)         #执行python代码 没有返回值

a="{'a':'aaa'}"
def f():
    print("aaa")

b="f"
a0=eval(a)     #执行单个表达式python代码 有返回值
b0=eval(b)



c = compile(s,'','exec')
exec(c)

c = compile(b,'','eval')
f1=eval(c)

single_str = 'a = input("Input a number: ")'
code_single = compile(single_str, '', 'single')   #交互式
eval(code_single)


python_src = """
import time
a = time.time()
"""
exec(python_src)
print(a)
