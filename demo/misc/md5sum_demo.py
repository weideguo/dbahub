########################################################################
# 大文件时防止出现内存不够用 分块读取


import hashlib

def hash_bytestr_iter(bytesiter, hasher, hex_str=True):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if hex_str else hasher.digest())

def file_block_iter(filename, blocksize=65536):
    with open(filename, "rb") as afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


def my_md5(filename=None,str=None):
    hasher=hashlib.md5()
    if filename:
        return hash_bytestr_iter(file_block_iter(filename),hasher)
    elif str:
        try:
            str=str.encode("utf8")
        except:
            str=str
        return hash_bytestr_iter([str],hasher)
    else:
        return None
      
          
hash_bytestr_iter(file_block_iter("/root/ansible-2.7.4.zip"),hashlib.md5())  
    
       
######################################################################
# simple demo    
        
    
import hashlib   

src=u"askakirfkjhrzf这个"
m2 = hashlib.md5()   
m2.update(src.encode('utf-8'))      #unicode->utf8
print m2.hexdigest()
