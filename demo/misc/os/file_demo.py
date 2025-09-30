

#需要进行显示关闭
#f=file("/path_to_file/file_name","r")   #file() open() 两者类似返回值都是file类
###读操作
f=open("file_path","r")   ###打开文件
f.read()                  ###读文件 read()会一次性读取文件的全部内容  可以反复调用read(size)方法读取定长内容
f.close()				  ###关闭文件

###写操作
f = open('/Users/michael/test.txt', 'w')    ###打开文件
f.write('Hello, world!')					###写操作
f.close()									###关闭文件


#结束模块时自动关闭 不必显式关闭
with open("/path_to_file/file_name","r") as f:
    f.read()

try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()


#移动文件指针
#当调用read时，指针会移动到文件尾部，再次read前需要先移动文件指针
#或者以读写方式打开，写文件后想读取，则需要先移动文件指针
f.seek(0)  


def read(f):
    """同时兼容读路径与文件流"""
    import _io
    _str=""
    if isinstance(f,_io.TextIOWrapper):
        _str=f.read()
    else:
        with open(f) as fp:
            _str=fp.read()
    
    return _str
    

"""
'r', 'w','a'  读 写 增加
'b'  二进制形式打开 不加这个默认会以utf8进行编码转换
'+'  允许同时读写 

全部模式
r rb r+ rb+ 
w wb w+ wb+
a ab a+ ab+

r+ 读写 文件不存在时报错，不清空原有文件。适用于修改文件部分内容。
w+ 写读 文件不存在时创建，清空原有文件
"""

