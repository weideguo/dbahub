##登陆认证

# 服务端 -> 客户端
s1=b'\\\x00\x00\x00\n5.5.5-10.3.9-MariaDB-log\x00\x83Z\x00\x00/%jiQ;n;\x00\xfe\xf7\x08\x02\x00\xbf\x81\x15\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00zu\\KEV`bK0Mq\x00mysql_native_password\x00'

# 客户端 ->  服务端
c1=b'P\x00\x00\x01\x85\xa6\x0f\x20\x00\x00\x00\x01!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00test\x00\x14Y{\x95\x91Y/\xad\xf4\xae\xf4\x83\xb3\x99\xa2\xe8\xe4~\xfe\x9f\xb9mysql_native_password\x00'

# 服务端 -> 客户端
s2=b'\x07\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00'



########################################################################

def XOR(str1, str2):
    """
    两个等长字符串b'\xAA..'进行异或操作
    """
    if len(str1) != len(str2):
        raise Exception("two string is not in sample length")
    
    buf_str=b''
    
    for i in range(len(str1)):
        try:
            #python2
            _buf_str = ord(str1[i]) ^ ord(str2[i])
            __buf_str = chr(_buf_str)
        except:
            #python3
            _buf_str = str1[i] ^ str2[i]
            __buf_str = chr(_buf_str).encode('latin1')
        
        #print(__buf_str)
        buf_str += __buf_str
    
    return buf_str
    





salt=b'/%jiQ;n;zu\\KEV`bK0Mq'    #由第一个服务端发给客户端的包分析获得
mysql_password=b"test"           #实际明文密码


#客户端生成传给服务端的挑战认证数据  
#x := SHA1(password) XOR SHA1(salt + SHA1(SHA1(password)))
import hashlib
#p=hashlib.sha1(hashlib.sha1(mysql_password).digest()).digest()
#
#str2 = hashlib.sha1(salt+p).digest()
#
#str1 = hashlib.sha1(mysql_password).digest()


SHA1 = lambda x : hashlib.sha1(x).digest()

str1=SHA1(password) 
str2=SHA1(salt + SHA1(SHA1(password)))
    
client_secrect =  XOR(str1,str2)                               




##服务端验证
#SHA1(x XOR SHA1(salt + SHA1(SHA1(password)))) = SHA1(SHA1(password))
import base64
import hashlib


salt=b'/%jiQ;n;zu\\KEV`bK0Mq'
mysql_password_hash="*94BDCEBE19083CE2A1F959FD02F964C7AF4CFC29"      #存储于mysql.user表的实际值

p1 = base64.b16decode(mysql_password_hash[1:])                       #十六进制字符串转换成 b'\xAA..'

p == p1

px = hashlib.sha1(XOR(client_secrect, hashlib.sha1(salt+p).digest())).hexdigest().upper()

px1 = base64.b16encode(p).decode("latin1")      

px == px1



"""
#客户端将认证信息发个服务端
P\x00\x00                                                                                       #消息长度
\x01                                                                                            #序号
\x85\xa6                                                                                        #客户端权能标志 客户端收到服务器发来的初始化报文后，会对服务器发送的权能标志进行修改，保留自身所支持的功能，然后将权能标返回给服务器，从而保证服务器与客户端通讯的兼容性。
\x0f\x20                                                                                        #客户端权能标志扩展
\x00\x00\x00\x01                                                                                #最大消息长度 4
!                                                                                               #字符编码 1 
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00    #空填充 23
test                                                                                            #用户名
\x00                                                                                            #
\x14                                                                                            #挑战认证数据长度 1
Y{\x95\x91Y/\xad\xf4\xae\xf4\x83\xb3\x99\xa2\xe8\xe4~\xfe\x9f\xb9                               #挑战认证数据     20     SHA1(password) XOR SHA1(salt + SHA1(SHA1(password)))
mysql_native_password\x00
"""

"""
#服务端发给客户端OK响应报文
\x07\x00\x00    #消息长度
\x02            #序号
\x00            #1个字节的值，来区分响应报文的类型。
\x00            #受影响行数，当执行INSERT/UPDATE/DELETE语句时所影响的数据行数
\x00            #索引ID值
\x02\x00        #服务器状态
\x00\x00        #告警计数
"""                                                                                                 

