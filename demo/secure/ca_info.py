##CA证书的验证

##离线验证
from binascii  import hexlify
import OpenSSL

f=open("server.crt")
cert=OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,f.read())
cert.get_subject()
cert.get_issuer()
#有效期
cert.get_notBefore()
cert.get_notAfter()

#cryptCert = cert.to_cryptography()
#print hexlify(cryptCert.signature)

#python3
#从证书从获取公钥
OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8")



#从证书从获取公钥
#python2 python3
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

cert_str=open("server.crt").read()

cert_obj = load_pem_x509_certificate(str.encode(cert_str), default_backend())
public_key = cert_obj.public_key()

from cryptography.hazmat.primitives import serialization
public_key.public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo)


"""
从证书从提取公钥
openssl x509 -outform PEM -in server.crt -pubkey -out server.pubkey
"""


#在线验证
import ssl, socket

hostname = 'www.google.com'
ctx = ssl.create_default_context()
s = ctx.wrap_socket(socket.socket(), server_hostname=hostname)
s.connect((hostname, 443))
cert = s.getpeercert()

subject = dict(x[0] for x in cert['subject'])
issued_to = subject['commonName']
issuer = dict(x[0] for x in cert['issuer'])
issued_by = issuer['commonName']
