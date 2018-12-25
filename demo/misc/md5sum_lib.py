#coding:utf8

# 大文件时防止出现内存不够用 分块读取

import hashlib

def hash_bytestr_iter(bytesiter, hasher, hex_str=True):
    for block in bytesiter:
        hasher.update(block)
    return (hasher.hexdigest() if hex_str else hasher.digest())

def file_block_iter(file=None, afile=None, blocksize=65536):
    if file:
        afile=open(file, "rb")
    else:
        afile=afile
            
    with afile:
        block = afile.read(blocksize)
        while len(block) > 0:
            yield block
            block = afile.read(blocksize)


def my_md5(file=None,str=None,afile=None):
    """
    file     文件全路径名
    str      字符串  unicode 或者utf8编码
    afile    open()方法打开的文件对象
    """
    hasher=hashlib.md5()
    if file:
        return hash_bytestr_iter(file_block_iter(file=file),hasher)
        
    elif afile:   
        return hash_bytestr_iter(file_block_iter(afile=afile),hasher)
        
    elif str:
        try:
            str=str.encode("utf8")
        except:
            str=str
        return hash_bytestr_iter([str],hasher)
    else:
        return None
      

if __name__="__main__":
      
    hash_bytestr_iter(file_block_iter("/root/ansible-2.7.4.zip"),hashlib.md5())  
       
    hash_bytestr_iter(file_block_iter(afile=open("/root/ansible-2.7.4.zip","rb")),hashlib.md5())      
    
    my_md5(file="/root/ansible-2.7.4.zip")
    my_md5(str="中文")
    my_md5(afile=open("/root/ansible-2.7.4.zip","rb"))
