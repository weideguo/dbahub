host_info={"ip":"10.10.19.13","ssh_port":22,"user":"test","passwd":"test"}

import paramiko
from paramiko import SSHClient

client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host_info["ip"],port=int(host_info["ssh_port"]), username=host_info["user"],\
                        password=host_info["passwd"])

#多线程并发使用时也只有一个ssh连接，即只有一个tcp连接
ssh_client=client
ftp_client=ssh_client.open_sftp()

exist_remote_file="/root/test.sh"

remote_file="/home"

ftp_client.symlink(exist_remote_file,remote_file)




########################################################################################
#host_info1 通过代理 host_info连接

host_info={"ip":"192.168.65.130","ssh_port":22,"user":"weideguo","passwd":"weideguo"}

import paramiko
from paramiko import SSHClient

client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host_info["ip"],port=int(host_info["ssh_port"]), username=host_info["user"],\
                        password=host_info["passwd"])


#stdin,stdout,stderr=client.exec_command("pwd")
#print(stdout.read())

transport=client.get_transport()



host_info1={"ip":"192.168.65.131","ssh_port":22,"user":"root","passwd":"weideguo"}

sock=transport.open_channel(kind="direct-tcpip", dest_addr=(host_info1["ip"], int(host_info1["ssh_port"])), src_addr=("", 0))

#sock=None
client2 = SSHClient()
client2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client2.connect(hostname=host_info1["ip"],port=int(host_info1["ssh_port"]), username=host_info1["user"],\
                        password=host_info1["passwd"],sock=sock)

stdin,stdout,stderr=client2.exec_command("pwd")
print(stdout.read())




########################################################################################
#host_info 通过配置文件的代理设置进行代理连接 需要依赖本地的ssh命令 比python实现的代理模式快？


host_info={"ip":"192.168.65.130","ssh_port":22,"user":"weideguo","passwd":"weideguo"}

import paramiko
from paramiko import SSHClient

config = SSHConfig()
proxy = None
ssh_config="~/.ssh/config"
f=os.path.expanduser(ssh_config)
if os.path.isfile(f):
    config.parse(open(f))
    #读取配置文件不区分大小写 都转换成小写
    host=config.lookup(self.hostname)
    if "proxycommand" in host:
        proxy = paramiko.ProxyCommand(host["proxycommand"])

#ssh -W hostB hostA       
#相当于执行该命令，ssh连接hostA，将tcp信息转发给hostB
proxy = paramiko.ProxyCommand(host["proxycommand"])


client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host_info["ip"],port=int(host_info["ssh_port"]), username=host_info["user"],\
                        password=host_info["passwd"], sock=proxy)



