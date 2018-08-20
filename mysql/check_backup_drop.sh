#!/bin/bash
#check backup and drop database list
# list
# 10.0.0.1:3306:database_name1 

dirpath=$(cd "$(dirname "$0")";pwd)
cd ${dirpath}

user='root'
passwd='root_password'

check(){
    for list in `cat list`
    do
        ip=`echo ${list}| awk -F : '{print $1}'`
        port=`echo ${list}| awk -F : '{print $2}'`
        db=`echo ${list}| awk -F : '{print $3}'`
        num=`mysql -u${user} -p${passwd} -h${ip} -P${port} -e "show processlist" | grep -w ${db} | grep -v "root" | wc -l`
        
        if [ ${num} -eq 0 ]
        then
            echo -e "${list} \e[1;33m idle \e[0m"
        else
            echo -e "${list} \e[1;31m busy \e[0m"
        fi		 
    done
}

check_db(){
    for list in `cat list`
    do
        ip=`echo ${list}| awk -F : '{print $1}'`
        port=`echo ${list}| awk -F : '{print $2}'`
        db=`echo ${list}| awk -F : '{print $3}'`
                
        num=`mysql -u${user} -p${passwd} -h${ip} -P${port}  -e "show databases" | grep -w ${db}  | wc -l`
    
        if [ ${num} -eq 0 ]
        then
            echo -e "${list} \e[1;33m not exist \e[0m"
        else
            echo -e "${list} \e[1;31m exist \e[0m"
        fi		 
    done
}

drop(){
    for list in `cat list`
    do
        ip=`echo ${list}| awk -F : '{print $1}'`
        port=`echo ${list}| awk -F : '{print $2}'`
        db=`echo ${list}| awk -F : '{print $3}'`
        echo -e "${list}  \e[1;33m begin dropping  \e[0m"
        #echo "mysql -u${user} -p${passwd} -h${ip} -P${port} drop database ${db}"
        mysql -u${user} -p${passwd} -h${ip} -P${port} -e "drop database ${db}"
    
        if [ $? -eq 0 ];then
            echo -e "${list} drop----------------------------------------\e[1;33m done \e[0m"
        else
            echo -e "${list} drop----------------------------------------\e[1;31m error \e[0m"
        fi	
        sleep 2	
    done
    echo "drop completed"
}

backup_single(){
    if [ ! -d ${1}_${2} ];then
        mkdir ${1}_${2}
    fi
    mysqldump -u${user} -p${passwd} -h${1} -P${2} -R ${3} > ${1}_${2}/${3}.sql
    #echo "mysqldump -u${user} -p${passwd} -h${1} -P${2} -R ${3} > ${1}_${2}/${3}.sql"
    sleep 1
    
    if [ $? -eq 0 ];then
        echo -e "${list} backup----------------------------------------\e[1;33m done \e[0m"
    else
        echo -e "${list} backup----------------------------------------\e[1;31m error \e[0m"
    fi
}

backup(){
    v_thread=5
    v_fifofile="/tmp/$$.fifo"
    mkfifo -m 700 ${v_fifofile}
    exec 600<>${v_fifofile}
    rm -rf ${v_fifofile}
    
    for ((k=1;k<=${v_thread};k++));do
        echo >&600
    done	
    
    for list in `cat list`
    do	
        read -u600
        {
                ip=`echo ${list}| awk -F : '{print $1}'`
                port=`echo ${list}| awk -F : '{print $2}'`
                db=`echo ${list}| awk -F : '{print $3}'`
                echo -e "${ip}:${port}  \e[1;33m ${db} \e[0m"
                #echo "mysqldump -u${user} -p${passwd} -h${ip} -P${port} backup database ${db}"
                backup_single ${ip} ${port} ${db} 
        echo >&600
        }&
    done
    
    wait
    
    exec 600>&-
    exec 600<&-
    
    echo "backup completed"
}

case "$1" in
    'check')
        check
        ;;
    'backup')
        backup
        ;;
    'drop')
        drop
        ;;
    'check_db')
        check_db 
        ;;
	*)
        echo "$0 check|backup|drop|check_db"
        exit 1
        ;;
esac
