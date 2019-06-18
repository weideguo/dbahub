from jot import jwt, jws
 
"""
jwt json web tokens
服务端仅需要解析这个token，来判别客户端的身份和合法性，不需要存储。

签名串组成
header.payload.signature

header      #base64编码  类型和使用的哈希算法
payload     #base64编码  需要传输的信息，不要在此放入敏感的信息
signature   #签名串

"""  
 
secret_key='^z=xr3j)gipqyjsl)04+e$5zz&4d@l&+qko@&&5=dh^5+kblm3'
 
payload={'status': 'ready'} 
 
#生成签名串
signature = jwt.encode(payload, signer=jws.HmacSha(bits=128, key=secret_key))


#获取明文信息 以及校验
jwt.decode(signature, signers=[jws.HmacSha(bits=128, key=secret_key)])

