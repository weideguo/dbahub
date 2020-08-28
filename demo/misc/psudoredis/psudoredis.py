# -*- coding: utf-8 -*-

import sys
import os
import signal
import json
import time
import copy
from threading import Thread
import multiprocessing as mp

publish_prefix="__publish__"

def unicode_convert(json):
    """python2 unicode json to str json"""
    if isinstance(json, dict):
        return {unicode_convert(key): unicode_convert(value) for key, value in json.iteritems()}
    elif isinstance(json, list):
        return [unicode_convert(element) for element in json]
    elif isinstance(json, unicode):
        return json.encode("utf-8")


def wildmatch(p, s):
    """
    "*" "?" as wildcard
    "\*" "\?" not support 
    """
    l=[]
    for i in range(len(p)+1):
        l.append([0]*(len(s)+1))
    l[0][0]=1
    for a in range(1,len(p)+1):
        if p[a-1]=="*":
            l[a][0]=l[a-1][0]
        for b in range(1,len(s)+1):
            if p[a-1]=="*":                
                l[a][b]=l[a-1][b] or l[a][b-1]
            elif p[a-1]=="?"or p[a-1]==s[b-1]:
                l[a][b]=l[a-1][b-1]
            else:
                l[a][b]=0
    return l[-1][-1]!=0    
    
    
    
def Singleton(cls):
    """
    @Singleton
    class A():pass
    """
    _instance_lock = mp.Lock()
    _instance = {}
        
    def _singleton(*args, **kargs):
        if cls not in _instance:
            with _instance_lock:
                if cls not in _instance:
                    _instance[cls] = cls(*args, **kargs)
        return _instance[cls]
    
    return _singleton
        
    
