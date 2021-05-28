#!/bin/env pytyhon
# -*- coding: utf-8 -*-
#
#在DB2获取恢复DB1的sql文件以及开始的binlog、position 
#        
import os
import re
import sys
import time
import logging


log = logging.getLogger()
handler = logging.StreamHandler(sys.stdout) 
fmt = logging.Formatter("%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
handler.setFormatter(fmt)
log.addHandler(handler)
log.setLevel(logging.DEBUG)



def list_path(root_path):
    """
    列出路径下的文件、目录
    """
    files=[]
    dirs=[]
    for x in os.listdir(root_path):
        if os.path.isfile(os.path.join(root_path,x)):
            files.append(x)
        else:
            dirs.append(x)
    
    return files,dirs


def get_name_match_files(pattern, files):
    """
    从文件列表中获取名字匹配的文件列表
    """
    new_files=[]
    for f in files:
        if re.match(pattern,f):
            new_files.append(f)
    
    return new_files


def get_match_before_file(match_time, files, backup_time=""):
    """
    获取创建时间在匹配时间之前 且距离时间最短的文件 给的文件列表为绝对路径 返回绝对路径
    """
    last_ctime=0
    match_file=""
    for f in files:
        if backup_time:
            #确定备份时间时不用文件的创建时间判断
            #如3点时断开主从全实例逐库备份，则认为在3点对该库备份
            f_ctime=time.strftime("%Y-%m-%d",time.localtime(os.stat(f).st_ctime))+" "+backup_time
        else:
            f_ctime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(f).st_ctime))
        if f_ctime <= match_time and f_ctime>last_ctime:
            match_file=f
            last_ctime=f_ctime
   
    backup_date = time.strftime("%Y%m%d",time.localtime(os.stat(match_file).st_ctime)) 
    return match_file,backup_date



def get_master_status(status_file):
    """
    从show slave status\G信息中获取 Master_Log_File Exec_Master_Log_Pos:
    """
    tag_list=["Master_Host","Master_Log_File","Exec_Master_Log_Pos"]
    master_info={}
    
    with open(status_file,"r") as f:
        status_str=f.read()
        
        for l in status_str.split("\n"):
            for t in tag_list:
                pattern= "(?<=%s:).*" % t
                
                m=re.search(pattern, l)
                if m:
                    master_info[t]= m.group().strip()   

    return master_info[tag_list[0]],master_info[tag_list[1]],master_info[tag_list[2]]


if __name__ == "__main__":
    log.setLevel(logging.INFO) 
    #log.setLevel(logging.DEBUG)                         #调试时可以使用该模式，但不要在脚本正式使用时使用以免影响输出 
    
    if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help" or len(sys.argv)!=3:
        print("USAGE: %s <recovery_date> <database_name>" % sys.argv[0])
        sys.exit(1)

    recovery_date=sys.argv[1]
    database=sys.argv[2]

    #recovery_date="2020-09-02 05:20:00"
    #database="db_strategy_saesp_1281"    

    """
    请根据实际目录存放更改以下信息
    """     
    sql_dir="/data/dbbak"                                 #备份的sql文件存放的目录
    slave_status_dir="/data/server_tools/dbbackup"        #备份时关闭主从, show slave status\G导出到的文件的目录
                                                          #即如文件 slave_status_20200903.txt 所在的目录

    sql_file_pattern=".*"+database+".*sql.gz" 

    log.debug("sql_file_pattern: "+sql_file_pattern)

    sql_files=get_name_match_files(sql_file_pattern,list_path(sql_dir)[0])

    full_sql_files=[os.path.join(sql_dir,xi) for xi in sql_files]
    log.debug(full_sql_files)
    
    #每天凌晨3点备份
    match_sql_file, backup_date = get_match_before_file(recovery_date, full_sql_files, "03:00:00")
    log.debug("match_sql_file: %s, backup_date: %s " % (match_sql_file, backup_date))
    
    #时间格式如 20200904
    #backup_date=match_sql_file.split("_")[-2]

    status_file=os.path.join(slave_status_dir,"slave_status_%s.txt" % backup_date)
    log.debug("status_file: "+status_file)

    master_host,binlog,pos = get_master_status(status_file)

    log.debug("master_host,binlog,pos: %s %s %s" % (master_host,binlog,pos))
    
    print("%s:::%s:::%s:::%s" % (match_sql_file,master_host,binlog,pos))




    
