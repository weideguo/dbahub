# coding:utf8
# 散列算法

            
import hashlib   

src=u"askakirfkjhrzf这个"
src=src.encode('utf-8')                   #unicode->utf8 byte  需要给函数传入byte类型

hash = hashlib.md5()   
hash.update(src)      
print(hash.hexdigest())



src=u"askakirfkjhrzf这个"
src=src.encode('utf-8')

hash = hashlib.sha1()   
hash.update(src)      
print(hash.hexdigest())





src1=u"askakirfkjhrzf"
src2=u"这个"
hash = hashlib.sha1()   
hash.update(src1.encode('utf-8'))        #字符串过长时可以拆分并多次调用update
hash.update(src2.encode('utf-8'))    
print(hash.hexdigest())






src = u"1231"
src=src.encode('utf-8')

hashlib.md5(src).hexdigest() 

hashlib.sha1(src).hexdigest() 
hashlib.sha256(src).hexdigest() 
hlib.sha384(src).hexdigest() 
hashlib.sha512(src).hexdigest() 


hashlib.md5(src).digest()           #返回byte类型 即原始的二进制格式





