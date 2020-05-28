#coding:utf8
import struct
from socket import inet_aton
import os

"""Database for search IPv4 address.

The 17mon dat file format in bytes::

    -----------
    | 4 bytes |                     <- offset number
    -----------------
    | 256 * 4 bytes |               <- first ip number index
    -----------------------
    | offset - 1028 bytes |         <- ip index
    -----------------------
    |    data  storage    |
    -----------------------
"""


_unpack_V = lambda b: struct.unpack("<L", b)
_unpack_N = lambda b: struct.unpack(">L", b)

def _unpack_C(b):
    if isinstance(b, int):
        #python3
        return b
    #python2
    return struct.unpack("B", b)[0]

class IP:
    offset = 0
    index = 0
    binary = ""

    @staticmethod
    def load(file):
        try:
            path = os.path.abspath(file)
            with open(path, "rb") as f:
                IP.binary = f.read()
                IP.offset, = _unpack_N(IP.binary[:4])
                IP.index = IP.binary[4:IP.offset]
        except Exception as ex:
            print("cannot open file %s" % file)
            print(ex.message)
            exit(0)

    @staticmethod
    def find(ip):
        index = IP.index
        offset = IP.offset
        binary = IP.binary
        nip = inet_aton(ip)
        ipdot = ip.split('.')
        if int(ipdot[0]) < 0 or int(ipdot[0]) > 255 or len(ipdot) != 4:
            return "N/A"

        tmp_offset = int(ipdot[0]) * 4
        #使用4字节记录第一个ip段在索引的信息
        start, = _unpack_V(index[tmp_offset:tmp_offset + 4])

        index_offset = index_length = 0
        max_comp_len = offset - 1028
        #1024 第一个ip索引的占用
        start = start * 8 + 1024
        while start < max_comp_len:
            #每个ip信息使用8字节索引
            #4字节记录ip
            #3字节记录数据的偏移量
            #1字节记录数据的大小
            _index = index[start:start+8]
            
            if _index[0:4] >= nip :
                index_offset, = _unpack_V(_index[4:7]+chr(0).encode('utf-8'))
                index_length = _unpack_C(_index[-1])
                break
                
            start += 8

        if index_offset == 0:
            return "N/A"
        
        #1024？记录的index_offset每个都比实际大1024
        res_offset = offset + index_offset - 1024
        #print(offset)
        #print(index_offset)
        #print(res_offset,index_length)
        return binary[res_offset:res_offset + index_length].decode('utf-8')


if __name__ == "__main__":
    import sys
    import socket
    #从ipip.net下载/更新数据库
    IP.load("17monipdb.dat")
    
    ip=sys.argv[1]
    #域名解析
    ip = socket.gethostbyname(ip)
    print(IP.find(ip))
    #print(IP.find("114.114.114.114"))

