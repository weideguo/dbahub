host_info={"ip":"10.10.19.13","ssh_port":22,"user":"test","passwd":"test"}

import paramiko
from paramiko import SSHClient

client = SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host_info["ip"],port=int(host_info["ssh_port"]), username=host_info["user"],\
                        password=host_info["passwd"])

ssh_client=client
ftp_client=ssh_client.open_sftp()

exist_remote_file="/root/test.sh"

remote_file="/home"

ftp_client.symlink(exist_remote_file,remote_file)