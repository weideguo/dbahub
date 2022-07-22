
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



OOM out-of memory                         ##系统会杀掉一些进程以释放内存
OOM内核参数设置  
/etc/sysctl.conf                          ##修改该文件中对应的值
sysctl -p                                 ##使修改生效
sysctl vm.overcommit_memory=1             ##直接使内核参数生效
sysctl -a                                 ##列出所有内核参数值

echo 0 > /proc/sys/vm/swapping            ##禁用所有进程使用swap 直接生效 重启失效
vm.swapping=0                             ###/etc/sysctl.conf中修改禁用swap

cat /proc/sys/vm/swappiness               ##100-60=40%的时候，就开始出现有交换分区的使用 swappiness=0的时候表示最大限度使用物理内存
vm.swappiness=10                          ##修改swap的使用权重

swapoff -a  #临时关闭swap
##编辑/etc/fstab实现固定设置

SWAP分区异常使用
 程序内存泄露  
 NUMA使用不当
处理方法 重启OS

mysqld --memlock                ##内存锁定             

         
/proc/$pid/smaps                    ##查看进程的swap的使用
/proc/$pid/maps

cat /proc/$pid/smaps | grep "Swap"     ##查看swap，需要先相加起来
cat /proc/$pid/status | grep "Swap"    ##查看swap

pmap -d $pid 
代码段、数据段、堆、文件映射区域、栈
虚拟地址空间使用情况


透明巨型页
echo never > /sys/kernel/mm/transparent_hugepage/enabled    #修改巨型页的使用
vm.nr_hugepage=hugepage_num     ##使用hugepage  巨型页

透明巨型页的参数
cat /proc/meminfo | grep Huge
需要使用swap时，内存页被分割为4kb

x86的默认内存页大小是4kb，可以使用2mb或者更大的巨型页

echo 2000 > /proc/sys/vm/nr_hugepages  #修改巨型页的数量

numactl             ##控制进程与共享存储的numa技术

numactl --interleave=all ${command}
#当当前cpu没有可以分配的内存，可以使用其他cpu的内存。all表示所有
#不设置时当达到cpu的分配阈值，即使系统还有空余内存，也不分配给当前cpu，而选择使用SWAP


SMP  symmetic multi processing                对称多处理系统
MPP  massvie parallel processor                大规模并行处理
NUMA non uniform memory access architecture        非统一内存访问


vmstat                ###查看虚拟内存swap si/so 表示与物理内存的交换
vmstat -S m 1        ###隔1秒显示一次

##增加swap分区  重启后失效
dd if=/dev/zero of=/home/swap bs=1024 count=512000    ##增加512000K  #创建一个大文件，内容全为0
/sbin/mkswap /home/swap  ##执行命令
/sbin/swapon /home/swap  ##执行命令
/usr/swap/swapfile  /swap   swap    defaults    0 0   ##编辑/etc/fstab实现固定设置



资源限制
ulimit
cgroups
/proc/cgroups 

##修改最大文件描述符
/etc/security/limits.conf             ###配置文件修改，最大打开文件数，以及其他
/etc/security/limits.d



ulimit -a                            ###查看所有的限制
ulimit -n 2048                        ##修改允许打开最大的文件数
lsof | wc -l                        ##查看已经打开的文件数
lsof -p pid                         ##查看进程打开的文件
lsof -c mysql                                           ##查看对应进程名打开的文件
lsof +L1                                                ##unlinked的文件信息
lsof +L/-L                                              ##打开或关闭文件的连结数计算，当+L没有指定时，所有的连结数都会显示(默认)；若+L后指定数字，则只要连结数小于该数字的信息会显示；连结数会显示在NLINK列。
ulimit -Hn                          ##查看

#删除恢复 进程使用文件时删除文件的恢复
lsof | grep       
获取进程（PID列）        $pid
文件描述符（FD列的数字）  $fd

ll /proc/$pid/fd/$fd               #只要文件存在 可以cat并重定向恢复


chattr     #在文件系统层对文件属性的更改 只能在超级用户使用
A：即Atime，告诉系统不要修改对这个文件的最后访问时间。
S：即Sync，一旦应用程序对这个文件执行了写操作，使系统立刻把修改的结果写到磁盘。
a：即Append Only，系统只允许在这个文件之后追加数据，不允许任何进程覆盖或截断这个文件。如果目录具有这个属性，系统将只允许在这个目录下建立和修改文件，而不允许删除任何文件。
b：不更新文件或目录的最后存取时间。
c：将文件或目录压缩后存放。
d：当dump程序执行时，该文件或目录不会被dump备份。
D: 检查压缩文件中的错误。
i：即Immutable，系统不允许对这个文件进行任何的修改。如果目录具有这个属性，那么任何的进程只能修改目录之下的文件，不允许建立和删除文件。
s：彻底删除文件，不可恢复，因为是从磁盘上删除，然后用0填充文件所在区域。
u：当一个应用程序请求删除这个文件，系统会保留其数据块以便以后能够恢复删除这个文件，用来防止意外删除文件或目录。
t: 文件系统支持尾部合并（tail-merging）。
X：可以直接访问压缩文件的内容。

chattr +i dirname    #则不能对该文件夹进行任何修改
+ - =                #操作符

lsattr  filename     #查看文件属性


quota                  #磁盘使用限制
edquota                #编辑数据文件


pmap pid                            ##查看指定pid使用的内存


lspci | grep -i vga   ##查看显卡
lspci | grep -i net   ##查看网卡
lspci -v -s 


