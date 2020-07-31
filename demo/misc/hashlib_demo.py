#cofing:utf8

import hashlib

x=b"abc"

#sha256
hashlib.sha256(x).digest()

#转成字符串
import base64
base64.b64encode(hashlib.sha256(x).digest())

hashlib.sha256(x).hexdigest()



#MD5
hasher=hashlib.md5()
hasher.update(x)
hasher.hexdigest()




