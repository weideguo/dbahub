#coding:utf8

import hashlib


SHA256 = lambda x : hashlib.sha256(x).digest()

# 服户端
password=b"mysql_passwd"
_password = password
for i in range(5000+1):
    _password = SHA256(_password)



# 客户端

Nonce = b'\x38\x34\x27\x29\x09\x61\x0d\x44\x16\x2b\x42\x22\x25\x20\x5e\x77\x25\x38\x7b\x05\x00'

_passwordx = b'\x9e\x88\x7d\x0d\x6a\x73\x03\x66\x89\xbd\x56\xb4\xef\x79\x73\xd7\xda\xb1\x75\xde\x13\x25\xd7\x7d\x0d\x8e\xf8\x77\x20\xb9\xf4\x6f'


# 客户端返回
double_sha = SHA256(SHA256(password)) 
client_secret = SHA256(double_sha XOR Nonce)    # 用于缓存对比


"""    
客户端返回缓存命中，返回确认

缓存不命中：
使用TLS/SSL、Socket、Shared Memory，通过TLS将明文密码传递给服务端
不使用TLS/SSL，客户端与服务端交互获取RSA公钥，通过RSA将明文密码传递给服务端


源代码
sql/auth/sha2_password.cc
https://github.com/mysql/mysql-server/blob/mysql-8.4.7/sql/auth/sha2_password.cc#L853
"""
