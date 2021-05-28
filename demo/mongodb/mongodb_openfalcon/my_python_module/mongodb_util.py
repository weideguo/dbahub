import base64
import pymongo

def get_mongodb_status():
    try:
        #import urllib
        #urllib.quote('my_passwd')   #有特殊字符的要先编码
        #base64.b64encode('mongodb://admin:my_passwd@127.0.0.1:27017/admin')
        #将uri使用base64编码 尽量拆分成小字符串
        b='yyy'
        b+='xxx' 
        b+='9kYjo'        
        client=pymongo.MongoClient(base64.b64decode(b) , serverSelectionTimeoutMS=3000)
        loop_dict=client.admin.command('serverStatus')
        return loop_dict
    except:
        return {}
