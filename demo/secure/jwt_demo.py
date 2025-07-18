"""
pip install PyJWT
"""

from jwt import jwt, jws
 
"""
jwt json web tokens
服务端仅需要解析这个token，来判别客户端的身份和合法性，不需要存储。

签名串组成
header.payload.signature

header      #base64编码  类型和使用的哈希算法
payload     #base64编码  需要传输的信息，不要在此放入敏感的信息
signature   #签名串

"""  
 
secret_key = "my-secret-key-long-long-key-name"

# 不要将敏感信息存放于此
payload = {"user": "xxx", "expire":1800000000}    
 

# 生成签名串
encoded = jwt.encode(payload, secret_key, algorithm="HS256")

# 获取明文信息
jwt.decode(encoded, secret_key, algorithms=["HS256"])

"""
HS256
RS256
ES256
PS256
EdDSA
"""

