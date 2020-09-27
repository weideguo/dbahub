#!/bin/sh
#by weideguo

#通过配置文件由端口检查服务是都存在，不存在则启动

# process_list
# 6379|/data/redis/redis-server /data/redis/redis.conf

cd $(dirname $0)
config_file="process_list"

cat ${config_file} | while read line
do
    port=`echo $line | cut -d "|" -f 1`
    startup_command=`echo $line | cut -d "|" -f 2`
    
    nc -v -w 2 -z 127.0.0.1 ${port}
    
    if [ $? != "0" ];then
        echo "[ `date "+%Y-%m-%d %H:%M:%S"` ] port ${port} is shutdown"
        eval ${startup_command}
    else   
        echo "[ `date "+%Y-%m-%d %H:%M:%S"` ] port ${port} is on"
    fi
done
