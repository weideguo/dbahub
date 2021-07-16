mod = __import__(name)   # 模块名 即时为文件名去除后缀
cls = getattr(mod, 'A')  # 另外模块中定义 class A
cls().showme()


import importlib
mode=importlib.import_module(name, package=None)
cls = getattr(mod, 'A')  # 另外模块中定义 class A
cls().showme()


#getattr(object, name[, default])
#获取对象的属性
class A(object):
    a='aaa'
    def f(self):
        print('fff')

f0=getattr(A,'f')  #f0('')
a0=getattr(A,'a')



#热加载技术
"""
监听文件的时间 时间改变 即时加载
"""

module = sys.modules['model_name']          #模块名 即为文件名去除后缀
reload(module)                              #重新加载模块 实现热加载    


sys.modules
"""
所有已经加载的模块的字典
"""

#config.py
a="aaaa"


#demo.py
if __name__ == "__main__":
    import time
    #from imp import reload          #python2
    from importlib import reload     #python3
    
    import config
    while True:
        reload(config)
        print(config.a)
        time.sleep(2)
        
#config.py可以在线更改 无需重新运行demo.py