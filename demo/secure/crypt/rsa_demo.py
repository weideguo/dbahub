from Crypto.PublicKey import RSA

################################################pycypto 不建议再使用；使用pycryptodome代替
"""
openssl genrsa -out mykey.pem                  #私钥

openssl rsa -in mykey.pem -pubout > mykey.pub  #公钥

"""

text="this is original text"

pub_key=RSA.importKey(open('mykey.pub'))     #使用公钥加密
en_str=pub_key.encrypt(text)
#en_str=pub_key.encrypt(text,1234)          #随机数不影响

pri_key=RSA.importKey(open('mykey.pem'))     #使用私钥解密
de_str=pri_key.decrypt(en_str[0])


############pycryptodome
"""
The Public-Key Cryptography Standards (PKCS)
公钥密码学标准，
包括证书申请、证书更新、证书作废表发布、扩展证书内容以及数字签名、数字信封的格式
等方面的一系列相关协议。
PKCS#1 ... PKCS#15
"""
