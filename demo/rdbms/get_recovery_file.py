#!/bin/env python
# -*- coding: utf-8 -*-
#
# 用于从给定目录获取回滚mysql的文件信息，即列出回滚使用的备份sql文件+binlog文件，备份文件以及binlog需要在同一主机上
# 备份文件名字带有完整库名，备份时加 --master-data=2   
# binlog文件的命名格式如  binlog-file-prefix.123456
# by weideugo in 20200730
#

import os
import re
import sys
import time
import subprocess
import logging


log = logging.getLogger()
handler = logging.StreamHandler(sys.stdout) 
fmt = logging.Formatter("%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
handler.setFormatter(fmt)
log.addHandler(handler)
log.setLevel(logging.DEBUG)


def cmd_exe(cmd):
    p = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return p.stdout.read().strip()


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


def get_match_before_file(match_time, files, backup_date=""):
    """
    获取创建时间在匹配时间之前 且距离时间最短的文件 给的文件列表为绝对路径 返回绝对路径
    """
    last_ctime=0
    match_file=""
    for f in files:
        if backup_date:
            #确定备份时间时不用文件的创建时间判断
            #如3点时断开主从全实例逐库备份，则认为在3点对该库备份
            f_ctime=time.strftime("%Y-%m-%d",time.localtime(os.stat(f).st_ctime))+" "+backup_date        
        else:
            f_ctime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(f).st_ctime))
        
        if f_ctime <= match_time and f_ctime>last_ctime:
            match_file=f
            last_ctime=f_ctime
    
    return match_file
    
   
# head -c 1000 abc.sql.gz | gzip -d 2>/dev/null | grep "CHANGE MASTER TO" | grep -oP "(?<=MASTER_LOG_FILE\=').*(?=')"   
def get_match_binlog_list(match_time, match_sql_file, binlog_cmd_pattern, pos_cmd_pattern, binlog_dir):  
    """
    由sql压缩文件获取备份信息从而确定需要的binlog列表 给的sql压缩文件为绝对路径
    """
    if not match_sql_file:
        log.debug("no validated match sql file")
        sys.exit(1)
        
    #cmd=''' head -c 2000 %s | gzip -d 2>/dev/null | grep "CHANGE MASTER TO" | grep -oP "(?<=MASTER_LOG_FILE\=').*(?=')" ''' % match_sql_file
    cmd=binlog_cmd_pattern % match_sql_file
    begin_binlog=cmd_exe(cmd)
    cmd1=pos_cmd_pattern % match_sql_file
    begin_pos=cmd_exe(cmd1)
    
    log.debug(cmd)
    log.debug(cmd1)
    
    binlog_pattern=".".join(begin_binlog.split(".")[:-1])+"\.\d+$"
    
    all_binlog=get_name_match_files(binlog_pattern, list_path(binlog_dir)[0])
    
    #重新排序
    all_binlog.sort()
    
    tmp_match_time=0
    
    #设置第一个binlog存在 否则可能出现第一个binlog被删除从而导致获取结果错误
    match_binlog=[begin_binlog]
    for b in all_binlog:
        if b > begin_binlog and (not tmp_match_time):
            #获取到第一个最后修改时间大于匹配时间的 之后的binlog不需要
            match_binlog.append(b)
            #最后修改时间
            b_mtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(os.path.join(binlog_dir,b)).st_mtime)) 
            if b_mtime > match_time:
                #print(match_time,b_mtime)
                tmp_match_time= b_mtime               
    
    return match_binlog,begin_pos

    
def check_binloglist(binlog_list, binlog_dir):
    """
    检查binlog列表是否逐渐递增，以及binlog文件是否存在（只用第一个binlog文件判断）
    """
    begin_binlog=binlog_list[0]
    if not os.path.isfile(os.path.join(binlog_dir,begin_binlog)):
        log.debug("not exist: "+os.path.join(binlog_dir,begin_binlog))
        sys.exit(1)
    
    a=begin_binlog
    for b in binlog_list[1:]:
        if (int(b.split(".")[-1]) - int(a.split(".")[-1])) == 1:
            a=b
        else:
            log.debug("error: %s %s" % (a,b))
            sys.exit(1)

         
if __name__ == "__main__":
    log.setLevel(logging.INFO) 
    #log.setLevel(logging.DEBUG)                         #调试时可以使用该模式，但不要在脚本正式使用时使用以免影响输出 

    if len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help" or len(sys.argv)!=3:
        print("USAGE: %s <recovery_date> <database_name>" % sys.argv[0])
        sys.exit(1)

    recovery_date=sys.argv[1]
    database=sys.argv[2]
    
    #recovery_date="2020-07-29 04:00:00"
    #database="db_log_fake_0001"

    
    """
    请根据实际目录存放更改以下信息
    """                                                  
    sql_dir="/data/dbbak"                                #备份的sql文件存放的目录
    binlog_dir="/data/mysqllog/binlog/"                  #binlog存放的目录
    
    sql_file_pattern=".*"+database+".*sql.gz"            #备份的sql文件的正则匹配（不需要过滤时间）
    #从备份文件获取 MASTER_LOG_FILE MASTER_LOG_POS 的值，即备份时加 --master-data=2 
    get_binlog_cmd_pattern=''' head -c 2000 %s | gzip -d 2>/dev/null | grep "CHANGE MASTER TO" | grep -oP "(?<=MASTER_LOG_FILE\=').*(?=')" '''         
    get_pos_cmd_pattern   =''' head -c 2000 %s | gzip -d 2>/dev/null | grep "CHANGE MASTER TO" | grep -oP "(?<=MASTER_LOG_POS\=).*(?=;)" '''  
    """
    其他不需要更改
    """
      
    
    log.debug("sql_file_pattern: "+sql_file_pattern)
    
    sql_files=get_name_match_files(sql_file_pattern,list_path(sql_dir)[0])
    
    full_sql_files=[os.path.join(sql_dir,xi) for xi in sql_files]
    log.debug(full_sql_files)
    
    #获取备份的sql
    match_sql_file=get_match_before_file(recovery_date, full_sql_files)
    log.debug("match_sql_file: "+match_sql_file)
    
    #获取binlog列表 以及开始的position
    match_binlog, begin_pos = get_match_binlog_list(recovery_date, match_sql_file, get_binlog_cmd_pattern, get_pos_cmd_pattern, binlog_dir)
    
    log.debug("--------------------------------------------")
    
    #检查binlog是否正确
    check_binloglist(match_binlog, binlog_dir):
        
    print(match_sql_file+":::"+begin_pos+":::"+" ".join(match_binlog))
        
        
        
        
        
        
    
