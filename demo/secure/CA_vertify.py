##CA证书的验证

##离线验证
import OpenSSL
f=open('./ca.crt','r')
x=OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM,f.read())
x.get_subject()
x.get_issuer()




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
