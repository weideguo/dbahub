#!/bin/bash
#进程条
function processBar()
{
    allCount="$1"
    nowCount="$2"
    tput sc
    #隐藏光标
    tput civis
    #取得当前屏幕的列和行数
    screenCols=`tput cols`
    screenLines=`tput lines`
    #取得当前所在的行
    echo -ne '\e[6n';read -sdR pos
    pos=${pos#*[}
    nowLine=`echo ${pos} | cut -d ';' -f 1`
    if [ "${screenLines}" -ne "${nowLine}" ]; then
        nowLine=`expr ${nowLine} - 1`
    fi
    #算出进度条的块数
    allBlock=`echo "${screenCols}-7" | bc`
    #算出目前完成的块数
    nowBlock=`echo "(${nowCount}*${allBlock}/${allCount})" | bc`
    #算出总比例
    finishRate=`echo "${nowCount}*100/${allCount}" | bc`
    ratePos=`expr ${allBlock} + 2`
    #如果当前光标在底部，先空两行，留出来给显示
    if [ "${isFirst}" = "" -a "${screenLines}" -eq "${nowLine}" ]; then
        printf "\n"
        nowLine=`expr ${nowLine} - 2`
        isFirst='no'
    elif [ "${screenLines}" -eq "${nowLine}" ]; then
            nowLine=`expr ${nowLine} - 2`
    fi
    #找准位置显示完成数
    tput cup ${nowLine} 0
    printf "Connect Process: ${nowCount}/${allCount}"
    #显示进度条
    nowLine=`expr ${nowLine} + 1`
    tput cup ${nowLine} 0
    printf "["
    printf -v line '%*s' "$nowBlock"
    echo -n ${line// /=}
    printf ">"
    tput cup ${nowLine} ${ratePos}
    printf "]%d%%" ${finishRate}
    if [ "${nowCount}" -eq "${allCount}" ]; then
        printf "\n"
        #显示光标
        tput cnorm
    else
        tput rc
    fi
}
        
        
        
        
for ((i=1;i<=10;i++));do

    processBar 10 $i
    sleep 1

done  
        
                
