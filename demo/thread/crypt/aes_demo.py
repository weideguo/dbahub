from Crypto.Cipher import AES
import base64



key="qwertyuiopasdfgh"    #加密时使用的key，只能是长度16,24和32的字符串 #大小写敏感

def aes_encrypt(data,key):  
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    cipher = AES.new(key)
    encrypted = cipher.encrypt(pad(data))  #aes加密
    result = base64.b64encode(encrypted)  #base64 encode
    return result

def aes_decrypt(en_data,key):
    unpad = lambda s : s[0:-ord(s[-1])]
    cipher = AES.new(key)
    result2 = base64.b64decode(data)
    decrypted = unpad(cipher.decrypt(result2))
    return  decrypted

