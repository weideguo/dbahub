from Crypto.Cipher import AES
import base64

"""
Advanced Encryption Standard
对称加密算法
"""

key="qwertyuiopasdfgh"    #加密时使用的key，只能是长度16字节（16*8=128位）,24（24*8=192位）和32（32*8=256位）的字符串 #大小写敏感

def aes_encrypt(data,key):  
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)    #0-255（十进制）对应的扩展ascii码
    cipher = AES.new(key)
    encrypted = cipher.encrypt(pad(data))  #aes加密
    result = base64.b64encode(encrypted)   #base64 encode
    return result

def aes_decrypt(en_data,key):
    unpad = lambda s : s[0:-ord(s[-1])]     #ord 扩展ascii码的对应10进制数字（0-255）
    cipher = AES.new(key)
    result2 = base64.b64decode(en_data)
    decrypted = unpad(cipher.decrypt(result2))
    return  decrypted

