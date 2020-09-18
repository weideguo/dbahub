#coding:utf8
#基于ssh实现的shell命令执行
#基于paramiko库


from fabric import Connection

#username@host1:ssh_port   #host可以使用这种格式
c = Connection(host="192.168.253.128", port=22, user="root", connect_kwargs={"password":"my_ssh_password"})
c = Connection(host="root@192.168.253.128:22", connect_kwargs={"password":"my_ssh_password"})
#只能执行/usr/bin目录下的命令 
c.run("uname -a")       #在第一次执行命令时ssh连接才创建并保持
#上传文件
#c.put('myfiles.tgz', '/tmp')


#/sbin目录下的命令需要sudo
from fabric import Connection, Config
config = Config(overrides={'sudo': {'password': "my_ssh_password"}})   #'sudo': {'password': 'my_ssh_password', 'prompt': '[sudo] password: ', 'user': None}
c = Connection(host="192.168.253.128", port=22, user="root", connect_kwargs={"password":"my_ssh_password"}, config=config)
c.run("ifconfig")    
c.sudo("ifconfig")




###使用gateway设置跳板 即使先ssh跳到gateway指定的主机，然后再在该主机ssh连接指定主机，可以使用多级gateway
#全链路ssh连接一直保持
#Connecton(..., gateway=Connection('user1@hop1.host', gateway=Connection('user2@hop2.host', gateway=...)))

#先跳到192.168.1.10 然后再连接 10.10.1.10
c=Connection(host="10.10.1.10", port=22, user="root", connect_kwargs={"password":"my_ssh_password"}, gateway=Connection(host="192.168.1.10", port=22, user="root", connect_kwargs={"password":"my_hop_ssh_password"}))
c.run("who")



from fabric import SerialGroup as Group

"""
group = SerialGroup(
    "host1", "host2", "host3", user="admin", forward_agent=True,
)
"""
#username@host1:ssh_port
for c in Group('web1', 'web2', 'web3', connect_kwargs={"password":"my_ssh_password"}):
   c.run("who")


#pool = Group('web1', 'web2', 'web3')
#pool.put('myfiles.tgz', '/opt/mydata')
#pool.run('tar -C /opt/mydata -xzvf /opt/mydata/myfiles.tgz')


#并发执行
#from fabric import ThreadingGroup as Group