lspci 查看PCI设备
lsusb 查看USB设备）
lsblk 查看块设备
ls+tab+tab  查看ls开头的命令
which command    ##查看command的路径
whereis command
type command    ##查看command的路径


time command    #计算命令执行的时间
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



linux下display参数设置
#1 vncserver   ##启动vnc(virtual network computer)
2 export DISPLAY=localhost:n  ##n为1中的启动信息 export DISPLAY=:0.0 
3 xhost +x  ## x可以为主机或用户名，如local:oracle，即指定为本地的oracle用户可以图像界面 不指定x为允许所有
DISPLAY hostname:displaynumber.screennumber  ##DISPLAY参数设置，使用xmanager连接

xclock   ###验证display参数

环境变量
系统参数
存储位置为用户的跟目录,如weideguo用户为 【/home/weideugo/.bash_profile】
使用【source .bash_profile】在更改后立即生效

/home/weideugo/.bashrc   ###每次打开新会话都自动生效

全局系统参数
/etc/profile
/etc/bashrc


.bash_history            ##history的信息，清空可以清除history的显示  

selinux
配置文件/etc/sysconfig/selinux
工作模式 SElinux=permissive
强制（enfocing）：违反策略的行动都被禁止，并作为内核信息记录
允许（permissive）：违反策略的行动不被禁止，但会产生警告信息
禁用（disabled）：禁用SElinux，与不带SElinux的系统一样         
/usr/sbin/sestatus -v      ##如果SELinux status参数为enabled即为开启状态
getenforce                 ##也可以用这个命令检查
setenforce 0                 ##临时关闭；1 为开启

由selinux设置问题导致启动失败
进入kernel选择界面，编辑kernel，添加 
enforing=0


传统的Linux系统安全，采用的是 DAC（自主访问控制方式），对应用户是否拥有某个资源的权限（读、写、执行）
SELinux是部署在Linux系统中的安全增强功能模块，对进程和文件资源采用 MAC（强制访问控制方式）

 
 
用户管理、权限管理
passwd testuser    ##给已创建的用户设置密码
userdel testuser   ##删除用户
rm -rf testuser    ##删除目录

#非交互模式更改密码 只能在root账号使用
echo 'new_passwd' | passwd --stdin auser

groupadd group_name  ###添加组
groupmod group_name  ###修改组
groupdel group_name  ###删除组
useradd –s /sbin/nologin –d /var/www/ dengftp
#注-s /sbin/nologin是让其不能登陆系统，-d 是指定用户目录为/var/www/ 
#添加用户时可以使用【-g、-G】参数关联到对应的组
chown –R user_name:group_name /var/www/   #注:将用户目录及其子目录的所有和所属的组设置为dengftp
chmod 774 /var/www/
chgrp group_name file_name  ###修改文件所属组
chmod -R 774 /var/www/  ###更改目录及目录下所有文件的权限
id -a user ###查看user所属的组
usermod    ##修改用户的信息，如修改所属组、home文件、密码、uid
usermod -a -G new_group username  #添加从组
usermod -G "" username            #移除所有从组
usermod -g primary_group username #修改主组

userdel user_name ##删除用户   (加 -r 删除用户目录）
/etc/passwd  ##保存用户信息  LOGNAME:PASSWORD:UID:GID:USERINFO:HOME:SHELL UID为0则为root账号同一用户级别
/etc/shadow  ##保存用户密码
/etc/group   ##保存组信息


/etc/shadow 文件字段说明
帐号名称 ：root 
加密后的密码              （星号代表帐号被锁定，双叹号表示这个密码已经过期了，密码格式$id$salt$encrypted）
上次修改密码的日期：      （ 1/1/1970 起的天数）
最小修改时间间隔：        （0表示可在任何时间修改） 
密码需要被重新变更的天数：（99999） 
密码变更前提前几天警告：
密码过期后的宽限天数：    
账号失效时间：            （ 1/1/1970 起的天数）
保留条目


umask -S        ###查看用户创建文件时文件的默认权限
umask 002    ###修改文件的默认权限，为 666-002
             ###文件夹777-002
添加执行sudo的权限为在sudoers文件【/etc/sudoers】中添加
visudo                          ###直接进入编辑/etc/sudoers   也可以用vi编辑，写入的时候强制写入
sudo ${command}                  ###以root用户执行命令

sudo -u db_user00 ${command}       ##以指定用户执行命令

sudo /bin/su - db_user00 /data/db_user00/redis_6379/redis_server.sh start   ##以root用户身份执行su ...

runuser -l db_user00 -c "${command}"  ##root账号以特定用户执行


##/etc/sudoers或/etc/sudoers.d目录下任意文件
#可以在任意地方以任意账号免密执行
%group_name  ALL=(ALL)  NOPASSWD: ALL
user_name  ALL=(ALL)  NOPASSWD: ALL
#可以在任意地方以root账号执行 需要输入当前账号的密码
%group_name  ALL=/bin/ls 
%group_name  ALL=(root)/bin/ls PASSWD: ALL
user_name  ALL=/bin/ls 
#可以在任意地方以root账号免密执行
%group_name   ALL=(root) NOPASSWD: /bin/ls,(root) NOPASSWD: /bin/ln
user_name   ALL=(root) NOPASSWD: /bin/ls,(root) NOPASSWD: /bin/ln


whoami ##显示当前用户
who    ##显示登陆用户
w      ##显示登陆用户并且现在干嘛

chmod
- 第一组rwx：文件所有者的权限是读、写和执行
- 第二组rw-：与文件所有者同一组的用户的权限是读、写但不能执行
- 第三组r--：不与文件所有者同组的其他用户的权限是读不能写和执行
可用数字表示为：r=4，w=2，x=1  因此rwx=4+2+1=7

