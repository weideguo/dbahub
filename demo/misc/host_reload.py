mod = __import__(name)   # 模块名 即时为文件名去除后缀
cls = getattr(mod, 'A')  # 另外模块中定义 class A
cls().showme()


import importlib
mode=importlib.import_module(name, package=None)
cls = getattr(mod, 'A')  # 另外模块中定义 class A
cls().showme()



#热加载技术
"""
监听文件的时间 时间改变 即时加载
"""

module = sys.modules['model_name']          #模块名 即时为文件名去除后缀
reload(module)                              #重新加载模块 实现热加载    


sys.modules
"""
所有已经加载的模块的字典
"""
