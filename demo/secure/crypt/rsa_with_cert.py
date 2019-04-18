#用证书加密、私钥文件解密
#用于消息传输
#私钥            server.key
#私钥生成的证书  server.crt
from M2Crypto import X509, RSA

def encrypt_with_certificate(message, cert_file):
    cert = X509.load_cert(cert_file)
    puk = cert.get_pubkey().get_rsa()                                       # get RSA for encryption
    message = base64.b64encode(message)
    encrypted = puk.public_encrypt(message, RSA.pkcs1_padding)
    return encrypted
    

print '加密串',encrypt_with_certificate('this is message','server.crt')



def decrypt_with_private_key(message, private_key_file):
    pk = RSA.load_key(private_key_file)                                              # load RSA for decryption
    decrypted = pk.private_decrypt(message, RSA.pkcs1_padding)
    decrypted = base64.b64decode(decrypted)
    return decrypted
    
    
print '解密串',decrypt_with_private_key(encrypted, 'server.key')
