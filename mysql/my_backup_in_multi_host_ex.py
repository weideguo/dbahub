#!/bin/env python
# coding:utf8
#backup database in multi host
# by wdg@dba in 20180122

import threading
import Queue
import time
import random
import MySQLdb
import re
from traceback import format_exc
import os
import logging
import sys
from multiprocessing import Pool

db_list_file='/data/db_list'

db_ip="db_ip"
db_port="db_port"
db_user="db_user"
db_passwd="db_password"

#sql to get backup host
get_backup_host_sql='select distinct server_localip from db.server where server_name like "XYZ";'

get_database_list_sql="select distinct table_schema from information_schema.tables where table_schema not in('mysql','information_schema','performance_schema','test');"

host_user="host_user"
host_passwd="host_user_password"
remote_backup_dir="/data/remote_backup_dir"

rsync_user="rsync_user"
rsync_host="rsync_host"
rsync_port="rsync_port"
rsync_block="rsync_block"

Ymd=time.strftime('%Y%m%d',time.localtime())

log_file=os.path.join(sys.path[0],'mulit_host_backup.log')
logging.basicConfig(
        filename=log_file,
        level = logging.DEBUG,
        format = '[%(levelname)s] %(asctime)s %(message)s',
)

backgroup_thread_list=[]

def get_list_from_db(db_ip,db_port,db_user,db_passwd,sql,column_index=0):
    mylist=[] 
    conn = MySQLdb.connect(host=db_ip,port=db_port,user=db_user,passwd=db_passwd)
    cursor = conn.cursor()
    cursor.execute(sql)
    alldata = cursor.fetchall()
    for r_tuple in alldata:
        mylist.append(r_tuple[column_index])
    cursor.close()
    conn.close()
    return mylist

def exec_remote(host_passwd,host_user,host_name,cmd):
    remote_cmd="sshpass -p '%s' ssh %s@%s \"%s\""%(host_passwd,host_user,host_name,str(cmd))
    os.system(remote_cmd)

def rsync_file(host_passwd,host_user,host_name,rsync_cmd,rm_file_cmd):
    try:
        exec_remote(host_passwd,host_user,host_name,rsync_cmd)
        exec_remote(host_passwd,host_user,host_name,rm_file_cmd)
        logging.debug(rm_file_cmd)  
    except:
        logging.error("rsync failed--- %s"%rsync_cmd)
        logging.error(format_exc())

def backup_remote(remote_backp_path,backup_user,backup_passwd,slave_ip,slave_port,host_name,master_ip,master_port,queue):
    while True:
        try:
            database_name=queue.get()
            YmdHM=time.strftime('%Y%m%d%H%M',time.localtime())
            backup_file_name="%s/%s_%s.sql.gz"%(remote_backp_path,database_name,YmdHM)
            dump_cmd="mysqldump -u%s -p%s -h%s -P%s --routines --triggers --single-transaction --max_allowed_packet=251658240 --default-character-set=utf8 %s | gzip > %s"\
                         %(backup_user,backup_passwd,slave_ip,slave_port,database_name,backup_file_name)
            #cmd="sleep 3;echo 'hello' > %s" % backup_file_name
            
            exec_remote(host_passwd,host_user,host_name,dump_cmd)
            logging.info("Dump completed + %s_%s_%s"%(master_ip,str(master_port),str(database_name)))
        except:
            logging.error("Dump failed + %s_%s_%s"%(master_ip,str(master_port),str(database_name)))
            logging.error(format_exc())    
        finally:
            queue.task_done()

def backup_on_remote_host(slave_ip,slave_port,backup_user,backup_passwd,master_ip,master_port,host_name,database_list):
    
    remote_backp_home="%s/%s-%s" % (remote_backup_dir,master_ip,str(master_port))
    remote_backp_path="%s/%s-%s/%s" % (remote_backup_dir,master_ip,str(master_port),Ymd)
    mkdir_cmd="mkdir -p %s" % remote_backp_path
    exec_remote(host_passwd,host_user,host_name,mkdir_cmd)
    
    q_backup=Queue.Queue()
    backup_concurrent=3    

    for i in range(backup_concurrent):
        t_backup_remote=threading.Thread(target=backup_remote,args=(remote_backp_path,backup_user,backup_passwd,\
                                                              slave_ip,slave_port,host_name,master_ip,master_port,q_backup))
        t_backup_remote.setDaemon(True)
        t_backup_remote.start()
 
    for database_name in database_list:
        q_backup.put(database_name) 
    q_backup.join()

    rsync_cmd="rsync -azvrP %s rsync://%s@%s:%s/%s" % (remote_backp_home,rsync_user,rsync_host,rsync_port,rsync_block) 
    rm_file_cmd="rm -rf %s" % remote_backp_home
    t_rsync=threading.Thread(target=rsync_file, args=(host_passwd,host_user,host_name,rsync_cmd,rm_file_cmd))
    t_rsync.start()
    backgroup_thread_list.append(t_rsync)


def backup_func(q_db,q_host):
    while True:
        try:
            db_str=q_db.get()
            host_str=q_host.get()
            try:
                slave_ip=db_str.split('|')[0]
                slave_port=int(db_str.split('|')[1])
                backup_user=db_str.split('|')[2]
                backup_passwd=db_str.split('|')[3]
                master_ip=db_str.split('|')[4]
                master_port=int(db_str.split('|')[5])

                logging.info("------------------------[ %s %s ]-------begin"%(host_str,master_ip))

                 
                database_list=get_list_from_db(master_ip,master_port,backup_user,backup_passwd,get_database_list_sql) 
                
                backup_on_remote_host(slave_ip,slave_port,backup_user,backup_passwd,master_ip,master_port,host_str,database_list)

                logging.info("------------------------[ %s %s ]--------end"%(host_str,master_ip))
            
            except:
                logging.error(format_exc())
                q_db.put(db_str)
            finally:    
                q_host.put(host_str)
                q_db.task_done()
        except:
            logging.error(format_exc())
            

def main():
    
    q_db =  Queue.Queue()
    q_host = Queue.Queue()

    backup_host_list=get_list_from_db(db_ip,db_port,db_user,db_passwd,get_backup_host_sql)

    for host_str in backup_host_list:
        q_host.put(host_str)

    for i in backup_host_list:
        t_backup = threading.Thread(target=backup_func, args=(q_db,q_host))
        t_backup.setDaemon(True)
        t_backup.start()


    f=open(db_list_file,'r')
    db_list=f.readlines()
    f.close()
    db_list=map(lambda x:x.split('\n')[0],db_list)

    #delete list info like "#XXXXXXX" 
    tmp_db_list=[]
    for db_str in db_list:
        if not re.match('^#.*',db_str):
            tmp_db_list.append(db_str)
    db_list=tmp_db_list

    for db_str in db_list: 
        q_db.put(db_str)
        #block until all item in queue have been gotten
    q_db.join()
    
    for t in backgroup_thread_list:
        t.join()

if __name__=='__main__':
    main() 
