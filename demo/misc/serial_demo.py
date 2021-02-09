#coding:utf8
#序列化与反序列化


#转换成可读的json文本

import json
a={"aa":"aaa","b":"bbbb"}

#serial
x=json.dumps(a)


#deserial
json.loads(x) 


######################################
#转换成特定的二进制格式

import pickle
a={"aa":"aaa","b":"bbbb"}

#serial
x=pickle.dumps(a)


#deserial
pickle.loads(x) 

"""

dump(object, file)
dumps(object) -> string
load(file) -> object
loads(string) -> object


file=open('path_to_file','wb')  
file=open('path_to_file','rb')  

if sys.version_info>(3,0):
    from io import StringIO
else:
    from StringIO import StringIO
file = StringIO()   
#可以类似文件操作的，只存于内存


pick = pickle.Pickler(file)  

#c实现的pickle，更加高效
import cPickle as pickle

"""
######################################     

#marshal格式不保证数据能移植到不同的 Python 版本中，主要用于支持读取和编写Python模块的.pyc文件
 
import marshal
a={"a":"aaaa"}

#serial
x=marshal.dumps(

#deserial
marshal.loads(x)     
     
     