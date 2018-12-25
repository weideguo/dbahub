
# coding:utf8
            
import hashlib   

src=u"askakirfkjhrzf这个"
m2 = hashlib.md5()   
m2.update(src.encode('utf-8'))      #unicode->utf8
print m2.hexdigest()
