#coding:utf8
import time

filename="/tmp/test.txt"
f=open(filename,"a+")             #只要数据落盘，open操作任何模式都能看到文件的变化

msg="aaaa"
i=0
while True:
    i += 1
    f.write(msg+str(i)+"\n")
    time.sleep(1)
    if not i % 3:
        f.flush()    #调用之后才从内存刷到磁盘，如果不落盘，则其他进程看不到数据
                     #即使外部用 mv 命令移动文件，也依然写到移动后的文件
                     #cat test.txt > test.txt.2 && echo -n > test.txt   #分割 操作时存在落盘操作是否会有数据丢失？flush前通过加文件锁实现更安全操作？

f.close()           #也会先落盘

