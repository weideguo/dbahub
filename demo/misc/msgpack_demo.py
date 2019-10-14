#二进制的使用

import msgpack

var = {'a': 'this',
       'b': 'is',
       'c': 'a test'
}

#直接转换
#参数可以是字符串 字典
x=msgpack.dumps(var)
msgpack.loads(x)


with open('/root/data.txt', 'wb') as f1:
    msgpack.dump(var, f1)                  # 存储数据
	
	
	
	
with open('/root/data.txt', 'rb') as f2:
    var = msgpack.load(f2, use_list=False, encoding='utf-8') # 读取数据
	print(var)
