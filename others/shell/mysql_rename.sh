#!/bin/sh
#
#Alter: weideguo
#Date: 2020-07-29
#Description:mysql数据库重命名 不需要交互

function usage()
{
    if [ "$instance_port" = "" -o "$mysql_user" = "" -o "$mysql_pwd" = "" -o "$from_dbname" = "" -o "$to_dbname" = "" ]; then
        echo "Usage:"
        echo "sh ${SCRIPT_NAME}"' ${mysql_port} ${mysql_user} ${mysql_pwd} ${from_dbname} ${to_dbname} [${host}]' 
        exit 1
    fi
}


function execute_sql()
{
    sql="$1"
    if [ -z "$mysql_user" -o "$mysql_user" = "" -o -z "${mysql_pwd}" -o "${mysql_pwd}" = "" ]; then
        echo "Error: mysql user or mysql password is not valid."
        exit 1
    fi
    if [ "$sql" = "" ]; then
        cat | mysql -u${mysql_user} -p${mysql_pwd} --default-character-set=utf8  ${server_tag}  -N 
    else
        echo "$sql" | mysql  -u${mysql_user} -p${mysql_pwd} --default-character-set=utf8  ${server_tag}  -N 
    fi
}


function check_db_exist()
{
    #防止$from_dbname意外变更
    temp_dbname="$from_dbname"
    is_exist_fromdb=`echo "show databases;" | execute_sql | grep -w "${from_dbname}" | wc -l`
    if [ "$is_exist_fromdb" -eq 0 ]; then
        echo "Error: The source database '${from_dbname}' is not exist."
        exit 1
    fi
}


#判断是否有连接
function check_conn()
{
    dbname="$1"

    is_exist_conn=`echo "show processlist" | execute_sql | grep -w "${dbname}" | wc -l`
    if [ "${is_exist_conn}" -ne 0 ]; then
        echo "connections of database is not 0" 
        exit 1
    fi
}


