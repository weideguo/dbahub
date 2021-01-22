#coding:utf8

#逐行遍历文件

filename="myfile.log"

with open(filename, "r") as f:
    #for line in f.readlines():
    for line in f:
        print(line)
        

with open(filename, 'r') as f:
    while True:
        line = f.readline()
        if not line:
          break
        
        print(line)   



#加载到cache读取
import linecache

line_no=1
linecache.getline(filename, line_no)

#清除cache 在不需要再getline时操作
linecache.clearcache()

#如果文件在磁盘中发生改变，进行检查重载
linecache.checkcache(filename)


