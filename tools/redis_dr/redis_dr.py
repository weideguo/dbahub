#!/bin/env python
#coding:utf8

"""
redis dump and restore
work if redis server has [dump] and [restore] command (Available since 2.6.0)
dump file not suppose to readable
by wdg@dba in 20190123
"""
import re
import time
import redis
from traceback import print_exc


line_split_flag="  "            #key's name should not have substring like line_split_flag+".*?"+line_split_flag
absolute_time_tag="#"           #tag for absolute time
default_dump_file="./redis.dump"


def get_redis_client(host='127.0.0.1',port=6379,db=0,password=None):
    print host,port,db,password
    return redis.StrictRedis(host=host,port=port,db=db,password=password)


def dumps(redis_client,absolute):
    for k in redis_client.keys():
        v=redis_client.dump(k)
        t=redis_client.ttl(k)
        if t==-1:
            t=0
        if absolute:
            t=absolute_time_tag+str(time.time()+t)
        if v==None:
            pass
        else:
            k=k.replace("\n","\\\\r")
            v=v.replace("\n","\\\\r")      #dump string may contain '\n',convert it
            l="%s%s%s%s%s\n" % (k,line_split_flag,t,line_split_flag,v)
            yield l

 
def dump(f="/tmp/redis.dump",redis_client=None,absolute=False):       

    fw=open(f,"wb")
    fw.close()             #clear old file

    counter = 0
    for l in dumps(redis_client,absolute):
        if not counter:
            fw=open(f,"ab")
        fw.write(l)
        counter = (counter + 1) % 10000
        if not counter:
            fw.close()
    if counter:
        fw.close()    


def restores(f):
    f=open(f,"rb")
    l=f.readline()
    while l:
        yield l
        l=f.readline()        

    f.close()


def restore(f,redis_client=None,replace=False):
    counter = 0
    for l in restores(f):
        try:
            new_split_pattern="%s.*?%s" % (line_split_flag,line_split_flag)
            new_split_str=re.findall(new_split_pattern,l)[0]
           
            k=l.split(new_split_str)[0]
            t=new_split_str.strip(line_split_flag)
            #print [k,t]
            v=l.lstrip("%s%s%s%s" % (k,line_split_flag,t,line_split_flag)).rstrip("\n")

            if re.search(absolute_time_tag+".*",t):
                t=t.lstrip(absolute_time_tag)
                t=float(t)-time.time()

            t=int(t)
            if t<0:
                t=0
            t=t*1000
       
            v=v.replace("\\\\r","\n")                           #reconvert 
            k=k.replace("\\\\r","\n")
            if not counter:
                p = redis_client.pipeline(transaction=False)              
            #print [k,t,v] 
            p.restore(k,t,v,replace)
            counter = (counter + 1) % 10000
            if not counter:
                p.execute()

        except:
            print_exc()            
            raise Exception("error in [%s,%s,%s]" % (k,t,v))
    

    if counter:
        p.execute()

 
def main(parser):

    options, args = parser.parse_args()
    
    if len(args)!=1:
        parser.print_help()
        exit(4)
    
    action=args[0]

    def options_to_kwargs(options):
        args={}
        if options.host:
            args["host"] = options.host
        if options.port:
            args["port"] = int(options.port)
        if options.password:
            args["password"] = options.password
        if options.db:
            args["db"] = int(options.db)
        return args
    
    kwargs=options_to_kwargs(options)

    if options.file:
        f=options.file
    else:
        f=default_dump_file
    print f

    if options.absolute=="True" or options.absolute=="true":
        absolute=True
    else:
        absolute=False
    
    if options.replace=="True" or options.replace=="true":
        replace=True
    else:
        replace=False

    if action=="dump":
        r=get_redis_client(**kwargs)
        dump(f,r,absolute)

    elif action=="restore":
        r1=get_redis_client(**kwargs)
        restore(f,r1,replace)

    else:
        parser.print_help()
        

if __name__=="__main__":
    import optparse
    usage = "Usage: %prog dump|restore [options]"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-H", "--host", help="Server hostname (default: 127.0.0.1).")
    parser.add_option("-p", "--port", help="Server port (default: 6379).") 
    parser.add_option("-n", "--db",   help="Database number. (default: 0)")
    parser.add_option("-a", "--password", help="Password to use when connecting to the server.(default: None)")
    parser.add_option("-f", "--file", help="File for output or input.(default: ./redis.dump)")    
    parser.add_option("-b","--absolute",help="Dump key use absolute time for expire.(default: false. true|false)")
    parser.add_option("-r","--replace",help="replace key if exist.(default: false. true|false)")

    main(parser)

    
