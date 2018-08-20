#!/bin/sh
#by weideguo
cd $(dirname $0)
# process_list
# 6379|/data/redis/redis-server /data/redis/redis.conf

cat process_list | while read line
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
