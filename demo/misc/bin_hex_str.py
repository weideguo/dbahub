#coding:utf8
#字符串与十六进制、二进制之间的转换

def str_to_hex(s):
    return r"\x"+r'\x'.join([hex(ord(c)).replace('0x', '') for c in s])

def hex_to_str(s):
    return ''.join([chr(i) for i in [int(b, 16) for b in s.split(r'\x')[1:]]])
    
def str_to_bin(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])
    
def bin_to_str(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])
    
    
    
h=str_to_hex("abc")

hex_to_str(h)


b=str_to_bin("abc")

bin_to_str(b)

 