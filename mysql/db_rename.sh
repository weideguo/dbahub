#/bin/bash

db_host=$1

from_db=$2
to_db=$3

#db_host="10.19.33.111"
db_port="3306"
db_user="root"
db_password="root_password"

mysql_conn="mysql -u ${db_user} -p${db_password} -h${db_host}  -P${db_port}"

create_cmd="${mysql_conn} -e 'create database ${to_db}'"
eval ${create_cmd}

table_list=`${mysql_conn} -N -e "select TABLE_NAME from information_schema.tables where table_schema='${from_db}'"`
#echo ${table_list}

for tb in ${table_list}
do
    altr_cmd="${mysql_conn} -e 'alter table ${from_db}.${tb} rename to ${to_db}.${tb}'"
    #echo ${altr_cmd}
    eval ${altr_cmd}
done