@Singleton
class PsudoRedis(object):
    
    base_dir=os.path.dirname(os.path.abspath(__file__))
    response_error = TypeError("WRONGTYPE Operation against a name holding the wrong kind of value")
    dthread = None
    
    def __init__(self, location="test.db", auto_dump=True, sig=True, *args, **kwargs):
        """
        psudo redis database
        support multi process and thread
        """
        self.db=mp.Manager().dict() 
        
        self.load(location, auto_dump)
        if sig:
            self.set_sigterm_handler()

    
    @property
    def data(self):
        return self.db.copy()
    
    
    def set_sigterm_handler(self):
        """wait dump complete when kill"""
        def sigterm_handler():
            if self.dthread is not None:
                self.dthread.join()
            sys.exit(0)
        signal.signal(signal.SIGTERM, sigterm_handler)

    
    def load(self, location, auto_dump):
        """load json file as db"""
        #location = os.path.expanduser(location)
        base_dir=os.path.join(self.base_dir, location)
        self.db_file = location
        self.auto_dump = auto_dump
        if os.path.exists(location):
            self.__load()
        return True

    
    def dump(self):
        """dump db to json file"""
        self.dthread = Thread(target=json.dump, args=(self.db.copy(), open(self.db_file, "w")))
        self.dthread.start()
        self.dthread.join()
        return True

    
    def __load(self):
        """Load or reload the json info from the file"""
        try:
            _db=json.load(open(self.db_file, "r"))
            self.db.update(_db)
            if sys.version_info<(3,0):
                self.db.update(unicode_convert(_db))
        except ValueError:
            if os.stat(self.db_file).st_size != 0: 
                raise Exception("load file failed")

    
    def __autodump(self):
        """Write/save the json dump into the file if auto_dump is enabled"""
        if self.auto_dump:
            self.dump()

    
    #use as a redis client
    def ping(self):
        return True
             
             
    def keys(self, pattern="*"):
        """like redis keys but not suport [] \* \?"""
        _k=[]
        for k in self.db.keys():
            if wildmatch(pattern,k):
                _k.append(k)
        
        return _k
        

    def exists(self, name):
        return 1 if name in self.db and self.db[name] else 0

    
    def delete(self, name):
        if not name in self.db: 
            return 0
        del self.db[name]
        self.__autodump()
        return 1
    
    
    def expire(self,name,sec):
        if not name in self.db: 
            return False
        #del self.db[name]
        return True

    
    def type(self, name):
        if isinstance(self.db[name],str):
            return "string"
        if isinstance(self.db[name],list):
            return "list"    
        if isinstance(self.db[name],dict):
            return "hash"    
        if isinstance(self.db[name],tuple):
            return "set"  
        else:
            raise self.response_error
        
        
    def flushdb(self,asynchronous=False):
        self.db.clear()
        self.__autodump()
        return True
    
    
    def flushall(self,asynchronous=False):
        self.db.clear()
        self.__autodump()
        return True
    
    
    # str
    def set(self, name, value):
        self.db[name] = value
        self.__autodump()
        return True

    
    def get(self, name):
        if isinstance(self.db[name], str):
            return self.db[name]
        raise self.response_error
        
        
    #lish
    def lrem(self, name, count, element):
        _count=0
        _list=copy.deepcopy(self.db[name])
        for k in _list:
            if k==element and (_count<count or not count):
                i = self.db[name].index(k)
                _l=self.db[name]
                del _l[i]
                self.db[name]=_l
                _count +=1
        self.__autodump()      
        return _count
    
    
    def blpop(self, name, timeout=0):
        duration=0
        while (not timeout or duration<timeout) and (not name in self.db or len(self.db[name]) == 0):
            time.sleep(0.1)
            duration += 0.1
        
        if not name in self.db or len(self.db[name]) == 0:
            return None
        else:
       
            return (name,self.lpop(name))
        
    
    def lpop(self, name):
        pos=0
        value = self.db[name][pos]
        _l=self.db[name]
        del _l[pos]
        self.db[name]=_l
        self.__autodump()
        return value

    
    def rpush(self, name, element):
        if not name in self.db:
            self.db[name] = []
        _l=self.db[name]
        _l.append(element)
        self.db[name] = _l
        self.__autodump()
        return True
    
    
    def lrange(self, name, start, end):
        if end == -1:
            end=None
        else:
            end=1+end
            
        if isinstance(self.db[name],list):
            return self.db[name][start:end]
        else:
            raise self.response_error
    
    
    def llen(self, name): 
        if isinstance(self.db[name],list):
            return len(self.db[name])
        else:
            raise self.response_error
    
    #hash
    def hmset(self, name, mapping):  
        for k in mapping.keys():
            self.hset(name,k,mapping[k])
        
        return True
    
        
    def hset(self, name, field, value):
        if not name in self.db:
            self.db[name] = {}
            
        _d=self.db[name]
        _d.update({field: value})
        self.db[name]=_d
        self.__autodump()
        return 1
        
        
    def hgetall(self, name):
        if isinstance(self.db[name], dict):
            return self.db[name]
        else:
            raise self.response_error
     
    def hget(self, name, field):
        return self.db[name][field]

    
    #publish/subscribe
    def publish(self, channel, message):
        #self.rpush(publish_prefix+channel, message)
        return 1
        
            
    def pubsub(self):
        s=Subscribe(self.db)
        return s



class Subscribe(object):
    def __init__(self,db):
        self.db=db

    def psubscribe(self,channel):
        self.channel = channel 


    def listen(self):
        return True
    
    
    def parse_response(self, block=True, timeout=0):
        time.sleep(1)
        return ["pmessage","test_channel","test_channel","test_message"]
        """
        data=self.db.copy()
        publish_key=publish_prefix+self.channel
        
        if block:
            duration=0
            if (not timeout or duration<timeout) and (not publish_key in data or not data[publish_key]):
                time.sleep(0.1)
                duration += 0.1

        if publish_key in data and data[publish_key]:
            _p=data[publish_key]
            message=_p.pop(0)
            self.db[publish_key]=_p
            
            return ["pmessage",self.channel,self.channel,message]
            
        else:
            return None
        """