chroot $NEWROOT $COMMAND   ####run command or interactive shell with special root directory

ACL（access control list）      ###现对与chmod管理粒度更细
mount -o acl /dev/sda5 /mnt     ###ACL需要在挂载文件的时候打开ACL功能
getfacl file_name                       ###查看一个文件的ACL设置
setfacl -m u:username:rwx file_name       ###设置用户权限
setfacl -m g:groupname:--x file_name     ###设置组权限
setfacl -x u:username file_name           ####删除ACL设置


tune2fs -o +acl /dev/sda        ###ext2/ext3/ext4文件系统增加acl功能


文件管理
tar –xvf file.tar        ##解压 tar包
tar -xzvf file.tar.gz    ##解压tar.gz
tar -xjvf file.tar.bz2   ##解压 tar.bz2
压缩/解压
bzip2 
gzip    
xz
    
awk '{print $1}' filename              ####显示文件中每行第一个字符串
awk -F':' '{print $1}' filename        ####使用分割符":"分割并显示每行第一个字符
awk -F":" '{print $1}' filename
awk -F":" '/exp/{print $1}'            ###查找符合exp的行并进行分割，可以使用正则表达式
awk '/exp/'

awk '{sum += $1};END {print sum}'   ##计算数字总和

ls -altr * | awk '{print $5}' | awk '{sum += $1};END {print sum/1024/1014/1014}'    #汇总计算文件大小

awk '{x[$1]+=1} END{for( i in x ){print x[i]"    "i}}'                              #聚合



sed [-nefri] 'command' filename             ####编辑文字  删除、替换  
sed 's/lintxt1/linetxt2/g'    filename        ####替换字符 将文件中的linetxt1替换成linetxt2 可以使用正则表达式
sed 's|lintxt1|linetxt2|g'    filename
sed '/linetxt/d' filename                    ####删除匹配的行  将配备linetxt的行删除 可以使用正则表达式


echo "xxx" | xargs                          ##设置标准输出

xargs - build and execute command lines from standard input

tr '.' '_'    filename                        ##将【.】替换为【_】，-d为删除
tr -s " " filename                            ##去除空格


list的使用
ip=($ip1 $ip2 $ip3)        ###以空格分割
${ip:1:2 }                ###显示list中下标1到2的元素
${str#exp}                                    ###字符串str截去exp，截取操作可以使用类似命令

cut -d '#' -f 1 filename                    ###以"#"分割字符串并获取第一个值
 
grep -o 'exp' filename                         ###查找只符合exp中的字符串，可以使用正则表达式  不用-o则匹配行
grep -oP "(?<=//).*?(?=/)"                    ###-P perl类型的正则表达式，支持零宽断言

grep -v "exp" filename                        ###反向选择，获取不包含exp的行

grep -C 5 "foo" file    #显示file文件里匹配foo字串那行以及上下5行
grep -B 5 "foo" file    #显示foo及前5行
grep -A 5 "foo" file    #显示foo及后5行


uniq filename                                ###获取的行没有重复，-d获取有重复的行

cmp filename1 filename2                        ###逐位比较两个文件
diff                                        ###逐行比

basename $path/filename                        ###从全录路径中提取文件名
basename $path/filename.txt    .txt            ###从全录路径中提取文件名并去掉后缀
 


diff  file_old file_new > file_update.patch   #生成补丁文件
patch -p0 file_old     file_update.patch      #应用补丁文件 不能多次应用


diff -Naru test test_new  > test.patch        #对比目录  使用git时 git diff > my.patch

mv test
patch -p1 < test.patch                        #因为对比时是在目录外对比，因此打补丁时要忽略一级目录
 

#二进制对比
xdelta3 -s SOURCE TARGET > OUT                #生成补丁
xdelta3 -d -s SOURCE OUT TARGET_NEW           #打补丁成新文件
 

##正则表达
"sinosy_${DATE}_*.log"    双引号可以禁止通配符扩展，但是允许变量扩展。
'sinosy_${DATE}_*.log'    同时禁止通配符扩展与变量扩展。
sinosy_${DATE}_\*.log    使用转义字符——反斜杠，也可以防止扩展。

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


cat ctl | grep -v ^- | grep -v ^$  ###去除【-】开头的行及去除空行
## ^正则表达式中字符串的开始 $正则表达式中字符串的结束


排序
sort -rn -k 1 -t: file_name   
####对文件的行以【:】分割，以第1列排序。不指定【-t】则默认为空格符。
####【-r】逆序；【-n】以10进制排序

test -d 'path_name1' || mkdir 'path_name2'     
###【test -d】判断路径是否为目录
###前一条件为假则执行后面的语句

curl  ##运行url，如下载文件

curl -d "p1=v1&p2=v2" "http://example"  #post

curl -k    #忽略https未信任证书错误

curl -u user:name ...
# 等同于
base64_str=`echo user:name | base64`
curl -H "Authorization: Basic ${base64_str}" ...



wget  ##通过url下载
scp local_file remote_username@remote_ip:remote_filefolder   ##从本地复制到远端，反过来即为远端复制到本地

scp -oPort=3600 -r ...
-oPort -P       ##指定使用的端口
-r              ##复制目录
-C                ##压缩传输

-o              ##与ssh的使用一致
-oPort=3600
-o "Port 3600"  ##格式跟~/.ssh/config的一致


sshpass -p my_password scp ...
sshpass -p my_password ssh ...
ssh [user@]hostname [command]   #远程执行


压缩传输

scp -C filename remote_user@remote_host:remote_path

scp -oStrictHostKeyChecking=no -P 16333 -Cr filename remote_user@remote_host:remote_path

#带压缩
rsync -zav --rsh='ssh -p 22' filename remote_user@remote_host:remote_path

#非交互传输
rsync -av dirname --rsh='sshpass -p ssh_password ssh -p 22'  root@172.16.2.150:/root/test

#非交互传输 自动接受未知的主机
rsync -av dirname --rsh='sshpass -p ssh_password ssh -oStrictHostKeyChecking=no -p 22'  root@172.16.2.150:/root/test


-z 压缩

--bwlimit 限制带宽

#断点续传 中断时再次启动默认会删除传输到一半的文件 可以选择以下参数实现断点续传
--partial
--partial-dir=DIR         #指定一个目录缓存传到一半的文件
-P


nc传输
host2传输到host1
host1: nc -l 1234 | tar zxvf -
host2: tar zcvf - test | nc 192.168.1.176 1234


telnet   #退出
ctrl+]   


