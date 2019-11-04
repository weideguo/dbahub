#!/bin/bash
# by weideguo in 20181114


dirpath=$(cd "$(dirname "$0")";pwd)
cd ${dirpath}

if [ $1 == "-c" ] 2>/dev/null;then                     #直接以ip 命令传入
    source ./config.sh
    tmp_tag=`date +%s%N`
    tmp_ip_list=".tmp_ip_list_"${tmp_tag}
    tmp_command_list=".tmp_command_list_"${tmp_tag}
    [ -f ${tmp_ip_list} ] && rm ${tmp_ip_list}
    [ -f ${tmp_command_list} ] && rm ${tmp_command_list}

    echo $2 | sed 's/,/\n/g' > ${tmp_ip_list}    #多个ip可以以","分隔
    echo $3 > ${tmp_command_list}

    IP_LIST=${tmp_ip_list}
    COMMAND_LIST=${tmp_command_list}
    
     
    if [ "X$4X" != "XX" ];then
        log_dir=$4
    fi
    

elif [ "X$3X" != "XX" ];then               #传入三个参数的情况
    source ./config.sh
    IP_LIST="$1"                 
    COMMAND_LIST="$2"       
    log_dir="$3/`date +%Y%m%d%H%M%N`"    


elif [ "X$1X" != "XX" ];then               #传入一个参数的情况
    source $1
else                                       #不传入参数的情况
    source ./config.sh
fi

mkdir -p ${log_dir}
echo ${log_dir}

myecho(){
    echo [`date +'%Y-%m-%d %H:%M:%S'`]" "$*
}


remote_exe(){
    remote_cmd=$*
    full_command='${SSHPASS} -p ''${PASSWD}'' ssh -p ${SSH_PORT} -l ${SSH_USER} ${SSH_HOST} ''${remote_cmd}'
    #echo ${full_command}
    eval ${full_command}
}

remote_send(){
    local_file=$1
    remote_dir=$2
    is_force=$3
    send_filename=`basename ${local_file}`
    local_file_md5sum=`md5sum ${local_file} | awk '{print $1}'`

    #make sure remote directory is correct
    if [ "${is_force}X" == "forceX" ] ;then
        remote_exe "[ -d ${remote_dir} ] && mv ${remote_dir} ${remote_dir}_`date +%s` ; mkdir -p ${remote_dir}" 
    else
        remote_exe "[ ! -d ${remote_dir} ] && mkdir -p ${remote_dir}"
    fi
    
    #to ensure file send complete,only file can send, not dir 
    full_send_command="${SSHPASS} -p '${PASSWD}' scp -P ${SSH_PORT} ${local_file} ${SSH_USER}@${SSH_HOST}:${remote_dir}" 
    #echo ${full_send_command}
    eval ${full_send_command}
    if [ $? -eq 0 ];then
        #remote_exe "md5sum ${remote_dir}/${send_filename}"
        remote_file_md5sum=`remote_exe "md5sum ${remote_dir}/${send_filename}" | awk '{print $1}'`
        if [ ${local_file_md5sum} == ${remote_file_md5sum} ] >/dev/null;then
            return 0
        else
            return 1
    
        fi
    else
        return $?
    fi

}


single_host_exe(){
    SSH_HOST=$1
    #echo ${SSH_HOST}
    #for cmd in $commands                                  #在空格换行问题
    #cat ${COMMAND_LIST} | grep -v "^#" | while read cmd   #存在只执行第一条命令问题
    c_num=`cat ${COMMAND_LIST} | wc -l`

    retcode=0 
    for j in `seq 1 ${c_num}`
    do
        if [ ${retcode} = 0 ];then
            cmd=`cat ${COMMAND_LIST} | head -n $j |tail -n 1 | grep -v "^#" | sed 's/^[ \t]*//g'`
            if [ "X${cmd}X" != "XX" ];then
            
                file_flag=`echo ${cmd} | grep -oP "^FILE"`
                myecho "CMD ------------ ["${cmd}"]"
                if [ ${file_flag} == "FILE" ] 2>/dev/null;then
                    local_file=`echo ${cmd} | awk -F ':' '{print $2}'`
                    remote_dir=`echo ${cmd} | awk -F ':' '{print $3}'`
                    is_force=`echo ${cmd} | awk -F ':' '{print $4}'`
                    remote_send ${local_file} ${remote_dir} ${is_force}
                else
                    remote_exe ${cmd}
                    #echo ${cmd}
                fi
                retcode=$?   
                myecho "return code ----------- "$retcode
                       
            fi
        fi
    done
}

#without concurrent control
main(){
    ips=`cat ${IP_LIST} | grep -v "^#" | sed 's/^[ \t]*//g'`
    for ip in $ips
    do
        myecho "begin runing ---------- ${ip}"
        { 
            single_host_exe ${ip} 
        } >${log_dir}/${ip}.log 2>${log_dir}/${ip}.err &
    done
    
    
    wait
    myecho "ALL DONE"
    
}

main

