
import socket
import logging
import time
from ipaddr import IPAddress
from threading import Thread
from bitstring import Bits


ICMP_PROTO = socket.getprotobyname('icmp')
ICMP_ECHO_REQUEST_TYPE = 8
BUFSIZE = 4096


def checksum(data, checksum_offset=1):
    ''' calcualte checksum using one's complement sum of all 16-bit words,
        put the result in the `checksum_offset`th 16-bit word
        data and returned data is bitstring.Bits'''
    chunks = list(data.cut(16))
    s = sum(map(lambda x: x.uint, chunks))
    s = (s & 0xffff) + (s >> 16)
    chunks[checksum_offset] = ~ Bits(length=16, uint=s)
    return Bits(0).join(chunks)


def make_ip_packet(src, dst, protocol, body, id=42, ttl=64):
    ip_header = Bits(hex='4500') # IP version and type of service and etc
    total_length = Bits(length=16, uint=20+body.length/8) # Total length
    # The BSD suite of platforms (excluding OpenBSD) 
    # present the IP offset and length in host byte order.
    # as they say... It's a feature, not a BUG!
    total_length = Bits(length=16, uint=socket.htons(total_length.uint))
    ip_header += total_length
    ip_header += Bits(length=16, uint=id)  # identification
    ip_header += Bits(hex='0000')  # flags, fragment offset
    ip_header += Bits(length=8, uint=ttl) # TTL
    ip_header += Bits(length=8, uint=protocol)
    ip_header += Bits(hex='0000') # checksum
    ip_header += Bits(length=32, uint=int(IPAddress(src)))
    ip_header += Bits(length=32, uint=int(IPAddress(dst)))
    return checksum(ip_header, 5) + body


def make_icmp_packet(typ, code=0, body=None, id=42, seq=42):
    icmp_header = Bits(length=8, uint=typ) # type
    icmp_header += Bits(length=8, uint=code) # code
    icmp_header += Bits(hex='0000')  # checksum
    icmp_header += Bits(length=16, uint=id) + Bits(length=16, uint=seq)
    icmp_header = checksum(icmp_header)
    return icmp_header if body is None else (icmp_header+body)


    


if __name__=='__main__':
    NO_RESPONSE_IP = '1.1.1.1'
    PING_INTERVAL = 10
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, ICMP_PROTO)        
    """
    使用raw模式，即需要完全控制传输层的数据包
    如实际工作为tcp，则需要自行实现三次握手
    """
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)    
    sock.settimeout(PING_INTERVAL)     
  
    #发出icmp请求 即类似于ping 1.1.1.1操作
    ip=NO_RESPONSE_IP
    icmp_packet = make_icmp_packet(ICMP_ECHO_REQUEST_TYPE)
    ip_packet = make_ip_packet(0, ip, ICMP_PROTO, icmp_packet)
    sock.sendto(ip_packet.bytes, (ip, 1))
    
    
    #icmp响应包
    response = sock.recv(BUFSIZE)    
    response = Bits(bytes=response)
    source_ip = response[12*8:][:4*8]
    source_ip = IPAddress(source_ip.uint)
    response = response[20*8:]              
    typ = response[:8]
    
    
    #构造icmp响应 time exceed
    server_ip='1.2.3.4'
    ICMP_TIME_EXCEED_TYPE = 11
    inner_icmp = make_icmp_packet(ICMP_ECHO_REQUEST_TYPE)
    inner_ip = make_ip_packet(server_ip, NO_RESPONSE_IP, ICMP_PROTO, inner_icmp)
    icmp_packet = make_icmp_packet(ICMP_TIME_EXCEED_TYPE, body=inner_ip)
    ip_packet = make_ip_packet(0, server_ip, ICMP_PROTO, icmp_packet)
    sock.sendto(ip_packet.bytes, (server_ip, 1))


    