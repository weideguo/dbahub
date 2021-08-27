#mysql_native_password 握手过程
#python2 python3
#10.3.9-MariaDB  5.7.30


import socket

mysql_host='127.0.0.1'
mysql_port=1039
#mysql_host='172.16.2.150'
#mysql_port=2433


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((mysql_host,mysql_port))

s=sock.recv(1024)                 #创建连接时第一个握手包





def sub_str(origin_str, sub_len):
    """
    从字符串截(b'\xAA...')取指定长度，大于0则从头截取，小于则从尾部截取
    """
    if abs(sub_len) > len(origin_str):
        raise Exception("substring too long")
    if sub_len>0:
        return origin_str[:sub_len],origin_str[sub_len:]
    else:
        return origin_str[sub_len:],origin_str[:sub_len]


def str_to_int(s):
    """
    little-endian格式的str(b'\xAA..')转换成数字
    """
    
    def format_bin(c):
        """
        以0填充成8位
        """
        raw_bin=bin(c).replace('0b', '')
        return (8-len(raw_bin))*'0'+raw_bin
    
    try:
        #python2
        bin_str=''.join([format_bin(ord(c))[::-1] for c in s])
    except:
        #python3
        bin_str=''.join([format_bin(c)[::-1] for c in s])
    
    #print(bin_str)
    
    return int(bin_str[::-1],2)



#s1=s[0:3]
#s=s[3:]
packet_length      ,s=sub_str(s,3)                    #消息长度 不包括当前4字符的包长度   消息长度+序号=消息头    
serial_no          ,s=sub_str(s,1)                    #序号 在一次完整的请求/响应交互过程中，用于保证消息顺序的正确，每次客户端发起请求时，序号值都会从0开始计算。

packet_length_int    = str_to_int(packet_length)
serial_no_int        = str_to_int(serial_no)


protocal_version   ,s=sub_str(s,1)                    #第一个字节表示协议版本号 
protocal_version_int = str_to_int(protocal_version)




i=0
while True:
    if s[i]==0 or s[i]== b'\x00':
        break
    else:
        i=i+1

server_version ,s =sub_str(s,i)                      #服务器版本  
s01            ,s =sub_str(s,1)                     
connection_id  ,s =sub_str(s,4)                      #服务器分配线程id
salt1          ,s =sub_str(s,8)                      #随机数1     
s02            ,s =sub_str(s,1)

#####
rs00      ,s =sub_str(s,-1)
         
i=-1
while True:
    if s[i]==0 or s[i]== b'\x00':
        break
    else:
        i=i-1


auth_plugin_name ,s=sub_str(s,i+1)           #mysq5.1 没有使用
rs01    ,s =sub_str(s,-1)                    #mysq5.1 没有使用


salt2   ,s =sub_str(s,-12)                   #随机数2
padding ,s =sub_str(s,-10)                   #填充数
rs1     ,s =sub_str(s,-1)                    #未使用

######
capability_flag_1  ,s=sub_str(s,2)
s_character_set    ,s=sub_str(s,1)
s_status_flags     ,s=sub_str(s,2)
capability_flag_2  ,s=sub_str(s,2)


salt=salt1+salt2

"""
服务端->客户端 第一个包数据解析
\\\x00\x00                                            消息长度                         3
\x00                                                  序号                             1
\n                                                    协议版本号                       1 
5.5.5-10.3.9-MariaDB-log                              服务器版本 不定长 
\x00
`Z\x00\x00                                            服务器分配线程id                 4
7!=OWHAN                                              随机数1                          8      
\x00                                                                                   
\xfe\xf7                                              服务器权能标志（一些约定信息）   2
\x08                                                  字符编码                         1
\x02\x00                                              服务器状态                       2
\xbf\x81                                              服务器权能标志（高16位）         2
\x15
\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00              填充数                           10
CEo#]*X]KAAa                                          随机数2                          12字节
\x00
mysql_native_password
\x00

salt=随机数1+随机数2
#数子以小端记录  二进制格式从低位开始计算（即左边开始）
"""

"""
import base64
s=b"xxx"
h=base64.b16encode(s)               #转成16进制串  
base64.b16decode(h)                 #转成字符串 b'\xAA...'
"""

"""
#客户端发送给服务端
x := SHA1(password) XOR SHA1(salt + SHA1(SHA1(password)))


#服务端验证
SHA1(x XOR SHA1(salt + SHA1(SHA1(password)))) = SHA1(SHA1(password))


XOR 异或满足结合律
"""

import hashlib

def mysql_native_password(password):
    """
    使用mysql_native_password时在mysql.user表password字段的值
    """
    mysql_password=password.encode('latin1')
    
    mysql_password_hash = hashlib.sha1(hashlib.sha1(mysql_password).digest()).hexdigest()
    
    return mysql_password_hash


"""
参考
https://github.com/cyrus-and/mysql-unsha1


 ./mysql-unsha1-sniff -i lo 127.0.0.1 3306 2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19:root
[+] origin_str:
[+] - username ........................ 'root'
[+] - salt ............................ 3274756c42415d3429717e482a3776704d706b49
[+] - client session password ......... 6d45a453b989ad0ff0c84daf623e9870f129c329
[+] - SHA1(SHA1(password)) ............ 2470c0c06dee42fd1618bb99005adca2ec9d1e19
[+] Output:
[+] - SHA1(password) .................. 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
[+] Check:
[+] - computed SHA1(SHA1(password)) ... 2470c0c06dee42fd1618bb99005adca2ec9d1e19
[+] - authentication status ........... OK



mysql-unsha1 -h 127.0.0.1 -P 3306 -u root --password=5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8

mysql> SELECT SHA1(UNHEX('5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'));
2470c0c06dee42fd1618bb99005adca2ec9d1e19

知道在mysql.user存储的值，可以进行登陆
"""