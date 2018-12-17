import struct
import hmac
import hashlib
import time
import base64


"""
HMAC-based One-Time
"""

def hotp(secret, counter):    
    basedSecret = base64.b32decode(secret, True)    
    structSecret = struct.pack(">Q", counter)    
    hmacSecret = hmac.new(basedSecret, structSecret, hashlib.sha1).digest()    
    ordSecret = ord(hmacSecret[19]) & 15    
    tokenSecret = (struct.unpack(">I", hmacSecret[ordSecret:ordSecret+4])[0] & 0x7fffffff) % 1000000    
    return tokenSecret
  

a=base64.b32encode("ssdsds")
b=int(time.time())
print hotp(a,b)

