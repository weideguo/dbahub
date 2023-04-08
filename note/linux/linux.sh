
shutdown 关机
  -h 关机
  -r 重启
poweroff 关机
reboot 重启
halt -p
init 0

运行级别
/etc/inittab   ##配置文件
 0 关机
 1 单用户模式
 2 不带网络的多用户模式
 3 多用户模式
 4 未使用
 5 X11图形化模式
 6 重新启动
runlevel ###显示上一个运行级别和当前运行级别
init 5   ###切换运行级别,系统中运行的第一个进程

启动顺序
BIOS->GRUB

(存储于CMOS)
BIOS(Basic Input Output System)      
EFI(Extensible Firmware Interface)   ##intel公司的bios升级

(存储于磁盘)
GRUB (GRand Unified Bootloader)
###linux使用的主流引导程序，linux上还有LILO
###多操作系统管理器，指定linux内核
/boot/grub/grub.conf   ###配置文件
/boot/grub 
dmesg 查看启动过程

###grub中的最小设置，可以进入编辑界面进行编辑
root     启动磁盘的位置，可以选择从磁盘 root (hd0,0) / root (cd0,0)
kernel     内核选择
initrd   初始化RAM磁盘，文件系统可用之前的一个初始化文件系统。作为内核引导的一部分进行加载。

#启动顺序
1）加载内核
2）执行init程序
3）/etc/rc.d/rc.sysinit             # 由init执行的第一个脚本
4）/etc/rc.d/rc$RUNLEVEL            # $RUNLEVEL为缺省的运行模式
5）/etc/rc.d/rc.local
6）/sbin/mingetty                   # 或/sbin/agetty等类似进程  用于开启终端，接受tty


当init进入一个运行等级的时候，按照数字顺序运行所有以K开头的脚本并传入stop参数，除非对应的init脚本在前一个运行等级中没有启动
按照数字顺序运行所有以S开头的脚本并传入start参数
任何以D开头的脚本都会被忽略


tty  #查看当前的tty

whoami ##显示当前用户
who    ##显示登陆用户
w      ##显示登陆用户并且现在干嘛

ls+tab+tab  查看ls开头的命令
which command    ##查看command的路径
whereis command
type command    ##查看command的路径


date 显示时间
hwclocck/clock 显示计算机硬件时间
cal 显示日历
uptime 系统运行时间

linux版本查看
cat /etc/issue

uname -a
查看【/etc/*-release】文件 
bash (bourne-again shell)  ###linux上大部分默认的Shell，其他shell例如tcsh、csh、ash、bsh、ksh
gnome-session  ##gnome情况


环境变量
系统参数
存储位置为用户的跟目录,如weideguo用户为 【/home/weideugo/.bash_profile】
使用【source .bash_profile】在更改后立即生效

/home/weideugo/.bashrc   ###每次打开新会话都自动生效

全局系统参数
/etc/profile
/etc/bashrc
/etc/profile.d/

.bash_history            ##history的信息，清空可以清除history的显示  


env  显示所有环境变量
set  显示本地定义的shell变量
unset 变量名  清除环境变量
export 变量名=变量值  设置环境变量

env 命令输出参数
PATH 可执行命令路径
PROMPT_COMMAND  用户执行后执行
SSH_CONNECTION  当前SSH连接信息

#查看当前主机ip（多网卡时显示当前连接所用的ip，复杂网络环境不适用）
env|grep -i SSH_CONNECTION|awk '{print $3}'


hostname       ##查看主机名  【/etc/sysconfig/network】修改配置文件实现修改主机名，使用【hostname new_hostname】临时修改主机名


echo "xxx" | xargs                          ##设置标准输出
ps -ef | grep xxx | xargs kill -9
xargs - build and execute command lines from standard input


date -d @141231322   #时间戳换成时间
date +%s             #显示时间戳
date "+%Y-%m-%d %H:%M:%S"  #显示时间
date -R                    #显示时区

#查看时区
ll /etc/timezone
ll /etc/localtime    #centos

#修改时区
#操作后直接生效 不需要重启
rm -rf /etc/timezone
ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/timezone   #必须要确保文件存在

export TZ='Asia/Shanghai'                               #修改环境变量也可以修改参数 如果要持久可以写入profile文件


telnet退出
ctrl+] 


service vsftpd start      ##启动程序
service vsftpd stop       ##结束进程

/var/log/cron            ##crontab日志
/var/spool/cron/        ##crontab 的信息，每个账号的调度对应一个文件，文件可以热加载（因而可能会被恶意利用，如通过写文件实现反弹shell）


##重启crond
service syslog stop                     ##系统的日志守护进程
service rsyslog restart                 ##sylog的增强版本，增加网络传输，远端的日志可以传输到本地
service syslog start
service crond restart

crontab  ####任务调度   设置可执行程序的定时运行
crontab -l   ###查看
crontab -e   ###编辑  使用方法与vi类似

stty size               #查看终端的大小
pwd                     ###显示当前目录

md5sum                  ##计算文件的MD5

sha1sum

sha256sum

base64编码
echo "AAA@#$" | base64
echo "QUFBQCMkCg==" | base64 -d



随机生成密码
date | md5sum

cat /dev/urandom | head -1 | md5sum 

openssl rand -base64 10


动态链接库
/etc/ld.so.conf
ldconfig



###funny###
二维码生成

qrencode -o qr.png "string_seen_by_scan_qr"

nice #调整进程优先级别


##linux与window的文件传输 使用ZModem协议
sz  将选定的文件发送到本地
rz  交互窗口 rz -bey