rsync
两种模式
C/S 
    server
        rsync --daemon --config=/data/rsyncd.conf
    client
        rsync -azvrP path_to_send rsync://remote_user@remote_host:port/block_name        ##block_name为server端配置文件中的块名
        
命令行（使用ssh协议）
        rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST             ##从源端（SRC，可以多个）同步文件到目的端（DEST）


客户端    
rsync rsyncd.secrets --password-file=test.secrets rsync://remote_user@remote_host:port/block_name    
    
使用密码文件权限必须其他账号不能访问（只是对于rsync模式有效，ssh模式不能使用密码文件）    
    
#进入stfp交互模式
sftp -o Port=22  root@10.10.1.10
 #在本地执行
 lpwd
 lcd
 lls
 #对远端主机执行
 pwd
 cd
 ls
 #上传下载
 get remote_file local_path
 put local_file remote_path


#实时文件同步
inotify-tools 监听文件然后使用rsync推送文件



nc
###端口扫描
nc -v -w 2 -z 192.168.5.230 21               

##扫描udp端口
nc -u 127.0.0.1 9000
nc -u -z -v -w 2 127.0.0.1 9000    #非交互模式

###监听端口
nc -lp 65500                   ###旧版
nc -l 65500                    ###新版
nc --udp -l 65500            ###新版 默认使用TCP协议

nc -lp 65500  &                ##后台运行
nc -l -w 10000 6500 &        ##


#使用不同网卡/ip监听  同一主机中相同端口不同ip之间不互相冲突，即可以同时监听  ipA:portX ipB:portX
nc -l 192.168.253.128  12345
nc -lv 192.168.253.128  12345
nc -lv 127.0.0.1 12345

###远程复制 host2到host1
##1234为端口，没有限制;操作步骤有要求
host1: nc -l 1234 > text.txt
host2: nc host1_ip 1234 < text.txt      

host1: nc -l 1234 | tar zxvf -
host2: tar zcvf - text.txt | nc host1_ip 1234

###聊天
host1: nc -lp 1234
host2: nc host1_ip 1234

###操作memcached
print "get key_name" | nc $ip_address $port


###查看命令
cat
more
tail

find ./ -name "file_name"  ##当前文件以名字查找
find ./ -name "*test*" –type f -exec rm -rf {} \;   ###查找当前目录下指定文件并删除 ##【-exec command ;】匹配后执行command
find ./ -name "*test*" –type d                        ###查找当前目录下指定的目录
find ./ -type f -ctime +14 -exec rm -rf {} \;        ##查找时间离现在大于14天的文件，删除

find ./ ! -path "./aaa"                             #! 过滤

-maxdepth   #目录深度指定



wc -l   ###计算行数
wc      ###文本计数

strings binary_file      ###查看二进制文件


- 可看成特殊的文件？
echo "aaa" | cat -
echo "aaa" | cat --
echo "aaa" | cat 


tee filename         ##将输入写入文件中

echo "xyz" > filename    ###清空文件并写入
echo "xyz" >> filename      ###在尾部追加写入


stdbuf -oL    ${command} > out.log
#以行为缓冲单位重定向命令的输出，即命令输出一行，写入文件一行


VI列编辑
crtl+v 进入列模式
shift+i 插入
ESC两次 退出列模式

TAB替换为空格
~/.vimrc文件写入
set ts=4 
set expandtab

对于已保存的文件
:set ts=4
:set expandtab
:%retab!

VI
使用【Esc键】切换由插入模式进入命令模式（command mode、insert mode）
由命令模式进入插入模式
按 i 切换进入插入模式后，是从光标当前位置开始输入文件；
按 a 进入插入模式后，是从目前光标所在位置的下一个位置开始输入文字；
按 o 进入插入模式后，是插入新的一行，从行首开始输入文字。

删除文字
x ：每按一次，删除光标所在位置的一个字符。
#x ：删除光标所在位置的后面#个字符。
X ：每按一次，删除光标所在位置的前面一个字符。（shift+x 也可以）
#X ：删除光标所在位置的前面#个字符。
dd ：删除光标所在行。
#dd ：从光标所在行开始删除#行。
dgg   删除当前行至第一行
dG    删除当前行至最后一行
d1G    删除当前行至第一行 包括当前行以及第一行

退出及保存文件
:w （保存当前文件）
:w filename （将文件以指定的文件名“filename”保存）
:wq （保存并退出vi）
:wq filename（将正在编辑的文件保存为“filename”文件退出vi）
:q （退出vi）
:q! （不存盘强制退出vi）
:x （相当于 :wq 的功能）

