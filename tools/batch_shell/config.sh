#!/bin/bash

SSHPASS="./sshpass"


SSH_PORT=22
SSH_USER="root"
PASSWD='weideguo'                           #主机密码 #使用单引号防止一些字符转义


IP_LIST="ip_list"                           #最好使用绝对路径
COMMAND_LIST="command_list"                 #相对路径为脚本my_batch_exe.sh所在的目录
log_dir="log/`date +%Y%m%d%H%M%N`"          #

