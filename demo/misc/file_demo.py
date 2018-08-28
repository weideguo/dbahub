
###读操作
f=open("file_path","r")   ###打开文件
f.read()                  ###读文件 read()会一次性读取文件的全部内容  可以反复调用read(size)方法读取定长内容
f.close()				  ###关闭文件

###写操作
f = open('/Users/michael/test.txt', 'w')    ###打开文件
f.write('Hello, world!')					###写操作
f.close()									###关闭文件


with open('/path/to/file', 'r') as f:
    print f.read()

try:
    f = open('/path/to/file', 'r')
    print f.read()
finally:
    if f:
        f.close()