恢复上一次操作
u ：如果您误执行一个命令，可以马上按下 u ，回到上一个操作。按多次 u 可以执行多次恢复。

复制粘贴
yw ：将光标所在之字符串复制到缓冲区中。
#yw ：复制#个字串到缓冲区。
yy ：复制光标所在行到缓冲区。
#yy ：复制从光标所在行往下#行文字。
p ：将缓冲区内的字符贴到光标所在位置。

替换更改
r ：替换光标所在处的字符。
R ：替换光标所到之处的字符，直到按下 ESC 键为止。
cw ：更改光标所在处的字到字尾处
#cw ：更改多个字符

移动光标
vi可以直接用键盘上的光标来上下左右移动，但正规的vi是用小写英文字母 h 、 j 、 k 、 l ，分别控制光标左、下、上、右移一格。
按 G ：移动到最后一行行尾。   （键盘为shift+G）
按1G ：定位到第一行，第n行同理（1+shift+G）
按 $ ：移动到光标所在行的行尾。
按 0 ：移到当前行的开头。
#G ：移动光标至文件的第#行行首
按 Ctrl+b ：屏幕往后移动一页。
按 Ctrl+f ：屏幕往前移动一页。
按 Ctrl+u ：屏幕往后移动半页。
按 Ctrl+d ：屏幕往前移动半页。
Ctrl+g 列出光标所在行的行号。

按 ^ ：移动到光标所在行的行首。
按 w ：光标跳到下个字的开头。
按 e ：光标跳到下个字的字尾。
按 b ：光标回到上个字的开头。
按 #l ：光标往后移的第#个位置。

显示行号
:set number
关闭行号
：set nonu
/string        向前搜索指定的字符
?string        向后收索指定的字符
n            收索下一个字符串

linux中的文件标识
l是链接，相当于windows的快捷方式
d是目录，相当于windows的文件夹
c是字符设备文件，鼠标，键盘
b是块设备，如硬盘
s套接文件，如mysql启动时生成的mysql.sock

ln existingfile newfil       ###硬链接(hard link)  ##源文件删除后链接文件还可以读取
ln -s existingfile newfile   ###软链接(soft link)   ###源文件删除后链接文件同时失效

if [ -h $newfile ];then echo 111; fi       #判断是否是链接
readlink $newfile                          #读取链接的指向

linux文件夹
bin     可执行文件（命令）所有用户
boot     引导目录，内核保存于其中  
dev     被抽象为文件的硬件设配
etc     配置文件
usr     保存装的应用软件
root     root用户文件
home     用户私有数据
lib     库文件
sbin     可执行的二进制文件（超级用户才可执行）
media      挂载文件
mnt     挂载文件
opt     装大型软件（非强制）
proc     虚拟文件夹（保存在内存中的实时信息）
sys     底层硬件信息
var     保存经常变化的信息（如log，保存的是日志）
tmp     临时目录（系统会自动删除）

/etc/cron.daily/tmpwatch  tmp目录清空机制centos6以及以下

# centos7 清理配置
/usr/lib/tmpfiles.d/tmp.conf   

进程管理
ps -ef | grep java       ##查看有关与java的进程
pgrep java


service vsftpd start      ##启动程序
service vsftpd stop       ##结束进程
crontab -l               ##让使用者在固定时间或固定间隔执行程序之用
                        ## -l 查看 、-e 编辑
/var/log/cron            ##crontab日志
/var/spool/cron/        ##crontab 的信息，每个账号的调度对应一个文件，文件可以热加载（因而可能会被恶意利用，如通过写文件实现反弹shell）


##重启crond
service syslog stop                     ##系统的日志守护进程
service rsyslog restart                 ##sylog的增强版本，增加网络传输，远端的日志可以传输到本地
service syslog start
service crond restart

cat /etc/syslog.conf    #查看各个日志的对应路径

##linux日志
/var/log目录下

    
/var/log/messages       ##系统日志，记录各种事件   也可以用 logger 命令手动写日志进入

/var/log/secure         ##安全日志（记录账号的登陆断开信息，如果很大说明有人在试图破解密码？）

/var/log/wtmp           ##二进制日志，记录每个用户的登录次数和持续时间等信息
#查看
who /var/log/wtmp
last

/var/log/btmp           #二进制日志，记录用户登陆失败的信息   
#查看
lastb

/var/log/lastlog        #用于最后一次登陆的信息
#查看
lastlog


                                            
pidof ${command}        ##查看当前命令的pid            

kill -HUP ${pid}        ##程序可能自定义处理这些信号而不是结束进程，从而实现重新加载配置等操作，这需要程序支持才能如此
kill -SIGUSR1 ${pid}                
    
线程管理
ps -T                    ##查看所有线程
ps -T -p $pid            ##查看某个进程的线程
ps -eLo pid,lwp,psr,args | grep qemu   #第三列代表线程运行的第几个cpu


ps -xH   #查看所有线程


ps aux   
#rss  占用的物理内存，包含调用的.so共享文件
#vss  占用的虚拟内存


ps -eF
#SZ  由进程单独占用的物理内存
#PSR 进程占用的处理器数量
#STAT 线程、进程状态

D uninterruptible sleep (通常io使用)
R running or runnable (on run queue)
S interruptible sleep (waiting for an event to complete)
T stop
W paging(2.6+内核不适用)
X dead(不会被看到)
Z defunct ("zombie") process (终止但未被父进程回收)

< 高优先级
N 低优先级
L 在内存中
s is a session leader
l is mult-threaded
+ is in the foreground process group


ps -ely 



ps -U user_name   #查看用户当前运行的进程

ps -ejH   #查看进程树
ps axjf   

