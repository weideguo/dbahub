########################################################################
# 大文件时防止出现内存不够用 分块读取


import hashlib

def hash_bytestr_iter(bytesiter, hasher=hashlib.md5(), hex_str=True):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if hex_str else hasher.digest())

def file_block_iter(filename, blocksize=65536):
    with open(filename, "rb") as afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


      
hash_bytestr_iter(file_block_iter("/root/ansible-2.7.4.zip"))  
    
    
    
######################################################################
# simple demo    
        
    
import hashlib   

src=u"askakirfkjhrzf这个"
m2 = hashlib.md5()   
m2.update(src.encode('utf-8'))      #unicode->utf8
print m2.hexdigest()
