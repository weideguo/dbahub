#!/bin/bash
#
#多进程扫描指定主机的端口，查看是否开放
#
#by weideguo in 20200515
#

#全局参数
#要扫描的主机ip
declare HOST="127.0.0.1"
#要扫描的端口列表
declare -a PORTS
declare PORT_NUM=0
#TCP超时则自动中断
declare TCP_TIMEOUT=10
#日志
declare LOGFILE="./$0.log"


#并发数
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

get_run_time()
{
    local run_count local_hz run_time
	local start_time curr_time

	if [ -d "/proc/$1" ]; then
        run_count=`cat /proc/$1/stat | cut -d " " -f 22`
	else
		return 0
	fi
        local_hz=`getconf CLK_TCK`
        start_time=$(($run_count/$local_hz))
        #echo $start_time
        
        curr_time=`cat /proc/uptime | cut -d " " -f 1 | cut -d "." -f 1`
        run_time=$((curr_time-start_time))
    
    #echo $run_time
	return $run_time
}

scan()
{
    local pipe_num=6
    
    init_concurrent ${pipe_num}
    
    echo -n > $LOGFILE
    for port in ${PORTS[*]}; 
    do
        read -u${pipe_num}
        {   
            echo "begin scan "$port
            {
                echo 2>/dev/null > /dev/tcp/$HOST/$port
                ret=$?
                if [ $ret -eq 0 ]; then 
                    echo -e "port is open: \e[1;33m $port\e[0m"
                    echo $port >> $LOGFILE
                fi
            } &
            sleep 1
            while [ 1 ] ;do
                pid=`jobs -p`
                get_run_time $pid
                run_time=$?
                #echo $port $pid "run time: "$run_time
                if [ $run_time -eq 0 ] || [ $run_time -gt $TCP_TIMEOUT ];then
                    kill -9 $pid 2>/dev/null
                    break
                fi
                sleep 1
            done
            wait 2>/dev/null 
            #echo "end scan "$port
            
            echo >&${pipe_num}
            
        } &
    
    done
    wait_concurrent ${pipe_num}
}

_parse_port()
{
	local start_port end_port port

	start_port=`echo $1 | cut -d "-" -f 1`
	end_port=`echo $1 | cut -d "-" -f 2`
	
	for ((port=$start_port; port <= $end_port; port++))
	do
		PORTS[$PORT_NUM]=$port
		((PORT_NUM++))
	done
	((PORT_NUM--))
}

parse_port()
{
	declare -a ports
	local tmp_ifs port

	tmp_ifs=$IFS; IFS=','; ports=$1
	
	for port in ${ports[@]}
	do
		if echo $port | grep -e ".*-.*" >/dev/null; then
			_parse_port $port
		else
			PORTS[$PORT_NUM]=$port
			((PORT_NUM++))
		fi
	done
	IFS=$tmp_ifs
}

usage()
{
echo -e "usage: \n\t$0 -p <port> [-n <concurrent_num> | -t <tcp_timeout> | -l <logfile>] <host>"
echo "example:"
echo -e "\t$0 -p 22,23,8000-8080 192.168.1.128"
echo -e "\t$0 -p 22,23,8000-8080 -n 10 192.168.1.128"
echo -e "\t$0 -p 22,23,8000-8080 -n 10 -t 20 -l test.log 192.168.1.128"
}

main()
{
	if [ $# -eq 0 ]; then
		usage
		exit 0
	fi
    
    #解析命令行获取参数 部分参数可以使用默认值
	while getopts "p:n:t:l:h" arg
	do
	case $arg in
		p)
			PORT=$OPTARG ;;
		n)
			MAX_SCAN_CONCURRENT=$OPTARG ;;
        t)  
            TCP_TIMEOUT=$OPTARG ;; 
        l)
            LOGFILE=$OPTARG ;; 
		h)
			usage
			exit 0
			;;
		?)
			usage
			exit 1
			;;
		esac
	done
    
    shift $((OPTIND-1))
    HOST=$@
    parse_port $PORT 
    
    scan 
    
    wait
}

main $@


