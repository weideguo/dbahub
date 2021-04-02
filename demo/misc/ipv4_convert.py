#coding:utf8



def ipv4_convert(ipv4, convert_type=int):
    """
    ipv4转成10进制数字 16进制字符串 8进制字符串
    type: int hex oct
    """
    
    _ipv4 = ipv4.split(".")
    __ipv4 = int(_ipv4[0])*(2**24) + int(_ipv4[1])*(2**16)+ int(_ipv4[2])*(2**8) +int( _ipv4[3])*(2**0)
    return convert_type(__ipv4)



"""
浏览器中 url可以表示为 
http://点分十进制 == http://十进制 == http://0x十六进制 == http://0八进制 
http://127.0.0.1 == http://2130706433 == http://0x7F000001 == http://017700000001 

http:2130706433:8080/x/y/z

"""
