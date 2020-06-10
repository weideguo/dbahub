
'''
zabbix_api
├── workdir
│   ├── get_zabbbix_value.py
│	├── __init__.py             # 当成模块时需要创建该文件 可以为空或者里面的对象可以直接调用(不需要再指定文件对应的模块名)
│   └── yyy.py					# import  get_zabbbix_value
└──  xxx.py        				# impoer workdir.get_zabbbix_value
'''


#继承
class Mammal(Object):
	pass

class Dog(Mammal):				 #单继承
    pass
	
class Dog(Mammal, Runnable):     #多重继承
    pass


