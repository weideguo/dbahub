#!/usr/bin/env python
# coding: utf-8
# author: frk
# update: weideguo
# python2/python3

import struct
from socket import inet_aton
import os

_unpack_V = lambda b: struct.unpack("<L", b)
_unpack_N = lambda b: struct.unpack(">L", b)

def _unpack_C(b):
    if isinstance(b, int):
        #python3
        return b
    #python2
    return struct.unpack("B", b)[0]

class IP:
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
        start, = _unpack_V(index[tmp_offset:tmp_offset + 4])

        index_offset = index_length = 0
        max_comp_len = offset - 1028
        start = start * 8 + 1024
        while start < max_comp_len:
            if index[start:start + 4] >= nip:
                index_offset, = _unpack_V(index[start + 4:start + 7] + chr(0).encode('utf-8'))
                index_length = _unpack_C(index[start + 7])
                break
            start += 8

        if index_offset == 0:
            return "N/A"

        res_offset = offset + index_offset - 1024
        return binary[res_offset:res_offset + index_length].decode('utf-8')


class IPX:
    binary = ""
    index = 0
    offset = 0

    @staticmethod
    def load(file):
        try:
            path = os.path.abspath(file)
            with open(path, "rb") as f:
                IPX.binary = f.read()
                IPX.offset, = _unpack_N(IPX.binary[:4])
                IPX.index = IPX.binary[4:IPX.offset]
        except Exception as ex:
            print("cannot open file %s" % file)
            print(ex.message)
            exit(0)

    @staticmethod
    def find(ip):
        index = IPX.index
        offset = IPX.offset
        binary = IPX.binary
        nip = inet_aton(ip)
        ipdot = ip.split('.')
        if int(ipdot[0]) < 0 or int(ipdot[0]) > 255 or len(ipdot) != 4:
            return "N/A"

        tmp_offset = (int(ipdot[0]) * 256 + int(ipdot[1])) * 4
        start, = _unpack_V(index[tmp_offset:tmp_offset + 4])

        index_offset = index_length = -1
        max_comp_len = offset - 262144 - 4
        start = start * 9 + 262144

        while start < max_comp_len:
            if index[start:start + 4] >= nip:
                index_offset, = _unpack_V(index[start + 4:start + 7] + chr(0).encode('utf-8'))
                index_length = _unpack_C(index[start + 8:start + 9])
                break
            start += 9

        if index_offset == 0:
            return "N/A"

        res_offset = offset + index_offset - 262144
        return binary[res_offset:res_offset + index_length].decode('utf-8')
        

if __name__=="__main__":
    import sys
    import socket
    #从ipip.net下载/更新数据库
    IP.load("17monipdb.dat")
    
    ip=sys.argv[1]
    #域名解析
    ip = socket.gethostbyname(ip)
    print(IP.find(ip))
    

    """
    #需要付费？
    IPX.load("mydata4vipday2.datx")
    print(IPX.find(ip))
    """