function mysql_db_rename()
{
    echo "change the database name from '${from_dbname}' to '${to_dbname}'"
    
    create_database_by_sql="yes"
    if [ ${host} = "127.0.0.1" -o ${host} = "localhost" ] && [ -d ${data_dir} ];then
        #操作本地数据库时
        teg_db_file=$(find ${data_dir} -name "${from_dbname}")
        ibd_num=$(find ${data_dir} -name "${from_dbname}" |  xargs ls | grep ibd | wc -l)
        
        if [ -L "${teg_db_file}" -a $ibd_num -ge 1 ]; then
            #数据库的数据目录为链接时
            db_file_num=$(find /data -name "${to_dbname}" | grep -w ${to_dbname} |wc -l)
            if [ ${db_file_num} -ge 1 ]; then
                echo "Error: The target database '${to_dbname}' is alread exist."
                exit 1
            fi
    
            sour_db_file=$(echo ${teg_db_file%/*} | xargs ls -l| grep -w ${from_dbname} |awk -F"->" '{print $2}' | sed 's/\ //')
            teg_db_path=$(echo ${teg_db_file%/*})
            sour_db_path=$(echo ${sour_db_file%/*})
            mkdir ${sour_db_path}/${to_dbname}
            chown -R mysql:mysql ${sour_db_path}/${to_dbname}
            ln -s ${sour_db_path}/${to_dbname} ${teg_db_path}/${to_dbname}
            create_database_by_sql=""
        fi
    fi
    
    if [ ${create_database_by_sql} ];then
        is_exist_to_db=`echo "show databases;" | execute_sql | grep -w "${to_dbname}" | wc -l`
        if [ "$is_exist_to_db" -ne 0 ]; then
            echo "Error: The target database '${to_dbname}' is alread exist."
            exit 1
        fi
        echo "create database ${to_dbname};" | execute_sql
        if [ "$?" -ne 0 ]; then
            echo "Error: Some error occur when create database ${to_dbname}."
            exit 1
        fi
    fi
    the_dumpout_file="temp_`date +%Y%m%d%T | sed 's/://g'`"
    if [ -f $the_dumpout_file ]; then
        echo "Error: The file $the_dumpout_file is alread exist."
        exit 1
    fi
    echo "USE ${to_dbname} ;" > $the_dumpout_file
    #dump出视图
    echo "select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='$from_dbname' and TABLE_TYPE='VIEW';" | execute_sql | while read viewName; do
        mysqldump -u${mysql_user} -p${mysql_pwd}  ${server_tag} --default-character-set=utf8 -d ${from_dbname} ${viewName} >> $the_dumpout_file
        if [ "$?" -ne 0 ]; then
            echo "Error: Some error occur when dump out view ${viewName}."
            exit 1
        fi
    done
    if [ "$?" -ne 0 ]; then    
        echo "Error: Some error occur when dump out view."
        exit 1
    fi    
    #dump存储过程和事件
    mysqldump -u${mysql_user} -p${mysql_pwd}  ${server_tag} --default-character-set=utf8 ${from_dbname} --no-create-info --no-data -E -R >> $the_dumpout_file
    if [ "$?" -ne 0 ]; then
        echo "Error: Some error occur when dump out data."
        exit 1
    fi
    #迁表
    echo "select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='$from_dbname' and TABLE_TYPE='BASE TABLE';" | execute_sql | while read tableName; do
        echo "alter table ${from_dbname}.${tableName} rename ${to_dbname}.${tableName};" | execute_sql
        if [ "$?" -ne 0 ]; then
            echo "Error: Some error occur when execute 'alter table ${from_dbname}.${tableName} rename ${to_dbname}.${tableName};'"   
            exit 1
        fi
    done
    if [ "$?" -ne 0 ]; then
        echo "Error: Some error occur when alter table name."
        exit 1
    fi
    from_site=`echo "${from_dbname}"|awk -F"_" '{print $3"_"$4}'`
    toSite=`echo "${to_dbname}"|awk -F"_" '{print $3"_"$4}'`
    sed -i "s/${from_site}/${toSite}/g" $the_dumpout_file
    sed -i "s/${from_dbname}/${to_dbname}/g" $the_dumpout_file
    
    cat $the_dumpout_file | execute_sql
    if [ "$?" -ne 0 ]; then
        echo "Error: Some error occur when dump in data."
        exit 1
    else
        #成功
        echo "${from_dbname} ====> ${to_dbname}............OK."
        rm -rf $the_dumpout_file
    fi

    #删除原来的数据库
    echo "drop the database '${from_dbname}'"
    echo "drop database ${from_dbname}" | execute_sql
    if [ "$?" -ne 0 ]; then
        echo "Error: Some error occur when drop database ${from_dbname}."
        exit 1
    fi
 
}


function main()
{
    instance_port="$1"
    mysql_user="$2"
    mysql_pwd="$3"
    from_dbname="$4"
    to_dbname="$5"
    host="$6"
    usage
    
    data_dir="/data/mysqldata/"
    default_port="3306"
    
    if [ "X${host}X" != "XX" ];then
        server_tag="-h ${host} -P ${instance_port}"
    else
        #多个数据库的情况
        host="127.0.0.1"
        msock=$(ps -ef | grep -v -E "mysqld_safe|awk" | awk '/mysqld /,/socket=/''{for(i=1;i<=NF;i++){if($i~/socket=/) print gsub(/--socket=/,""),$i}}' | awk '{print $2}')
        thesock=$(echo $msock | sed 's/\ /\n/g' | grep $instance_port | head -1)
        if [ "$thesock" = "" -a ${instance_port} = ${default_port} ]; then
            mysql_sock=$(ps -ef | grep -v -E "mysqld_safe|awk" | awk '/mysqld /,/socket=/''{for(i=1;i<=NF;i++){if($i~/socket=/) print gsub(/--socket=/,""),$i}}' | awk '{print $2}' | head -1)
            mysql_port="${instance_port}"
        else
            mysql_sock="${thesock}"
            mysql_port="${instance_port}"
        fi
        server_tag="-S ${mysql_sock} -P ${mysql_port}"
    fi
    
    check_db_exist
    check_conn "${from_dbname}"
    mysql_db_rename
}

SCRIPT_NAME=$0
main "$1" "$2" "$3" "$4" "$5" "$6"

#不能存在trigger，如果存在，请先手动备份trigger并删除，然后再运行
#demo:
#./mysql_rename.sh 3306 root my_passwd db1 todb1 
#./mysql_rename.sh 3306 root my_passwd db1 todb1 127.0.0.1



