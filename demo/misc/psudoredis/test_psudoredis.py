# -*- coding: utf-8 -*-
import time
from threading import Thread
from multiprocessing import Process

from psudoredis import PsudoRedis


class TestClass(object):
    r=PsudoRedis()

    def test_singleton(self):
        r2=PsudoRedis()
        assert self.r == r2

    def test_ping(self):
        assert self.r.ping()

    def test_set_get_delete(self):
        assert self.r.set("a","aaa")
        assert self.r.get("a") == "aaa"
        assert self.r.delete("a") == 1
        self.r.db.clear()
        
    def test_keys_flushall(self):
        self.r.db["a"]="aaa"
        self.r.db["ab"]="aaa"
        self.r.db["abc"]="aaa"
        self.r.db["adc"]="aaa"
        assert len(self.r.keys("a*c"))==2
        assert self.r.flushall()
        self.r.db.clear()
        
    def test_flushdb(self):
        self.r.db["adc"]="aaa"
        assert self.r.flushdb()
        self.r.db.clear()
    
    def test_exists(self):
        self.r.db["a"]="aaa"
        assert self.r.exists("a") == 1
        self.r.db["a"]=""
        assert self.r.exists("a") == 0
        self.r.db.clear()

    def test_expire(self):        
        self.r.set("a","aaa")
        assert self.r.expire("a",100)
        assert not self.r.expire("aaa",100)
        self.r.db.clear()
     
    def test_type(self):
        self.r.db["a"]="aaa"
        assert self.r.type("a") == "string"
        self.r.db["a"]=["a","b"]
        assert self.r.type("a") == "list"
        self.r.db["a"]={}
        assert self.r.type("a") == "hash"
        self.r.db["a"]=()
        assert self.r.type("a") == "set"
        self.r.db.clear()
    
    def test_data(self):
        self.r.db.clear()
        self.r.db["a"]="aaa"
        assert self.r.data=={"a":"aaa"}
        self.r.db.clear()
        
    def test_rpush(self):
        assert self.r.rpush("a","aa")
        assert self.r.rpush("a","bb")
        assert self.r.lrange("a",0,-1)==["aa","bb"]
        assert self.r.lrange("a",0,-2)==["aa"]
        self.r.db.clear()
    
    def test_lrange_llen_lpop_lrem(self):
        self.r.db["a"]=["xx","aa","bb","cc","aa","dd","aa","ee"]
        assert self.r.lrange("a",2,4) == ['bb', 'cc', "aa"]
        assert self.r.llen("a") == 8
        assert self.r.lpop("a") == "xx"
        assert self.r.lrem("a",2,"aa") == 2
        self.r.db.clear()
    

    def test_blpop(self):
        self.r.db["a"]=["xx"]
        assert self.r.blpop("a") == ("a","xx")
        assert not self.r.blpop("a",1) 
        self.r.db.clear()
        
    def test_blpop_process(self):
        def f(k):
            r1=PsudoRedis('test.db',True) 
            for i in range(2):
                time.sleep(3)
                r1.rpush(k,"a")
        
        #Thread(target=f, args=('kkk',)).start() 
        Process(target=f, args=('kkk',)).start() 
              
        assert self.r.blpop('kkk',4)
        assert not self.r.blpop('kkk',1) 
        assert self.r.blpop('kkk')
    
    def test_blpop_thread(self):
        def f(k):
            r1=PsudoRedis('test.db',True) 
            for i in range(2):
                time.sleep(3)
                r1.rpush(k,"a")
        
        Thread(target=f, args=('kkk',)).start() 
              
        assert self.r.blpop('kkk',4)
        assert not self.r.blpop('kkk',1) 
        assert self.r.blpop('kkk')        
        
    def test_hmset_hgetall(self):  
        a={"a":"aa","b":"bb"}
        self.r.db["a"]=a
        assert self.r.hgetall("a")==a
        self.r.db.clear()
    
    def test_hset_hget(self):
        assert self.r.hset("a","a","aa")
        assert self.r.hset("a","b","bb")
        assert self.r.hget("a","a") == "aa" 
        assert self.r.hget("a","b") == "bb" 
        self.r.db.clear()

    def test_publish(self):
        assert self.r.publish("mychannel","mymessage")

    def test_subscribe(self):
        s=self.r.pubsub()
        s.psubscribe("mychannel")
        s.listen()
        assert s.parse_response(block=True)


if __name__ == "__main__":
    tests = TestClass()
    test_methods = [method for method in dir(tests) if callable(getattr(tests, method)) if method.startswith("test_")]
    for method in test_methods:
        getattr(tests, method)() 
        print(method)
