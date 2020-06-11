"""
属性在运行时的动态替换，叫做猴子补丁（Monkey Patch）
"""
class Foo(object):
    def bar(self):
        print('Foo.bar')

def bar():
    print('Modified bar')


f=Foo()
f.bar=bar
f.bar()


