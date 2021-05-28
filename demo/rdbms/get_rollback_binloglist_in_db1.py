#!/bin/env pytyhon
# -*- coding: utf-8 -*-
#
#在DB1获取恢复单个数据库所需的binlog列表
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


def get_match_binlog_list(recovery_date, begin_binlog, binlog_dir):
    binlog_pattern=".".join(begin_binlog.split(".")[:-1])+"\.\d+$"
    
    log.debug("binlog_dir: %s, binlog_pattern: %s" % (binlog_dir,binlog_pattern))    

    all_binlog=get_name_match_files(binlog_pattern, list_path(binlog_dir)[0])

    #重新排序
    all_binlog.sort()
    
    tmp_match_time=0

    #设置第一个binlog存在 否则可能出现第一个binlog被删除从而导致获取结果错误
    match_binlog=[begin_binlog]
    for b in all_binlog:
        if b == begin_binlog:
            #第一个binlog最后修改时间大于匹配时间 之后的binlog不再需要
            b_mtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(os.path.join(binlog_dir,b)).st_mtime)) 
            if b_mtime > recovery_date:
                log.debug("last_binlog_date: "+b_mtime)
                break
        if b > begin_binlog and (not tmp_match_time):
            #获取到第一个最后修改时间大于回滚时间的 之后的binlog不需要
            match_binlog.append(b)
            #最后修改时间
            b_mtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(os.stat(os.path.join(binlog_dir,b)).st_mtime)) 
            if b_mtime > recovery_date:
                log.debug("last_binlog_date: "+b_mtime)
                #print(match_time,b_mtime)
                tmp_match_time= b_mtime  
    
    return match_binlog



def check_binloglist(binlog_list,binlog_dir):
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
        print("USAGE: %s <begin_binlog> <recovery_date>" % sys.argv[0])
        sys.exit(1)	

    begin_binlog=sys.argv[1]
    recovery_date=sys.argv[2]
    
    #begin_binlog="binlog.216174"
    #recovery_date="2020-09-02 02:59:59"
    
    """
    请根据实际目录存放更改以下信息
    """  
    binlog_dir="/data/mysqllog/binlog/"                  #binlog存放的目录

    """
    其他不需要更改
    """
    match_binlog = get_match_binlog_list(recovery_date, begin_binlog, binlog_dir)
    log.debug(str(match_binlog))


    check_binloglist(match_binlog,binlog_dir)

    print(" ".join(match_binlog))
    


