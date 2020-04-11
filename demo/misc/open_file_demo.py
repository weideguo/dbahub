"""
'r', 'w','a'  读 写 增加
'b'  二进制形式打开
'+'  允许同时读写 

全部模式
r rb r+ rb+ 
w wb w+ wb+
a ab a+ ab+
"""

#需要进行显示关闭
#f=file("/path_to_file/file_name","r")   #file() open() 两者类似返回值都是file类
f=open("/path_to_file/file_name","r")
f.read()
f.close()


#结束模块时自动关闭 不必显式关闭
with open("/path_to_file/file_name","r") as f:
    f.read()

#移动文件指针
#当调用read时，指针会移动到文件尾部，再次read前需要先移动文件指针
#或者以读写方式打开，写文件后想读取，则需要先移动文件指针
f.seek(0)    
