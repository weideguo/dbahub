#coding:uft8


#read_per_line.py
import sys
while True:
    line = sys.stdin.readline()
    if not line:
        break
    sys.stdout.write(line)
    sys.stdout.flush()





from shlex import split as shlsplit
from subprocessess import *

command_line='python  read_per_line.py'
cmd=shlsplit(command_line)
process =Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT, bufsize=1)

#可以多次调用输入与输出
string = 'say hi123121234\n'      #因为命令行单次以行处理，在此以"\n"结尾
process.stdin.write(string)
line = process.stdout.readline()     #使用read()时必须指定长度
print(line)
process.stdout.flush()               #???






##################################################################################################
#使用redis测试

from shlex import split as shlsplit
from subprocessess import *

command_line='telnet 127.0.0.1 6479'
cmd=shlsplit(command_line)
process =Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=STDOUT, bufsize=1)


string = 'auth my_redis_passwd\n'      
process.stdin.write(string)
process.stdout.readline()                #读取超过会阻塞 如果为read()需要确定值


string = 'hgetall __solve__\n'      
process.stdin.write(string)
process.stdout.readline()


import os
os.read(process.stdout.fileno(), 10000000)      #读取超过不会阻塞，但如果stdout已经读取完毕则会阻塞









