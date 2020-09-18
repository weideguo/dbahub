#coding:utf8
##命令行模式
#文件名必须为 fabfile.py  ？
#touch fabfile.py 
from invoke import task

@task
def hello(c):
    c.run("echo 'hello fabric'")
    print("hello fabric!")


#运行 默认本地执行
#fab hello

#在远端主机执行  逐个主机执行
#fab --prompt-for-login-password --hosts host1,host2,host3 hello 
#指定用户以及端口
#fab --prompt-for-login-password --hosts username@host1:ssh_port,username@host2:ssh_port hello 