pstree $pid                ##查看进程、线程的层级
tree                    ##展示目录的树状结构

pstree -p $pid | awk -F"[()]" '{print $2}'| xargs kill -9            #杀死进程以及相关子进程


top                     ##使用子命令H查看线程，Tasks数增多

c cpu使用率排序
M 内存排序


ulimit -u                ##当前用户的最大线程数查看
ulimit -u 2048            ##修改当前用户的最大线程数


                        
prtconf -m          ##AIX查看物理内存
prtconf              ##查看物理参数
prtconf | more        ##分页查看                     
free -m               ##内存与swap查看   ###SWAP用作虚存分区
    
    total   总内存
    used    已经使用的内存
    free    空闲内存
    shared  当前废弃不用的内存
    buffer  buffer cache内存
    cached  page cache内存
    available 列显示还可以被应用程序使用的物理内存大小
    
    
    -buffer/cache =used-buffers-cached  程序占用的内存
    +buffer/cache =free+buffers+cached  可以挪用的内存（available大概估算）

    
    centos7
    total = used + free + buff/cache
    available = free + buff/cache



/proc/meminfo  #free命令信息来自于此


top                    ###查看系统运行状态   AIX使用topas
###top的内部命令 在执行top后输入
h    ##帮助说明
    %us user cpu time   执行用户进程的时间
    %sy system cpu time 在内核空间运行的cpu时间
    %ni user nice cpu time (% CPU time spent on low priority processes)
    %id idle cpu time
    %wa io wait cpu time (% CPU time spent in wait)
    %hi hardware irq (% CPU time spent serving/handling hardware interrupts)
    %si software irq (% CPU time spent serving/handling spftware interrupts)
    %st steal time (% CPU time in involuntary wait by virtual while hypervisor is servicing another processor)

    
    VIRT virtual memory usage  
    RES resident memory usage
    SHR shared memory 
    DATA 数据占用的内存
    
    RES-SHR  计算进程占用物理内存
    
    
    VIRT:
    It includes all code, data and shared libraries plus pages that have been swapped out and pages that have been mapped but not used.
    进程"需要"虚拟内存大小，包括进程使用的库、代码、数据。是一个假象的内存空间，在程序运行过程中虚拟内存空间中需要被访问的部分会被映射到物理内存空间中。虚拟内存空间大只能表示程序运行过程中可访问的空间比较大，不代表物理内存空间占用也大。

f 选择显示的内容    

    
cat /proc/stat            #%Cpu从此计算

cpu usage=(idle2-idle1)/(cpu2-cpu1)*100 
cpu usage=[(user_2 +sys_2+nice_2) - (user_1 + sys_1+nice_1)]/(total_2 - total_1)*100;
    
    
cat /proc/loadavg         # load average 从此计算   1=100%
    
lavg_1      1-分钟平均负载
lavg_5      5-分钟平均负载
lavg_15     15-分钟平均负载
nr_running  在采样时刻，运行队列的任务的数目，与/proc/stat的procs_running表示相同意思
nr_threads  在采样时刻，系统中活跃的任务的个数（不包括运行已经结束的任务）
last_pid    最大的pid值，包括轻量级进程，即线程。
 
 
Linux的系统负载指运行队列的平均长度，也就是等待CPU的平均进程数。 
    
Load值=CPU核数，这是最理想的状态，没有任何竞争，一个任务分配一个核，最充分利用cpu。实际情况应该低于 0.7*cpu核数。
  


  
time命令的输出
   
real/user/sys   
   
程序从开始到结束所经历的时间，也就是用户所感受到的时间。包括当前程序CPU的用时和所有延迟程序执行的因素的耗时总和（比如其他程序耗时，等待I/O完成耗时等）。
程序执行过程中在用户空间（user space）中所花费的所有时间，即程序用户模式下的CPU耗时。当前进程I/O阻塞的时间均不计在内。库代码调用仍然是在用户模式下。
程序执行过程中内核空间（kernel space）中所花费的时间，即程序在内核调用中的CPU耗时。   
   
   
   
    
iostat -d -x -k 1 10    ##查看io信息间隔一秒查询，查10次

-d #只显示disk的信息
-c #只显示cpu的信息

    %util  #在统计时间内（所有处理io的时间/总时间）

cat /proc/$pid/io      #查看进程的io的情况
    
pidstat -r -p PID      #查看进程的内存使用    
    
    
    
    
badblocks -s -v sdb1   ##坏道检测
hdparm sdb1               ##磁盘信息获取


sar                 ###系统活动信息

/proc/meminfo        ##内存信息
/proc/cpuinfo       ##查看CPU信息
/proc/interrupts    ##中断信息

cat /proc/cpuinfo | grep processor | wc -l   ##cpu核数


setup          ##进入图形化设置界面
xmanager     ###远程桌面软件，可以使用图形界面
eval        ###先扫描命令行进行变量替换，然后再执行命令  eval {command} $var

AIX  显示10个消耗cpu最多的进程
ps aux |head -1 ;ps aux |sort -rn +2 |head -10   ###修改【sort -rn +x】指定由第x+1列排序


ps -p pid -o lstart   #查看进程启动时间



ll /proc/PID    #查看进程的绝对路径

cwd 进程运行的目录
exe 执行程序的绝对路径
cmdline 程序运行的输入的命令
environ 进程运行时的环境变量
fd 进程打开或使用的文件符号连接


head -n 1  #前一行
head -c 1  #前一个字符

#最后一行
awk 'END {print}'
sed -n '$p'
sed '$!N;$!D'
awk '{b=$0}END{print b}'
#最后2行
awk '{b=a"\n"$0;a=$0}END{print b}'
#最后3行
awk '{b=a"\n"$0;a=c"\n"$0;c=$0}END{print b}'

