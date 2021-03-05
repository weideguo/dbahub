from scapy.all import *

conf.L3socket=L3RawSocket

sport=10000
#dport=45000
dport=1039
pkt=IP(src="192.168.253.128", dst="192.168.253.128")


#通过flags响应的状态？

#创建连接 三次握手 本地发送两次 远端发送一次


SYN=pkt/TCP(sport=sport, dport=dport, flags="S")
SYNACK=sr1(SYN)   #发送SYN，接收远端响应SYNACK
SYNACK

ACK=pkt/TCP(sport=sport, dport=dport, flags="A", seq=SYNACK.ack, ack=SYNACK.seq + 1)
send(ACK)         #对远端的响应SYNACK发送 ACK


"""
以上完成连接创建，数据可以在此传输，本地传输时需要远端确认响应
"""


#断开 四次挥手 本地发送两次 远端发送一次（隐含为两次？）

#FIN=pkt/TCP(sport=sport, dport=dport, flags="FA", seq=SYNACK.ack, ack=SYNACK.seq + 1)
FIN=pkt/TCP(sport=sport, dport=dport, flags="FA")
FINACK=sr1(FIN)   #发送FIN 远端回应 ACK 并发送FIN给本地


LASTACK=pkt/TCP(sport=sport, dport=dport, flags="A", seq=FINACK.ack, ack=FINACK.seq + 1)
send(LASTACK)    #对FINACK回应 完成断开 


"""
全扫描   完成三次握手
半扫描   只发SYN包进行端口扫描，但有可能被对方防火墙拦截 
FIN扫描  只发FIN包进行端口扫描 
"""
