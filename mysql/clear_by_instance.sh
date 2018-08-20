#/bin/sh 

cd $(dirname $0)
db_ip=$1
db_port=$2
method=$3
db_user='root'
db_password='root_password'

hint="<ip> <port> check|backup|drop|clear"
if [ X${method} = X ];then
    echo "$0 ${hint}"
    exit
fi

database_list=`mysql -u${db_user} -p${db_password} -h${db_ip} -P${db_port} -e "show databases" | egrep -v "(Database|information_schema|mysql|performance_schema|sys)"`

check(){
    all_num=0
    for db in $database_list
    do
        num=`mysql -u${db_user} -p${db_password} -h${db_ip} -P${db_port} -e "show processlist" | grep -w ${db} | wc -l`
        let all_num=all_num+num
    done
    
    if [ ${all_num} -eq 0 ];then
        echo -e "instance [ ${db_ip}:${db_port} ] is \e[1;33m idle \e[0m"
    else
        echo -e "instance [ ${db_ip}:${db_port} ] is \e[1;31m busy \e[0m"
    fi

}

mysql_backup(){
    db=$1
    echo "backup ${db} begin"
    backup_cmd="mysqldump -u${db_user} -p${db_password} -h${db_ip} -P${db_port} ${db} --routines --triggers --events --set-gtid-purged=off > ${db}.sql"
    #echo ${backup_cmd}	
    eval ${backup_cmd}
    
    check_flag=`tail -n 1 ${db}.sql | grep "Dump completed" | wc -l`
    if [ ${check_flag} -ne 1 ];then
        echo -e "backup ${db_ip}:${db_port}/${db} \e[1;31m failed \e[0m"
    else
        echo -e "backup ${db_ip}:${db_port}/${db} \e[1;33m success \e[0m"
    fi
}


backup(){
    if [ ! -d ${db_ip}_${db_port} ];then
        mkdir ${db_ip}_${db_port}
    fi
    
    cd ${db_ip}_${db_port}
    
    for db in ${database_list}
    do
        mysql_backup $db &
    done
    
    wait
}

drop(){
    for db in ${database_list}
    do
        drop_db_cmd="mysql -u${db_user} -p${db_password} -h${db_ip} -P${db_port} -e \"drop database ${db}\""
        eval ${drop_db_cmd}
        #echo ${drop_db_cmd}
        
        if [ $? -eq 0 ];then
            echo -e "drop database $db \e[1;33m success \e[0m"
        else
            echo -e "drop database $db \e[1;31m error \e[0m"
        fi
    done
}


clear(){
    user_list=`echo "select distinct user from mysql.user" | mysql -u${db_user} -p${db_password} -h${db_ip} -P${db_port} | grep -vw "user" | egrep -v "(ucloudbackup|root|slaveroot|tencentroot|tencentdumper)"`
    for user in ${user_list}
    do
        user_host_list=`echo "select distinct host from mysql.user where user='${user}'" | mysql -u${db_user} -p${db_password} -h${db_ip} -P${db_port} | grep -vw "host"`
        for user_host in ${user_host_list}
        do
            drop_user_cmd="echo \"drop user '${user}'@'${user_host}'\" | mysql -u${db_user} -p${db_password} -h${db_ip} -P${db_port}" 
            #echo ${drop_user_cmd}
            eval ${drop_user_cmd}	
            echo -e "drop user \e[1;33m'${user}'@'${user_host}'\e[0m"
        done
    done
    clear_root_cmd="echo \"update mysql.user set password=password('') where user='root';flush privileges;\" | mysql -u${db_user} -p${db_password} -h${db_ip} -P${db_port}"
    #echo ${clear_root_cmd}
    eval ${clear_root_cmd}
    echo "clear password done"
}


case "${method}" in
    'check')
        check
        ;;
    'drop')
        drop
        ;;
    'clear')
        clear
        ;;
    'backup')
        backup
        ;;
    *)
        echo "$0 ${hint}"
        exit 1
        ;;
esac