/etc/rc.d/init.d/service_name    ### linux服务设置；如【service xxx start】为调用脚本时传入【start】参数

crontab  ####任务调度   设置可执行程序的定时运行
crontab -l   ###查看
crontab -e   ###编辑  使用方法与vi类似

开机启动设置
/etc/rc.d   ###/etc目录下的相关设置是链接    
##Linux在启动时，会自动执行/etc/rc.d目录下的初始化程序，可以把启动任务放到该目录下
rc.local是在完成所有初始化之后执行的


通过服务设置自启动   会修改/etc/rc.d/rcX.d 下面的链接
chmod +x /etc/rc.d/init.d/simpleTest    使之可直接执行
chkconfig --add simpleTest                把该服务添加到配置当中
chkconfig --list simpleTest                可以查看该服务进程的状态   显示不同级别的状态
chkconfig --del httpd                   删除
chkconfig --level httpd 2345 on         设置在哪些级别运行
chkconfig --level httpd 2345 off        设置在哪些级别关闭

/etc/rc.d/rc0.d                #运行级别为0的启动项 通过链接到/etc/rc.d/init.d/下的文件设置
/etc/rc.d/rc1.d                #运行级别为1的启动项


#centos7 service文件位置
systemctl
将server放入这个目录下，如mysqld.service
/usr/lib/systemd/system

#重新加载即可
systemctl daemon-reload
systemctl enable mysqld.service
systemctl is-enabled mysqld


##linux与window的文件传输 使用ZModem协议
sz  将选定的文件发送到本地
rz    交互窗口 rz -bey

FTP
vim /etc/vsftpd/chroot_list  
#将dengftp添加到此文件中，这样打开ftp 的时候自动定位到根目录下
service vsftpd restart 

ftp模式
! 执行外壳命令 如 !ls
delete
mdelete
put
mput
get
mget

dirname $path1/filename.txt            ###显示文件的父目录
pwd                                    ###显示当前目录



${command} > out.file 2>&1        ####将错误的输出定向到标准输出

0    标准输入。键盘输入，并返回在前端。
1    标准输出。正确返回值，输出到前端。【1>】可以直接表示成【>】， &1表示1通道
2    标准出错。错误返回值，输出到前端。

; 表示语句的结束，一行中出现多语句时使用


创建临时文件夹模拟回收站
myrm(){ D=/tmp/$(date +%Y%m%d%H%M%S); mkdir -p $D; mv "$@" $D && echo "moved to $D ok"; }
alias rm='myrm'
unalias commad    ###删除别名



filename1 -nt filename2   #文件filename1比filename2更新
filename1 -ot filename2   #文件filename1比filename2更旧

-z $string  字符长度为0
-n $string  字符长度非0


在shell中使用配置文件，使用filename文件中的变量
. filename



环境变量
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




shell执行方式
1、产生新的shell执行相应的shell scripts。
    使用方式是在scripts文件中加入  #!/bin/sh
2、不产生新的shell，在当前shell下执行一切命令。
    source命令，使用"."类似,当前进程执行
    exec以新的进程代替原来的进程，PID保持不变
加入【&】在执行脚本后面实现后台运行
nohup command_nam &  ##在后台运行命令command_name


setup         ##进入图形配置界面

ping           ##测试网络连接  
host、dig    ##测试DNS解析 
ip route     ##显示路由表
traceroute     ##追踪到达目标地址的网络路径 
mtr            ##网络质量测试 
hostname     ##查看主机名  【/etc/sysconfig/network】修改配置文件实现修改主机名，使用【hostname new_hostname】临时修改主机名

netperf     ##测试网络带宽


kill -l                     ##列出所有信号名称
stty -a                        ###查看信号对应的操作

stty size       #查看终端的大小


关闭ICMP回应(不能使用ping命令连接)

临时设置
#设置为0，开启；1，关闭
echo 0 >/proc/sys/net/ipv4/icmp_echo_ignore_all

永久设置
#vim /etc/sysctl.conf
net.ipv4.icmp_echo_ignore_all=1



开启器端路由转发功能
vi /etc/sysctl.conf
net.ipv4.ip_forward = 1

#将经过自己的流量转发到真正的目标地址
echo 1 > /proc/sys/net/ipv4/ip_forward
sysctl -w net.ipv4.ip_forward=1



md5sum             ##计算文件的MD5

sha1sum

sha256sum

base64编码
echo "AAA@#$" | base64
echo "QUFBQCMkCg==" | base64 -d


#编码转换 原utf8文件file1 转成gbk的file2
iconv -c -f utf-8 -t gbk file1 -o file2

#命令行中utf8转成gbk 需要预先设置好命令行的输入格式
echo -n "中文" | iconv -c -f utf-8 -t gbk


随机生成密码
date |md5sum

cat /dev/urandom | head -1 | md5sum 

openssl rand -base64 10


yum安装软件
yum (yellow dog update,modify)

yum install package_name ##使用yum安装软件，安装包在配置文件中指定
yum install vsftpd  ##安装软件，使用默认yum源
yum remove vsftpd   ##卸载软件
yum install --installroot=/usr/src/ vim   ###安装时指定安装路径
yum install software_name --enablerepo=repo_name 
###由指定yum源安装软件  【repo_name】对应/etc/yum.repos.d/下的文件中【[repo_name]】

