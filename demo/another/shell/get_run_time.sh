#!/bin/bash
#
#获取指定pid的进程的运行时间 返回秒
#

function get_run_time()
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
    
    echo $run_time
	return $run_time
}

get_run_time $@

#useage
#./get_run_time.sh $pid
