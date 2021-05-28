import paramiko
from paramiko import SSHClient,SSHConfig

hostname="192.168.253.128"
port=22
username="root"
password="weideguo"


key_filename=None
proxy=None

client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=hostname, port=port, username=username, password=password,sock=proxy,key_filename=key_filename)
ssh_client=client

#cmd="who"
#stdin, stdout, stderr = ssh_client.exec_command(cmd)
#
#print(stdout.read(), stderr.read())


#cmd="/data/redis/bin/redis-server /data/redis/redis.conf "

cmd="cd /data/redis/ && bin/redis-server redis.conf &"

cmd = "echo 222 && sleep 1000 && echo 111 "

cmd ="echo 111 && xxx && sleep 10000 "

#cmd ="xxxx &"
channel = ssh_client._transport.open_session()
channel.exec_command(cmd)

channel.exit_status_ready()

channel.recv_stderr_ready()
channel.recv_stderr(10)



channel.recv_exit_status()   #阻塞
channel.get_id()

channel.recv(10)


channel.recv_ready()

cmd="cd /data/redis/ && bin/redis-server redis.conf & #"


import subprocess

cmd="sleep 1000 && echo 111"

#cmd="cd /data/redis && bin/redis-server redis.conf &"
p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,bufsize=1)

#print(p.stdout.read(),p.stderr.read())