main 定义了全局配置选项，整个yum 配置文件应该只有一个main。常位于/etc/yum.conf 中。
repository 每个源/服务器的具体配置，可以有一到多个。常位于/etc/yum.repos.d 目录下
【repository设置】
[serverid]   ##区别不同的repository
name=Some name for this server   ##对reporitory的描述
baseurl=url:##path/to/repository/  ###文件的获取路径，url可谓file、ftp、http三种
enabled=1  ##设置为可用
gpgcheck=1  ##可选，使用key检查安装包
gpgkey=file:##/etc/pki/rpm-gpg/RPM-GPG-KEY-oracle   ###设置key

yum update

验证
yum list all   ##查看yum设置是否正确，all可以为具体的包 

yum/rpm涉及key的位置
/etc/pki
yum --import /etc/pki/xxx...
rpm --import /etc/pki/xxx...

yum install -downloadonly -downloaddir=/xxx docker   #只下载，不安装
yum repolist   #查看repo
yum clean all  #清除缓存
yum makecache  #创建缓存



rpm安装
rpm -ivh package_name
rpm -ivh --relocate /=/opt/temp xxx.rpm    ###安装时指定安装路径
rpm -ivh --prefix= /opt/temp    xxx.rpm
rpm -qa | grep vsftp   ##查看是否安装软件
rpm -Uvh package_name  ##升级指定程序

rpm -i package.src.rpm        ##解压源码包，之后可以选择标准源码包安装相同操作
rpm -e package_name         ##删除包




负载均衡
lvs(linux virtual server)    不会影响后端节点的网络识别，依然识别最初始的客户端的ip，而不是分发器的ip
ipvsadm


haproxy


nginx


ipcmk -Q   ##创建message queue
 
ipcs -q    ##查看message queue



虚拟文件系统
#可用于对指定目录进行容量限制
dd if=/dev/zero of=/usr/disk-quota.ex4 count=4096 bs=1mb   #创建4G的文件
mkfs -t ext4 -F /usr/disk-quota.ex4   #创建文件系统   -F 强制，不会检查是否是设备文件
mount -o loop,rw,usrquota,grpquota /usr/disk-quota.ex4 /path/to/images/top/level    #挂载到容器目录


#traffic control 流量控制
tc




动态链接库
/etc/ld.so.conf
ldconfig



十六进制查看
vim vi中
:%!xxd         十六进制模式   
:%!xxd -r   文本模式

ctrl+f 前翻一页
ctrl+b 后翻一页


%所有行
!xxd  外部程序调用

hexdump -C file_name   #输出规范的十六进制和ASCII码
xxd


使用其他用户执行命令
sudo -u yhserver bin/mysqld_safe --defaults-file=etc/my_3306.cnf &
su - yhserver -c "bin/mysqld_safe --defaults-file=etc/my_3306.cnf &"


ipcmk
ipcs
ipcmr


编码转换
iconv



CPU控制
/sys/devices/system/cpu/

echo 0 > /sys/devices/system/cpu/cpu7/online    #禁用某个cpu



#日志滚动设置
#逐日存放日志
/etc/logrotate.d

copytruncate模式 copy完成到truncate完成的中间数据会丢失


###funny###
二维码生成

qrencode -o qr.png "string_seen_by_scan_qr"

nice #调整进程优先级别


#分割压缩文件
tar -zcvf ABCD.tar.gz ABCD | split -b 2000M -d -a 1 - ABCD.tar.gz

split -b 2000M -d -a 1 ABCD.tar.gz ABCD.tar.gz.

cat ABC.tar.gz.* | tar -zxv

#压缩过滤 多个目录可以用多个exclude
tar -zcvf abcd.tar.gz --exclude=abcd/def abcd

tar cvf - mypath | pigz -9 -p 3 > mypath.tgz
并发压缩

shc  将shell脚本编译成二进制二进制文件

file -i file_name  查看文件的编码，但是否为utf8-bom查看不出




##恢复
yum install e2fsprogs*
./configure
make && make install

fuser -m -u /u01            #identify processes using files or sockets  查看使用文件的进程，必须先杀死相关进程才能umount
umount /dev/sdb1
extundelete /dev/sdb1 --restore-all


tcpdump 导出后的文件可以使用wireshark打开



#######################################################################################################################
dos2unix    #dos的文本转换成unix的



#####################################
GPU

lspci | grep -i vga      #查看显卡信息

lshw -C display


#DNS设置
/etc/resolv.conf


#########################################
ELF  类Unix操作系统的二进制文件标准格式

00000000  7f 45 4c 46 02 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|

头部恒为“.ELF”




##第一个进程执行
flock -n /tmp/.my.lock -c 'sleep 10 && echo 111'     

##另外一个进程执行 获取锁失败 直接退出
flock -n /tmp/.my.lock -c 'sleep 10 && echo 111'  


##第一个进程执行
flock -s /tmp/.my.lock -c 'sleep 10 && echo 111'     

##另外一个进程执行，同时获取到锁
flock -s /tmp/.my.lock -c 'sleep 10 && echo 111'  



##第一个进程执行
flock -x /tmp/.my.lock -c 'sleep 10 && echo 111'     

##另外一个进程执行 需要等待第一个进程直接结束才能获取到锁
flock -x /tmp/.my.lock -c 'sleep 10 && echo 111'  

      
#共享锁和排它锁不能同时存在 
#如果出现，则跟两个排它锁情况一致



#使用文件描述符实现锁
lock() {
  exec 7<>.lock
  flock -n 7 || {
    echo "Waiting for lock to release..."
    flock 7
  }
}

#加锁
lock

#释放锁
flock -u 7


# 将文件缩小到指定大小，可以避免直接rm造成的io挤占
truncate ${filename} -s 524280000

