#!/bin/env python
"""
仅使用减法实现的10进制转二进制
"""


def to_bin(n):
    #n>=0
    bin_str=""
    while True:
        if n==0:
            if bin_str=="":
                return "0"
            else:
                return bin_str
            
        elif n==1:
            #return last2(bin_str)
            return last(bin_str)
            
        else:
            if bin_str=="":
                #bin_str="01"
                bin_str="10"
            else:
                #bin_str=bin_str[0]+last2(bin_str[1:])
                bin_str=last(bin_str[:-1])+bin_str[-1]
            n=n-2


def to_bin2(n):
    #n>=0
    bin_str=""
    for i in range(n):
        bin_str=last(bin_str)
    
    if bin_str:
        return bin_str
    else:
        return "0"
    

def last(bin_str):
    #左往右最后一位进1
    if bin_str=="":
        return "1"
    elif bin_str[-1]=="0":
        return bin_str[:-1]+"1"
    else:
        return last(bin_str[:-1])+"0"
    

def last2(bin_str):
    #左往右第一位进1
    if bin_str=="":
        return "1"
    elif bin_str[0]=="0":
        return "1"+bin_str[1:]
    else:
        return "0"+last(bin_str[1:])


def reverse(s):
    #左往右倒序
    if len(s)==0:
        r=""
    elif len(s)==1:
        r=s
    else:
        r=s[-1]+reverse(s[0:-1])
    
    return r
        
        
"""
#使用
>>> reverse(to_bin(9996))
'10011100001100'

#校验
>>> bin(9996)
'0b10011100001100'
"""

