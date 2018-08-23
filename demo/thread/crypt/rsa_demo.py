from Crypto.PublicKey import RSA


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
