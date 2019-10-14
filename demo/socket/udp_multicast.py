
#组播/多播
#可以跨域？ 需要路由特定设置？


#sender
import socket

multicast_group_ip = '239.255.255.252'    # 组播组IP ip须在组播地址内
multicast_group_port = 8001

#send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "I am multicast"
send_sock.sendto(message.encode(), (multicast_group_ip, multicast_group_port))






#receiver
import socket

multicast_group_ip = "239.255.255.252"
server_address = ("0.0.0.0",8001)
 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(server_address)
#import struct 
#mreq = struct.pack('4sL',socket.inet_aton(multicast_group_ip),socket.INADDR_ANY)  #socket.INADDR_ANY  #"0.0.0.0"
mreq = socket.inet_aton(multicast_group_ip)+socket.inet_aton("0.0.0.0")
sock.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,mreq)   #设置加入组播
 
# sock.setblocking(0) # 设置非阻塞 默认为阻塞
data,address = sock.recvfrom(1024)

	
	
"""
setsockopt(level, option, value)
          ([family[, type[, proto]]])
"""	

"""
224.0.0.0～224.0.0.255     为预留的组播地址（永久组地址），地址224.0.0.0保留不做分配，其它地址供路由协议使用；
224.0.1.0～224.0.1.255     是公用组播地址，可以用于Internet；
224.0.2.0～238.255.255.255 为用户可用的组播地址（临时组地址），全网范围内有效；
239.0.0.0～239.255.255.255 为本地管理组播地址，仅在特定的本地范围内有效。

"""
