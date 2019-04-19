from OpenSSL.crypto import load_certificate, load_privatekey,FILETYPE_PEM
from OpenSSL.crypto import X509Store, X509StoreContext
from six import u, b, binary_type, PY3

ca_cert_pem=open('ca.crt','r').read()
intermediate_server_cert_pem=open('server.crt','r').read()

ca_cert = load_certificate(FILETYPE_PEM, ca_cert_pem)
intermediate_server_cert = load_certificate(FILETYPE_PEM, intermediate_server_cert_pem)
store = X509Store()
store.add_cert(ca_cert)
#store.add_cert(intermediate_cert)       #如果存在中间证书颁发机构
store_ctx = X509StoreContext(store, intermediate_server_cert)
print(store_ctx.verify_certificate())

'''
none 则认证成功
ca.crt     需要为权威的认证机构的证书 由此获取公钥
server.crt 为服务端的证书 由此获取 摘要 签名，签名通过公钥解密得到摘要，从而对比两个摘要以验证server.crt证书的合法性
'''
