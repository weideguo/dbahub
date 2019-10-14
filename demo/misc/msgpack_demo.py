#二进制的使用

import msgpack

var = {'a': 'this',
       'b': 'is',
       'c': 'a test'
}

with open('/root/data.txt', 'wb') as f1:
    msgpack.dump(var, f1)                  # 存储数据
	
	
	
	
with open('/root/data.txt', 'rb') as f2:
    var = msgpack.load(f2, use_list=False, encoding='utf-8') # 读取数据
	print(var)
