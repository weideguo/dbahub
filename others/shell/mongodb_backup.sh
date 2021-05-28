#!/bin/bash

source  ~/.bash_profile 

mongodb_uri='mongodb://admin:my_passwd@127.0.0.1:27017'
auth_db="admin"

backup_path="/data/dbbak"
date_str=`date '+%Y%m%d_%H%M%S'`
backup_file="sdk_mongodb_${date_str}"
oplog_backup_file="sdk_mongodb_oplog_${date_str}"

mongodump --uri ${mongodb_uri} --authenticationDatabase=${auth_db} --oplog -o ${backup_path}/${backup_file}


# 备份oplog开始时间 稍微多于备份间隔，确保oplog数据都备份
let begin_timestamp=`date +%s`-90000 
mongodump --uri ${mongodb_uri} --authenticationDatabase=${auth_db} -d local -c 'oplog.rs' -q '{"ts":{"$gt": {"$timestamp":{"t":'${begin_timestamp}', "i":1}}}}' -o ${backup_path}/${oplog_backup_file}

cd ${backup_path} && tar -zcf ${backup_file}.tar.gz ${backup_file} --remove-files
cd ${backup_path} && tar -zcf ${oplog_backup_file}.tar.gz ${oplog_backup_file} --remove-files

remain_day=10
find "${backup_path}" -maxdepth 1  -name "sdk_mongodb_*.tar.gz" -mtime +"${remain_day}" -follow -exec rm -f {} \;

