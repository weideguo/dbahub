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
#coding:utf8
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256



class RsaCrypt(object):
    """
    RSA 加密/解密
    """

    def __init__(self):
        self.private_key, self.public_key = self.get_key()


    def get_key(self,key_len=2048):
        """
        生成公钥和私钥
        key_len 1024 / 2048 / 3072
        """
        key = RSA.generate(key_len)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        return private_key,public_key


    def encrypt(self,data):
        """
        加密
        传入byte格式
        """
        public_key = RSA.import_key(self.public_key)
        cipher = PKCS1_OAEP.new(public_key)
        en_data = cipher.encrypt(data)
        return en_data


    def decrypt(self,en_data):
        """
        解密
        返回byte格式
        """
        private_key = RSA.import_key(self.private_key)
        cipher = PKCS1_OAEP.new(private_key)
        data = cipher.decrypt(en_data)

        return data


    def sign(self,data):
        """
        签名
        """
        digest = SHA256.new(data)
        private_key=RSA.import_key(self.private_key)
        signature = pkcs1_15.new(private_key).sign(digest)
        return signature

    
    def verify(self,data,signature):
        """
        签名校验
        """
        digest = SHA256.new(data)
        public_key = RSA.import_key(self.public_key)
        try:
            pkcs1_15.new(public_key).verify(digest, signature)
            return True
        except:
            return False


if __name__ == "__main__":
    rc=RsaCrypt()
    print(rc.private_key,rc.public_key)
    data = b"123456"

    en_data=rc.encrypt(data)
    rc.decrypt(en_data)


    signature=rc.sign(data)
    rc.verify(data,signature)
