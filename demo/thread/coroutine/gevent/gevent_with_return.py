#coding:utf8
import gevent
#from gevent import socket
import socket

def method1():
    try:
        # get local ip using UDP and a  broadcast address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.connect(('239.255.255.250', 1))
        return [s.getsockname()[0]]
    except:
        pass

def method2():
    # Get ip by using UDP and a normal address (google dns ip)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 0))
        return [s.getsockname()[0]]
    except:
        pass

def method3():
    # Get ip by '' hostname . Not supported on all platforms.
    try:
        return socket.gethostbyname_ex('')[2]
    except:
        pass



threads = [
    gevent.spawn(method1),
    gevent.spawn(method2),
    gevent.spawn(method3)
]

gevent.joinall(threads, timeout=5)

local_ips = []
for thread in threads:
    if thread.value:
        local_ips += thread.value
        
local_ips = list(set(local_ips))        
print(local_ips)