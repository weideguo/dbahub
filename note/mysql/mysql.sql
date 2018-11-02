参考文档
http://dev.mysql.com/doc/


mysql --prompt="what_to_prompt"
\\u		用户名
\\h		主机名
\\p		端口
\\d		数据库名
\\r		时间


help command_name;  ----查询命令的使用格式

select user();   ----查询当前用户
select now(); 	 ----查询当前时间

status										----查看数据库的状态
show status
show engines;  								-----查看提供的引擎
show variables like '%storage_engine%';  	----查看存储引擎
show create table table_name;  				-----查看某个表的创表语句，可查看使用的引擎
show table status like "%table_name%"\G     -----查看表的状态信息

show variables like '%port%';    			----查看端口信息
show variables like '%version%';    		----查看版本
show warnings\G;   							---显示告警
show errors\G



flush hosts;        ----清空主机缓存，当ip发生改变需要执行，以及清空连接失败的计数
FLUSH LOGS;			----closes and reopens all log files

	flush BINARY logs;
	flush ENGINE logs;
	flush ERROR logs;
	flush GENERAL logs;
	flush RELAY logs;
	flush SLOW logs;


	
	
	

quit  ---退出客户端


show open status

desc table_name										--查看表字段
show fields from table_name like column_name;		--查看特定字段

select now()			--时间
select sysdate()

----查看连接信息
show processlist;   		   				
show full processlist;   			
mysqladmin -u roo -p processlist
select id from information_schema.processlist where user='root'; 

kill id   ---终止连接（在mysql中执行），information_schema.processlist的id


show variable like 'wait_timeout'               ---空闲连接的在被关闭前的秒
net_read_timeout                     			---The number of seconds to wait for more data from a connection before aborting the read.
net_write_timeout                    			---The number of seconds to wait for a block to be written to a connection before aborting the write.
connect_timeout									---The number of seconds that the mysqld server waits for a connect packet before responding with Bad handshake
slave-net-timeout								---The number of seconds to wait for more data from the master before the slave considers the connection broken, aborts the read, and tries to reconnect.



在不同的时间段查询两次取差值
show status like 'queries'
QPS=(Q1-Q2)/time

questions也可以做一定的衡量，不包含存储过程执行的语句



show status like 'Com_commit'
show status like 'Com_rollback'
TPS=(CC1+CR1-CC2-CR2)/time


状态
show global status like 'Max_used_connections'  ---查看历史最大连接数  
show global status like 'Threads_connected'		---查看当前连接数
show global variables max_connections         	----最大连接数
show global variables max_user_connection 	 	----单个用户最大连接数




设置实例参数
1.修改my.cnf文件并重启
2.设置全局变量
	set global variables_name=variables_value;
3.设置会话变量
	set [local|session] variables_name=variables_value;
4.会话变量设置为全局变量的值
	set @@session.wait_timeout=@@global.wait_timeout;	
	

存储引擎
存储引擎/插件安装/卸载
SHOW VARIABLES LIKE 'plugin_dir';  				---查看共享库
INSTALL PLUGIN archive SONAME 'ha_archive.so';  ---安装存储引擎 【ha_archive.so】为共享库下的动态链接库文件
UNINSTALL PLUGIN archive;   					---卸载存储引擎 【show plugins】

select * from mysql.plugin;


#在启动中安装
plugin_load=xxxx.so     ##指定加载动态库


proxy权限
install plugin auth_test_plugin soname 'auth_test_plugin.so' 
create user 'user2'@'host2' identified with auth_test_plugin soname as 'user1'@'user2';    
--proxy_user只读参数，显示当前用户所使用的代理账号




CREATE TABLE t1 (c1 INT PRIMARY KEY) DATA DIRECTORY = '/alternative/directory';   --创建表时指定数据文件路径

ln -s existingfile newfile			---使用连接重定向数据文件，系统命令，只能对MyISAM的数据文件使用（数据文件[.myd]和索引文件[.myi]，格式文件[.fem]不能使用连接）


create temporary table tmp_tablename ...        ---创建临时表，mysql临时表只在当前会话有效，结束会话临时表就被drop。mysql只有会话级临时表，没有事务级临时表。




创表时指定存储引擎
create table table_name() engine=myisam;

innoDB 存储引擎
	show variables like 'inndb%log%';   ----innoDB相关的日志
	.frm  表的结构定义
	.idb  表空间的数据文件     ---当启用多用表空间时，每个表会生成与表名相同的数据文件	
	
	
	row_format={compressed | dynamic}   ---创建时指定存储格式
	
	COMPACT    默认，性能瓶颈不在CPU时性能可以提高
	REDUNDANT  兼容旧版本
	DYNAMIC    COMPACT的衍生，变长存储
	COMPRESSED COMPACT的衍生，压缩存储
	
	
	innodb使用系统表空间存储内部数据字典及undo日志，所以使用多重表空间时数据文件(.ibd)不能随意移动
	
	rename table db1.table_name db2.table_name;    ---将表从一个数据库移动到另外一个数据库，只是修改数据字典中的定义而已
	
	
	ib_logfile   ---redo日志
	ib_data      ---系统表空间数据文件
	ibdata
	
	
	系统表空间
		数据字典                     ---innodb的
		doublewrite buffer           ---数据页写到数据文件前，innodb先写到doublewrite buffer，完全写入doublewrite buffer后数据才写入到数据文件中。    
		change buffer				 ---更改的二级索引缓存，由buffer bool转写到系统表空间以防止丢失，回写到表空间后会清理
		undo logs (可以设置使用单独的数据文件而不再系统表空间中)
		表的数据(启用多重表空间时表的数据在单独的表空间) --innodb的
	
	
	doublewrite={0|1}
		0 不启用二次写
		1 启用二次写，数据被写到磁盘两次
	
	change buffer
		A special data structure that records changes to pages in secondary indexes.
		DML语句的结果。
		Changes are only recorded in the change buffer when the relevant page from the secondary index is not in the buffer pool.改变非聚集索引的数据，所在的页不在内存中。
		包含delete buffering, insert buffering, purge buffering。(5.5之前只有insert buffering)
	innodb_change_buffering={none|inserts|deletes|changes|purges|all}  ---默认all
	innodb_change_buffer_max_size={0~50}  --默认25
		change buffer占用buffer pool的比例
	
	
	
	配置参数
	innodb_file_per_table=1   ---启用多重表空间，有一个表对应一个表空间  为0时为使用独立表空间文件，只有一个表空间，为系统表空间，但可以有多个数据文件  系统表空间总是存在
	
	---启动后更改只对更改后的表生效
	
	---使用独立的undo表空间，必须在数据库创建前指定
	innodb_undo_directory     ---指定undo日志的目录
	innodb_undo_tablespaces   ---指定undo表空间数量
	
	innodb_log_group_home_dir ---指定redo日志文件的目录 默认为data目录
	innodb_log_file_size	  ---指定redo日志文件的大小	
	innodb_log_file_in_group  ---指定redo日志文件组的数量 
	
	---不启用多重表空间时，可以选择设置如下
	innodb_data_home_dir      ---指定系统表空间数据文件保存的目录
	innodb_data_file_path=datafile_spec[;datafile_spec1...]  	  ---系统表空间的数据文件  datafile_spec=file_name:file_size[:autoextend[:max:max_file_size]]
	
	innodb_flush_log_at_trx_commit={0|1|2}   ---默认为1
	0 每秒刷新log buffer
	1 每次事务提交时log buffer写入log file，并刷新到磁盘
	2 每次事务提交后或者每秒刷新log buffer
	
	sync_binlog=n  ---0~4294967295为数字
	在n次提交后binlog刷新到磁盘
	0 提交时binlog不同步到磁盘
	1 每次提交写将binglog写到磁盘
	
	innodb_fast_shutdown={0 | 1 | 2}    ---默认为 1
	0 中止新的连接，等待会话关闭、事务结束，将缓冲区的数据写入磁盘。		对应oracle: shutdown normal
	1 中止新的连接，关闭会话，将提交的数据写入数据文件，未提交的事务回滚。  对应oracle: shutdown immediate
	2 中止新的连接，关闭会话，忽略当前所有操作。重启需要执行故障恢复，重新读取日志文件，回滚未提交的事务等。 	对应oracle: shutdown abort
	
	
	可移植表空间
		--启用多重表空间
		--创建相同结构的表，抛弃表空间
		ALTER TABLE tbl_name DISCARD TABLESPACE;
		--使用元有的数据文件导入表空间
		ALTER TABLE tbl_name IMPORT TABLESPACE;
	
	
	
ISAM (Indexed Sequential Access Method) 索引顺序访问方法
MyISAM 存储引擎
	.myi 索引文件
	.myd 数据文件
	.frm 存储表定义

	存储格式 
	fixed 		定长/静态   不包含变长的列(varchar/varbinary/blob/text)
	dynamic 	动态		
	compressed  压缩        创建只能使用myisampack，解压使用myisamchk，表是只读格式
	fixed/dynamic创表时自动适配
	row_format={fixed | dynamic}    ---创表时选择强制指定
	
	
	myisamchk -ei table_name.myi  ---查看表的统计信息
	myisamchk -ed table_name.myi  ---查看表表对象的链接数
	
	
	
	
csv存储引擎 
	
	.csv 数据文件 以逗号分隔符存储

db.opt  指定数据库的字符集和排序使用的字符集
	
	
MyISAM和innodb区别
MyISAM
不支持事务
查询、写入比innodb快
只有表锁
不支持外键
内存只加载索引的数据（叶子页和非叶子页），表的数据不加载

If a MyISAM table has no holes in the data file (deleted rows in the middle), an INSERT statement can be executed to add rows to the end of the table at the same time that SELECT statements are reading rows from the table. 
If there are multiple INSERT statements, they are queued and performed in sequence, concurrently with the SELECT statements. 
新数据会被附加到数据文件的结尾，如果时常做一些UPDATE，DELETE操作之后，数据文件就不再是连续的，就是数据文件里出现了很多洞洞。
concurrent_insert=0时，不允许并发插入功能。 
concurrent_insert=1时，允许对没有洞洞的表使用并发插入，新数据位于数据文件结尾（缺省）。 
concurrent_insert=2时，不管表有没有洞洞，都允许在数据文件结尾并发插入。 

堆表
索引的叶子几点记录表的地址（逻辑地址，移动文件之后索引依旧可以使用），由此实现回表查询。

innodb
支持事务	
行锁、表锁	
支持外键	
内存加载索引以及表的数据，可以通过自适应hash技术实现在内存中实现回表查询

索引组织表
二级索引的叶子节点记录主键，由此查询clustr索引（即主键索引，innodb由主键组织存放）实现回表查询。


索引
fulltext索引   ----只有myisam使用
CREATE TABLE fulltext_sample(name TEXT,FULLTEXT(name)) ENGINE=MyISAM;
ALTER TABLE fulltext_sample ADD FULLTEXT(name);   ----改表结构添加全文索引
create fulltext index index_name on fulltext_sample(name);   

alter table table_name drop index index_name;

show index from table_name;

show keys from table_name;

前缀索引
alter table table_name add key(column_name(prefix_length))
create index index_name on table_name(column_name(prefix_length))
	
create index index_name USING {BTREE | HASH} on tbl_name (index_col_name,...) ...

b树索引
	 用于=, >, >=, <, <=, or BETWEEN
	 LIKE比较不能以通配符开始
	 IS NULL可以使用索引
	 Any index that does not span all AND levels in the WHERE clause is not used to optimize the query. In other words, to be able to use an index, a prefix of the index must be used in every AND group.

	 最左原则
	 if you have a three-column index on (col1, col2, col3), you have indexed search capabilities on (col1), (col1, col2), and (col1, col2, col3). 
	 
hash索引
	只能用于= or <=> ,返回单条记录
	不能用于加快ORDER BY
	Only whole keys can be used to search for a row
	
	
	
	
	
windows下
	启动mysql服务
		运行mysqld命令，命令位于bin目录下  mysqld 
	关闭mysql
		mysqladmin -u root -p shutdowmn ---root可以为其他有关闭权限的mysql用户
	登录mysql
		mysql -u root -p     
		【-h hostname -P port_num】---指定服务器及端口号
		【-S socket_file】  ---指定socket文件  
linux
	启动mysql服务
		mysqld或mysqld_safe或mysqld_multi
		mysqld_safe --defaults-file=/my.cnf   ----指定配置文件的位置，也可以使用【mysqld】命令启动
	运行系统命令
		system {sys_command}    ----{sys_command}为系统命令
		system clear   ---清屏 

mysqld --ship-grant-tables     -----安全模式启动  可用于在忘记密码时进行修改
	
mysqld_multi --defualts-extra-file=my.cnf start 1,2,3
---	启动对个实例，需要使用不同端口、数据文件等
1,2,3 对应配置文件my.cnf中[server1] [server2] [server3]

		
my.cnf文件 --windows下为my.ini  
---启动参数文件，默认设置端口号为3306

---linux下查看使用的启动参数文件
mysql --help | grep my.cnf
---查看启动参数文件使用优先级
mysqld --verbose --help |grep -A 1 'Default options' 



强制启动
innodb_force_recovery={0-6}    
	0 	--默认 正常启动，有crash recovery过程
	1	
	2
	3
	4
	5
	6

跳过回滚
杀死mysql，使用	innodb_force_recovery=3 启动
	
myisam-recover-options    #启动时恢复myisam表
	
	
使用密码文件登录
#mysql5.6后支持
mysql_config_editor set --help		
mysql_config_editor set --login-path=fastlogin --user=root --host=localhost --password --socket=/u02/mysql/data/my.sock	       ---- 在当前账号的家目录下生成一个隐藏加密文件.mylogin.cnf  
mysql_config_editor print --all     ----查询创建的加密文件

mysql --login-path=fastlogin   		----使用创建的密码文件登录		
		

		
查询命令的使用格式
mysql  --help
mysqld --help
mysqladmin  --help		

perror err_code   ----查询错误代码的解释

命令行中
help contents  #由此提示逐层查看相关命令



----参数
prompt		设置命令行的提示符，可以在使用mysql命令你时加入，也可以再配置文件中[mysql]块下加入


MySQL用户管理
用户信息保存在 mysql.user表中
	mysql.user的host字段
	所有主机：%
	精确的主机或IP地址：www.weideguocom 或 192.168.1.1
	使用"*"通配符：*.weideugo.com
	指定同一网段： 192.168.1.0/255.255.255
	
mysql.uesr			---实例的权限
mysql.db 			---存储数据库的权限
mysql.tables_priv	---表的权限
	
	
---创建用户
create user user_name identified by user_password;
create user user_name@'host_ip' identified by user_password;  --设置用户并限定登陆ip或主机名，
RENAME USER old_name TO new_name;   ----更改用户名

---更改密码
set password [for user_name]=password('user_password');
update mysql.user set password=password('user_password') where user='user_name';

GRANT	授予权限
REVOKE	撤销权限

GRANT ALL PRIVILEGES ON *.* to 'weideguo'@'%' identified by 'weideguo' [with grant option] 
REVOKE ALL PRIVILEGES on *.* FROM weideguo;

--不要直接更改mysql.user表，因为更改的命令会被明文保存到日志 

--密码会被修改保存到日志的语句
CREATE USER ... IDENTIFIED BY ...
ALTER USER ... IDENTIFIED BY ...  				--5.7之后才有
GRANT ... IDENTIFIED BY ...
SET PASSWORD ...
SLAVE START ... PASSWORD = ...
CREATE SERVER ... OPTIONS(... PASSWORD ...)
ALTER SERVER ... OPTIONS(... PASSWORD ...)


grant usage on ...       --usage 代表无权限，用于在创建用户时使用

flush privileges	---使修改的权限生效
show grants			---查看当前用户被授予的权限
show grants for db_user;

show privileges     ---查看所有的权限

mysql.db			---数据库的权限

时区
system_time_zone                  --服务器的时区，，默认由操作系统确定，不可以动态修改						  
set global time_zone="+8:00"      --数据库实例当前的时区，设置后即影响mysql的时间，默认与system_time_zone一致
set time_zone="+8:00"						  


字符集
数据库保存相同内容所占用的空间大小、数据库与客户端通信

SHOW CHARACTER SET;   ---查看MySQL支持的字符集：
show collation;       ---查看排序字符集
编码属性：
character set		存储使用的字符集
collation			排序、对比使用的字符集
查看MySQL当前使用的字符集：
SHOW VARIABLES LIKE "characrer_set%"
SHOW VARIABLES LIKE "collation%"

--创建数据库时指定默认字符集：
CREATE DATABASE database_name DEFAULT CHARACTER SET char_set1 DEFAULT COLLATION char_set2;
--修改字符集
ALTER  DATABASE database_name CHARACTER SET char_set1 COLLATION char_set2;	--修改数据库默认的字符集：
alter table table_name convert to character set char_set1;			--转换表的默认字符集，已有的数据会被转变，如果表的转换存储字符集不兼容，可能导致数据丢失
alter table table_name DEFAULT CHARSET=utf8;                                    --To change only the default character set for a table
alter table table_name change column_name1 column_name1 blob;


latin1 	单字节编码
GBK     中文二字节，英文一字节
utf8	中文三字节，英文一字节

skip-character-set-client-handshake   --mysql --default-character-set无效，连接使用默认编码

设置MySQL默认编码：配置文件中
[client]
default-character-set=utf8
[mysql]
default-character-set=utf8
[mysqld]    
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'             ----客户端连接的时候执行命令"set names utf8",也可以使其他命令,对super用户无效
character-set-server = utf8


	
大小写
lower_case_table_names=[0|1|2]      
If set to 0, table names are stored as specified and comparisons are case sensitive. 
If set to 1, table names are stored in lowercase on disk and comparisons are not case sensitive. 
If set to 2, table names are stored as given but compared in lowercase. 
This option also applies to database names and table aliases. 

内容大小写敏感
创建表时指

column_name varchar(100) binary    ---由binary指定大小写敏感


	
正则表达式
select * from table_name where column_name regexp 'regular_expression';		

select * from mysql.user\G   -----查询结果按列打印
	
use database_name;   ---切换数据库

表复制
Insert into Table2(field1,field2,...) select value1,value2,... from Table1 ---要求table2存在
select value1,value2 into table2 from table1;   --要求table2不存在

---将命令即输出写入文件中
tee file_name.txt
...
notee

修改系统参数
set global var_name=var_value;    ---var_name参数名  var_value参数值
set var_name=var_value;     ----重启失效


set autocommit={on|off}  ---设置是否自动提交事务

事务
start transaction;   ----开始事务
...
commit;    ----提交事务   ---rollback回滚事务


SAVEPOINT identifier
ROLLBACK [WORK] TO [SAVEPOINT] identifier
RELEASE SAVEPOINT identifier



隔离级别

SET [GLOBAL | SESSION] TRANSACTION
    transaction_characteristic [, transaction_characteristic] ...

transaction_characteristic:
    ISOLATION LEVEL tx_level
  | READ WRITE
  | READ ONLY

tx_level:
     REPEATABLE READ
   | READ COMMITTED
   | READ UNCOMMITTED
   | SERIALIZABLE


select @@tx_isolation;    ---查询隔离级别
SET GLOBAL tx_isolation='READ-UNCOMMITTED';   -----设置隔离级别
READ-UNCOMMITTED     ---未提交读。幻想读、不可重复读和脏读都允许。
READ-COMMITTED		 ---已提交读。允许幻想读、不可重复读，不允许脏读
REPEATABLE-READ		 ---可重复读。允许幻想读，不允许不可重复读和脏读
SERIALIZABLE		 ---可串行化。幻想读、不可重复读和脏读都不允许。读加共享锁，写加排他锁，读写互斥，使用的悲观锁的理论


1.幻想读：
	事务T1读取一条指定where条件的语句，返回结果集。
	事务T2插入一行新记录，恰好满足T1的where条件。
	然后T1使用相同的条件再次查询，结果集中可以看到T2插入的记录，这条新纪录就是幻想读。
2.不可重复读取：
	事务T1读取一行记录，
	紧接着事务T2修改了T1刚刚读取的记录，
	然后T1再次查询，发现与第一次读取的记录不同，这称为不可重复读。
3.脏读：
	事务T1更新了一行记录，还未提交所做的修改，
	这个T2读取了更新后的数据，
	然后T1执行回滚操作，取消刚才的修改，
	所以T2所读取的行就无效，也就是脏数据。


MVCC(Multi-Version Concurrency Control) 多版本并发控制
read没有阻塞write, 使用MVCC的技术解决了write/read相互阻塞的问题

而对开启MVCC机制的锁，叫做乐观锁，大多基于数据版本(Version)记录机制实现

MVCC的一种简单实现是基于CAS(Compare-and-swap)思想的有条件更新(Conditional Update)


乐观锁
提交事务时验证 


悲观锁
提交事务前验证，执行语句时验证


latches   闩
    Mutexes and rw-locks are known collectively as latches.
    
    Mutex(mutual exclusion)  
        represent and enforce exclusive-access locks to internal in-memory data structures
    
    rw-lock 
        represent and enforce shared-access locks to internal in-memory data structures.



        
record-level lock：
record lock		--锁住一行记录(行锁)
gap lock 		--锁住一段范围的记录(间隙锁)
next-key lock	--前两者效果的叠加



innodb的锁

Shared Locks Exclusive Locks
	A shared (S) lock permits the transaction that holds the lock to read a row.
	An exclusive (X) lock permits the transaction that holds the lock to update or delete a row.
	
Intention Locks
	Intention shared (IS): Transaction T intends to set S locks on individual rows in table t.
	Intention exclusive (IX): Transaction T intends to set X locks on those rows.

Record Locks
	Record locks always lock index records, even if a table is defined with no indexes.
	锁加在索引记录上。
	SELECT c1 FROM t WHERE c1 = 10 FOR UPDATE;				---当条件列存在索引时，只锁住所选的范围；当不存在，锁全表
	
Gap Locks
	锁索引记录间隙。对隔离级别为RR以上的才有效。
	SELECT c1 FROM t WHERE c1 BETWEEN 10 and 20 FOR UPDATE; 
	--prevents other transactions from inserting a value of 15 into column demo.id, 
	--whether or not there was already any such value in the column, 
	--because the gaps between all existing values in the range are locked.

	--间隙锁可以没有锁冲突，可以同时存在排他锁
	
	(Gap locking is not needed for statements that lock rows using a unique index to search for a unique row.
	 This does not include the case that the search condition includes only some columns of a multiple-column unique index; in that case, gap locking does occur.)
	
Next-Key Locks
	record locks和gap locks的叠加
	存在索引，锁定下开上闭的区间。
		create table test1(id int);
		create index i_test1 on test1(id);
		insert into test1 values(1),(5),(7),(15),(19);
		
		session1
		delete from test1 where id=7;   ----将锁住[5,15)的区间	
	
it sets shared or exclusive locks on the index records it encounters.row-level locks are actually index-record locks.
a next-key lock is an index-record lock plus a gap lock on the gap preceding the index record. 
因为innodb对于非唯一索引锁的方式是通过索引上连续存在的键实现的？
如索引存在（94，96，102，200）  则>100要锁住（96，+∞），如果innodb_locks_unsafe_for_binlog=1，则导致只锁住（102，+∞）
						  
Insert Intention Locks
	An insert intention lock is a type of gap lock set by INSERT operations prior to row insertion.


AUTO-INC Locks				   	 ---表中有auto_increment键时在插入产生的锁
	【innodb_autoinc_lock_mode】 ---变量确定自动增长锁类型
	


SELECT ... LOCK IN SHARE MODE;		----- sets an IS lock
SELECT ... FOR UPDATE;				----- sets an IX lock  ??
If you use 【FOR UPDATE】 with a storage engine that uses page or row locks, rows examined by the query are write-locked until the end of the current transaction. 
Using 【LOCK IN SHARE MODE】 sets a shared lock that permits other transactions to read the examined rows but not to update or delete them

---【commit】【rollback】会释放【FOR UPDATE】、【LOCK IN SHARE MODE】锁

读写分离

设置只读
set global read_only=1;   	    ----1为只读；0为读写；super用户依然可以写入

-----解锁
unlock tables;     				---开启事务先前有【lock tables】时，解锁时隐式提交事务


flush tables;   --刷数据到磁盘

---加锁
flush tables with read lock;    						----全局锁。锁住所有的表。加锁实现super用户也不能写入

FLUSH TABLES tbl_name [, tbl_name] ... WITH READ LOCK;	---对指定的表加锁
LOCK TABLES `table_name` WRITE;							---添加写锁，其他事务不可再加锁，其他事务不能读表
lock tables `table_name` read;							---添加读锁，其他事务可以再加读锁，其他事务可以读表

select * from table_name where ... for update;   


---一个会话只能同时有一个锁，以最后加的锁为当前状态；
---开启事务【start transaction】时会释放会话拥有的锁
---加锁时隐式提交会话先前的事务
LOCK TABLES												
    tbl_name [[AS] alias] lock_type
    [, tbl_name [[AS] alias] lock_type] ...

lock_type:
    READ [LOCAL]				--获取读锁
  | [LOW_PRIORITY] WRITE		--获取写锁


  
锁等待时间
--由锁造成等待时，等待多久才发出超时错误
lock_wait_timeout


死锁解决
等待超时。
杀死连接。【show processlist】【kill id】


When you call 【LOCK TABLES】, InnoDB internally takes its own table lock, and MySQL takes its own table lock.
InnoDB releases its internal table lock at the next commit, but for MySQL to release its table lock，you have to call 【UNLOCK TABLES】. 
You should not have 【autocommit = 1】, because then InnoDB releases its internal table lock immediately after the call of LOCK TABLES, and deadlocks can very easily happen.



---innodb有可能产生锁的语句
SELECT ... FROM
SELECT ... FROM ... LOCK IN SHARE MODE 
SELECT ... FROM ... FOR UPDATE 
UPDATE ... WHERE ... 
DELETE FROM ... WHERE ... 
INSERT 
INSERT ... ON DUPLICATE KEY UPDATE 
REPLACE
INSERT INTO T SELECT ... FROM S WHERE ...    
CREATE TABLE ... SELECT ...   
LOCK TABLES 

INSERT ... SELECT 
MyISAM that employs table-level locks locks all partitions of the target table; InnoDB that employ row-level locking.

CREATE ... SELECT
To ensure that the binary log can be used to re-create the original tables, MySQL does not permit concurrent inserts during CREATE TABLE ... SELECT.


mysql mem = 
  key_buffer_size 						--缓存MyISAM的Index block		   
+ innodb_buffer_pool_size               --innodb的缓冲，缓冲数据和索引      
+ innodb_additional_mem_pool_size       --用于存放数据字典等的内存池        
+ innodb_log_buffer_size                --日志的缓冲（ ib_logfile files that make up the redo log）       

+ query_cache_size                      --The amount of memory allocated for caching query results       
+ tmp_table_size                        --maximum size of internal in-memory temporary tables 

+
  max_connections 						--最大连接数
* (read_buffer_size 					--顺序读取数据缓存区 
+ read_rnd_buffer_size         			--随机读取数据
+ sort_buffer_size                      --
+ join_buffer_size                      --
+ binlog_cache_size                     --
+ thread_stack           				--存放线程的信息   
)



使用的内存 show status
Innodb_buffer_pool_bytes_data 
Innodb_buffer_pool_pages_misc=Innodb_buffer_pool_pages_total ? Innodb_buffer_pool_pages_free ? Innodb_buffer_pool_pages_data

当使用压缩表的时候Innodb_buffer_pool_pages_data大于Innodb_buffer_pool_pages_total    （bug）

压缩表
create table (...) row_format=compressed 


innodb命中
=innodb_buffer_pool_read_requests/(innodb_buffer_pool_read_requests+innodb_buffer_pool_read_ahead+innodb_buffer_pool_reads)

Innodb_buffer_pool_read_ahead_rnd          --The number of "random" read-aheads initiated by InnoDB. This happens when a query scans a large portion of a table but in random order.
Innodb_buffer_pool_read_ahead              --The number of pages read into the InnoDB buffer pool by the read-ahead background thread
Innodb_buffer_pool_read_ahead_evicted      --The number of pages read into the InnoDB buffer pool by the read-ahead background thread that were subsequently evicted without having been accessed by queries.
Innodb_buffer_pool_read_requests           --从innodb buffer中读数据
Innodb_buffer_pool_reads                   --从磁盘读数据到innodb buffer

myisam不命中率
=Key_reads/Key_read_requests.



Key_reads/Key_read_requests 
--ratio should normally be less than 0.01

Key_writes/Key_write_requests 
--near 1 if you are using mostly updates and deletes, 
--but might be much smaller if you tend to do updates that affectmany rows at the same time 
--or if you are using the DELAY_KEY_WRITE table option.


myisam正在使用的内存
1 - ((Key_blocks_unused * key_cache_block_size) / key_buffer_size)

Key_blocks_used    #使用block的高水位线(hight-water mark)



参数优化
myisam
key_buffer_size 	--缓存MyISAM的Index block	
open_table_cache    --可以由状态Opened_tables确定，


innodb
innodb_buffer_pool_instances            --buffer pool个数，innodb_buffer_pool_size超过G时可以提高并发性能


随机读取 如无法使用索引时的全表扫描
顺序读取 数据块的读取需要满足一定的顺序，如根据索引信息读取数据

mysql定位过程：
打开索引->根据索引键值逐层找B+树branch节点->定位到叶子节点，将cursor定位到满足条件的rec上


adaptive hash index(自适应哈希索引)
	engine取数据后，将cursor的位置保存起来，取下一条数据时，先恢复cursor的位置，成功则直接取数，不成功则重新定位cursor的位置。存储于hash_table的内存中，位于buffer pool。
	the hash index is always built based on an existing B-tree index on the table. 
	innodb_adaptive_hash_index={on|off}  --默认启用

	大量多表jion、模糊查询不建议使用AHI



linux下编译安装
5.0/5.1
./configure --prefix=instal_path
make
make install
bin/mysql_install_db --basedir=/u05/mysql5172 --datadir=data


(5.5/5.6)
cmake   ---需要配置其他参数   									   
make										 
make install								   
scripts/mysql_install_db --datadir=data_path    -----5.5/5.6初始化数据库，必须指定数据文件的路径  在mysql安装的根目录执行  默认读取/etc/my.cnf的配置
scripts/mysql_install_db --defaults-file=where_you_my.cnf     ----如果有参数文件，直接用参数文件  

cmake . -DCMAKE_INSTALL_PREFIX=/u01/mysql		     	
		-DSYSCONFDIR=/u01/mysql/data
		-DMYSQL_DATADIR=/u01/mysql/data
		-DMYSQL_UNIX_ADDR=/u01/mysql/data/mysqld.sock
		

default_setting		

-DCMAKE_INSTALL_PREFIX=$prefix			---安装目录，默认为/usr
-DINSTALL_SBINDIR=$prefix/bin			---可执行文件路径
-DSYSCONFDIR=/etc/my.cnf				----配置文件的目录
-DMTSQL_DATADIR=/var/lib/mysql			----数据文件路径
-DMYSQL_UNIX_ADDR=/tmp/mysqld.sock		----socket文件				
-DMYSQL_USER=mysql						----默认用户
-DEFAULT_CHARSET=utf-8
-DEFAULT_COLLATION=utf8_general_ci
-DEABLED_LOCAL_INFILE=ON				----本地文件导入支持
-DWITH_INNOBASE_STROTAGE_ENGINE=1
-DWITH_PARTION_STORAGE_ENEGINE=1
-DWITH_PERFSCHEMA_STORAGE_ENGINE=1
-DWITH_READLINE=ON
-DWITH_SSL={ssl_type|path_name}			----启用SSL


-DWITH_BOOST=xxx           --指定boost的目录

-DWITH_SSL=system           --编译中加入ssl
-DWITH_SSL=path_name



5.7/5.8初始化数据库
----随机生成密码存放在错误日志中
mysqld --defaults-file=my.cnf --initialize


cmake . -LH    ---查看cmake的选项


备份 
mysqlhotcopy    ----只能用于MyISAM、ARCHIVE引擎的联机热备份
mysqldump   	----导出成SQL文件或平面文件备份   --执行SQL脚本命令【source】【 mysql < filename.sql 】
mysqlbinlog		----查看二进制文件以供备份
xtrabackup/innobackupex      ----使用第三方开源软件进行备份和恢复


--账户需要有select、lock tables权限
mysqldump -u root -pyy123456 -h 10.104.220.123 -P 3306 nwebauth -R > nwebauth.sql   ----【-R】配备存储、函数过程


	--master-data[=1|2]		----导出中带有change master to... 语句
	-t					---不导出建表语句
	-d					---不导出插入数据语句
	-T	--tab=name		---将表以分割文件导出
	-X					---导出成xml结构
	--add-drop-table=false  ---不导出drop table if exist语句
	--single-transaction              	
		一致性导出，以单事务导出
		ALTER TABLE, DROP TABLE, RENAME TABLE,TRUNCATE TABLE 会对导出有影响
		This option sets the transaction isolation mode to REPEATABLE READ and 
		sends a START TRANSACTION SQL statement to the server before dumping data. 
		
	--quick
		 It forces mysqldump to retrieve rows for a table from the server a row at a time rather than 
		 retrieving the entire row set and buffering it in memory before writing it out.
	
	To dump large tables, combine the --single-transaction option with the --quick option.
	
	--lock-all-tables					
		Locks all tables across all databases.  锁定实例所有库的表
		
	--lock-tables
		Lock all tables for read. 锁定单个库的所有表
		For each dumped database, lock all tables to be dumped before dumping them.
		
	--add-locks         
		Add locks around INSERT statements. 导出sql中带有lock语句
	
	--set-gtid-purged={on|off|auto}     -----SET @@GLOBAL.GTID_PURGED是否导出，5.6新增以兼容低版本
	
	--where="column>x"				    -----导出表的时候进行表记录的选择
	
	--ignore-table                      -----排除某张表
	
	
	
	
	
mysqldump -u root -p -h 127.0.0.1 -P 3306 w1 b --where="x>1"

--ingore-table=dbname.tb_name  导出时排出某张表，多张表时重复使用这个参数，精确匹配


第三方逻辑备份
备份
./mydumper -u root -p weideguo -h 127.0.0.1 -R -B test -o /u03/mydumper_dir
还原
./myloader -u root -p weideguo -h 127.0.0.1 -B wdg -d /u03/mydumper_dir

	-t 					--线程数

	

gtid(global transaction identifier)

gtid-mode={on|off}    				--设置是否启动gtid
--gtid_executed='gtid_string'  		--设置
--gtid_purged='gtid_string'			--设置清除之前的binlog





mysql -u root -p -h 127.0.0.1 -P 3306 my_database < my_database.sql

全量冷备份，复制整个data文件夹

selct ... from ... into outfile "file_name" [export_options];     --导出数据文件
--目录在【secure_file_priv】指定

----导入分割文件  
mysqlimport											
load data infile 'file_name' into table 'table_name' [export_options];     --账号需要有file权限 并且设置secure_file_priv正确 

load data local infile ...;               --导入不需要额外设置


---export_options
[{FIELDS | COLUMNS} [TERMINATED BY 'string']   --字段分割符
[[OPTIONALLY] ENCLOSED BY 'char']			   --字段包围符
[ESCAPED BY 'char']							   --换行符



xml
mysql --xml -e 'select ...' > filename;   ----导出xml
load xml infile 'file_name' into table 'table_name';


mysqlshow [options] [db_name [table_name [col_name]]]		---显示数据库、表、字段的信息
mysqlslap		---模拟对mysql服务器发出请求
nysqlcheck		---检查数据库、表、字段的存在、可访问情况，以及修复【repair】、分析【analyze】、优化【optimize】

myisamcheck     ---检查myisam表
	-o  ---修复myisam的表
	-r  ---更快速修复，如失败，使用-o
	
##更新表的统计信息
analyze table table_name;

##修复myisam的表
repair table table_name;    

MyISAM, ARCHIVE, and CSV tables.

#checks a table or tables for errors.
CHECK TABLE 
InnoDB, MyISAM, ARCHIVE, and CSV tables. 
For MyISAM tables, the key statistics are updated as well.

#消除碎片和链接
optimize table table_name; 

#recover myisam table
myisamchk -r table_name.myi



文件
错误文件
log_err/log-error

socket文件
Mysql有两种连接方式：
（1）TCP/IP
（2）socket    -----使用socket文件mysql.sock
对mysql.sock来说，其作用是程序与mysqlserver处于同一台机器，发起本地连接时可用

auto.cnf
数据文件的根目录下，设置server_uuid



mysql使用localhost登陆时是通过socket登陆？


日志
---可以输出到表或者文件
---启动参数【log-output】TABLE、FILE、NONE，可以多个以【，】隔开
---TABLE  对应general_log和slow_log两个表
---FILE   

LSN(Log Sequence Number)

查看lsn
show engine innodb status\G   ----在LOG的部分查看


缓存命中率Buffer pool hit rate

log_output='table'   ---'file' 'table,file'

----general query log and slow query log output

慢查询日志 (slow query log)  -----记录查询时间达到【min_examined_row_limit】、查询记录达到【long_query_time】的SQL语句
【slow_query_log】   		 ----是否开启慢查询日志
【show_query_log_file】      ----指定日志的路径及文件名

mysqldumpslow   ---解析分析慢查询日志

通用查询日志(general query log)   ---记录所有操作
【general_log】    		----指定是否开启通用查询日志
【general_log_file】    ----通用查询日志的路径及文件名

二进制日志
--用于复制
--用于恢复
【sync_binlog】设置二进制日志同步到磁盘的频率，默认二进制日志不是实时同步到磁盘
log_bin 	 		---my.cnf设置二进制文件路径并启用二进制日志【log_bin=path_name】，设置后即启用
binlog_format   	---my.cnf设置二进制日志的记录格式【基于语句记录(Statement-Based Logging,SBL)、基于行格式记录(Row-Bbased Logging,RBL)、混合模式记录(Mixed-Based Logging,MBL)】
expire_logs_days	---保存时间（天）

binlog-ignore-db=db1[,db2]    ---指定库不使用binlog
binlog-do-db=db1[,db2]		  ---指定库使用binlog

replicate-ignore-db			  ---从库中设置不复制的库
replicate-do-db1			  ---从库中设置复制的库

--强制写日志
flush logs;
flush binary logs;

--手动删除二进制日志
PURGE BINARY LOGS TO 'mysql-bin.010';
PURGE BINARY LOGS BEFORE '2008-04-02 22:46:26';

SHOW BINARY LOGS;   ---查看二进制日志
 
---修改二进制日志记录格式
SET GLOBAL binlog_format = 'STATEMENT';
SET GLOBAL binlog_format = 'ROW';
SET GLOBAL binlog_format = 'MIXED';

show variables like 'log_bin';   			----查看是否启用二进制日志
show binlog events in 'mysql-bin.000025';  	---查看二进制日志的事件
show binlog events;
show binlog events in 'log_name' from pos_number limit 2
show binary logs;		---查看二进制日志的信息

show relaylog events [in 'relay_log_name'] [from pos_number] [limit 2];  

mysqlbinlog  log_name    ----查看二进制日志的内容
	--start-datetime
	--stop-datetime
	--short-form

	--start-position
	--stop-position
	--base64-output=decode-rows        ##导出row格式   只能用于查看，恢复的时候不要加这个参数
	-v    				   ##导出成sql格式  与--base64-output一同使用
	
--从远端读取二进制日志并保存
mysqlbinlog -u root -p -P 3306 -h host_name -R -r save_as_text_file_name remote_binlog_name
	--stop-never   ----持续获取不中断
	
	
	

在执行操作前【set sql_log_bin=0(或者off)】可禁止执行的语句生成二进制日志


中继日志(relay log)    
----(io_thread)从节点I/O线程将主节点的二进制日志读取并记录到从节点本地文件形成中继日志
--- (sql_thread)然后从节点SQL线程会读取relay_log日志的内容并应用到从服务器
【relay_log】


复制特性(replication)

【MASTER】
	设置唯一的server_id的值；
	必须启用二进制日志（设置【log_bin】参数）。
	
show master status\G;	-----查看主节点的状态
show slave hosts;		-----差看slave节点
	
	
【SLAVE】
---设置唯一的server_id值；(slave节点可以自由确定是否启用二进制日志)
---配置slave到master的连接。
---应该设置中继日志
change master to
master_host='master_host',				-----
master_port=master_port,				-----
master_user='master_user',				-----主节点的账号，并拥有replication slave权限（grant replication slave on *.* to 'master_user'@'host' identified by 'user_password'; 创建用户并赋予权限）
master_password='master_user_password', -----
master_log_file='master_logfile',		-----在master中使用【show master status】查看
master_log_pos=master_position;			-----在master中使用【show master status】查看

show slave status\G;    ---查看从节点的状态

show slave hosts;		---在主节点查看从节点的信息

start slave sql_thread;  ---启动从节点sql线程
start slave io_thread;   ---启动从节点io线程

stop slave;   ---停止从节点的slave服务
start slave;  ---开启从节点的slave服务


出现告警 If a crash happens this configuration does not guarantee that the relay log info will be consistent, Error_code: 0
---在配置文件添加参数
在复制的slave节点会创建两个日志：master.info、relay-log.info。可以选择存放在文件(file)或者表(table)中。
slave启动时会读取master.info和relay-log.info确认从master读取relay log的情况。
io_thread线程维护master.info。
sql_thread线程维护relay-log.info。
或
set global master_info_repository='TABLE';
set global relay_log_info_repository='TABLE';



#从节点
Relay_Master_Log_File   SQL线程执行到的主节点的文件
Exec_Master_Log_Pos     SQL线程执行到的主节点的position


Master_Log_File         IO线程读取到的主节点的文件
Read_Master_Log_Pos     IO线程读取到的主节点的position


主从信息删除
1. reset master;						----删除所有二进制日志
2. purge master logs to 'log_name';     ----删除位于指定日志或日期之前的日志索引中的二进制日志。
3. purge master logs before 'date';     ----date格式：'YYYY-MM-DD hh:mm:ss'

reset slave all;	---从库删除主从信息


联级复制  
slave节点启动二进制日志，并设置【--log-slave-updates】参数，由中继日志产生的数据库修改也会写到本地二进制日志
slave节点作为下一层级slave节点的master

由slave节点进行备份
将slave节点的sql_thread关闭，在slave节点执行mysqldump

半同步机制 (semisynchronous replication)
一主多从架构中至少一个slave几点接收到事务(io_thread同步即可),即可返回成功的信息
----启用半同步，需要预先安装半同步插件
----master安装 semisync_master.so
----slave安装 semisync_slave.so
rpl_semi_sync_master_enabled=on    	---master的设置
rel_semi_sync_master_status=on		---master的设置
rpl_semi_sync_slave_status=on		---slave的设置


atomic commitment protocol,APC
两阶段提交 (two-phase commit,2PC)
msater提交事务后，等slave节点提交完毕


高可用架构


MMM(Multi-Master Replication Manager) 双主故障切换
mmm: http://mysql-mmm.org/
mha: https://code.google.com/p/mysql-master-ha/
heartbeat+brdb: http://lin128.blog.51cto.com/407924/279411 http://www.centos.bz/2012/03/achieve-drbd-high-availability-with-heartbeat/
cluster:http://database.51cto.com/art/201008/218326.htm
双master+keeplived: http://database.51cto.com/art/201012/237204.htm
双master: http://yunnick.iteye.com/blog/1845301



DRBD(Distributed Replicated Block Device)：分布式复制块设备
物理同步，由物理设备组成虚拟设备，可以由多个物理节点组成，数据存储于虚拟设备上。
drbd节点分master/secondary(主/从)角色


NDB   ---一种存储引擎，在mysql cluster中使用
管理节点(mgmd)，数据节点(ndbd)，服务节点(mysqld)；启动顺序是：mgmd -> ndbd -> mysqld

cluster集群
----需要使用mysql的cluster版本

管理节点(management node)
提供管理服务
ndb_mgmd -f $mysql_cluster_home/config.ini   ----启动管理节点   管理节点通过config.init配置data节点和sql节点

ndb_mgm    ----管理节点的命令行工具

data节点(data node)
保存集群中的数据
ndbd  --initial  ----第一次启动时添加【--initial】参数，再次启动不添加，启动时清空整个集群的数据

sql节点(sql node)
为客户端提供读取cluster数据
mysqld --defaults-file=$mysql_cluster_home/my.cnf    -----启动sql节点  或使用mysqld_safe


关闭
sql节点				 mysqladmin
管理节点、data节点	 ndb_mgm命令行中的shutdown命令	



MHA(master high availability) mysql master-slave的自动切换
需要额外的软件
MHA node		在所有mysql节点上安装
MHA manage		



mysql升级
1.使用mysqldump从旧版导出，然后再倒入新版
2.直接复制data目录，运行mysql_upgrade升级


内部数据库
mysql
performance_schema
information_schema			--全部是视图。


##表大小
select table_schema,table_name,concat(round(data_length/1024/1024,2),'MB') data_size from information_schema.tables;

表、索引大小
select sum(data_length + index_length) as src_used_space from information_schema.tables


库的大小
select concat(round(sum(data_length/1024/1024),2),'MB') data_size from information_schema.tables where table_schema='database_name';



##比较表的差异
checksum table table_name;






压测
mysqlslap -u root -p -c 100 -i 10 -e innodb --create-schema='test' --query='select * from ddd' --number-of-queries=100




审计audit
安装插件 server_audit.so
设置参数(可以动态设置)       ---所有参数 show variables like '%audit%'
server_audit_events="connect,query,table,query_ddl,query_dml,query_dcl"     ---设置审计的事件，可以选择一种或多种
server_audit_incl_users=root 												---设置审计包含的对象   或者使用【server_audit_excl_users】审计不包含的对象
server_audit_logging=on														---启动审计




profile            --显示当前会话执行的资源占用，使information_schema库代替

--信息存储于information_schema.profiling

set profiling=1    --启用profile
show profile [all|...];
show profiles;


索引
show index from table_name [from database_name] 

SELECT * FROM t1, t2 FORCE INDEX (index_for_column)
  WHERE t1.col_name=t2.col_name;  --强制使用指定索引


show open tables [from databases_name]   ---查看打开的表





event   --类似于oracle中的job,定时调度
--mysql.event
--information_schema.events

trigger   --触发器
--information_schema.trigger

#routine
function  ---函数
procedure ---存储过程
--information_schema.routines 
--mysql.proc

#查看创建语句
show create procedure `procedure_name`;    --不是definer时 需要select on mysql.proc权限
show create trigger `trigger_name`;
show create event `myevent`;


select * from mysql.proc        		 ---查看存储过程的信息
show procedure core procedure_name		 

show procedure status [like 'patten']    ---查看存储过程的状态



show events;
show triggers;

--调用
call procedure_name(p1,p1,...);
select function_name(p1,p1,...);

#执行权限
Execute  --To execute stored routines

#创建权限
Event    --To create, alter, drop and execute events
Trigger  --To use triggers      




ssl
Server-Side
[mysqld]
ssl-ca=ca.pem
ssl-cert=server-cert.pem
ssl-key=server-key.pem  

Client-Side
mysql --ssl-ca=ca.pem \
       --ssl-cert=client-cert.pem \
       --ssl-key=client-key.pem

5.7以及以下 如果不启动ssl，则连接后的传输以明文传输
8.0 默认都以ssl加密传输
 
 
create user ... require ssl;

延时复制
slave节点中
change master to master_delay=n;   ----n为延时的秒


多源复制 mulit source replication
一个从库可以有多个主库
change master to master_host='127.0.0.1'
,master_port=3306
,master_user='root'
,master_password=''
,master_auto_position=1     --也可以使用传统的指定binlog文件名及position确定复制点
for channel 'master_2';




	
	
复制跳过
--slave_skip_errors	
--sql_slave_skip_counter	  ----跳过事件数
	
	
	
排序
指定主键时，不加order by语句则按照主键排序
不指定主键，但unqiue键在为第一个字段，按unique键排序。
不指定主键，按照插入顺序排序。	
	
	

	
	
count(*)/count(1)  --没有where子句时，使用最小的索引进行查询；带有where子句，使用能优化where的索引。	
count(*)           --所有行都计算
count(colume)      --字段的值为空时不计算



分区表
SELECT * FROM p1 PARTITION (p0[,p1])；     							#从指定分区查询
EXPLAIN PARTITIONS SELECT * FROM p1 WHERE column_name=10；			#查看从分区表的执行信息
ALTER TABLE tr DROP PARTITION p2;	                              	#删除分区，针对RANGE/LIST分区
ALTER TABLE tr ADD PARTITION (PARTITION p_name …);   				#增加分区，针对RANGE/LIST分区
ALTER TABLE members REORGANIZE PARTITION p0,p1,p2,p3 INTO (
    	PARTITION m0 …,
   	PARTITION m1 …);       						#调整RANGE/LIST分区
ALTER TABLE tr COALESCE PARTITION 4;   			#减小HASH/KEY分区
ALTER TABLE tr ADD PARTITION PARTITIONS 6;      #增多HASH/KEY分区


--信息查看
information_schema.partitions;	
information_schema.tables;	
	
select replace(convert(v using ascii),'?','')  from qwe;   	--使用不兼容的字符转换实现去掉字段中的中文

myisam没有行级锁？



在线DDL	


5.5或5.1在使用innodb plugin
fast index creation
sql语句无需更改	
	
	
online ddl 5.6之后的特性？？
innodb_online_alter_log_max_size 
Specifies an upper limit on the size of the temporary log files used during online DDL operations for InnoDB tables. This log file stores data inserted, updated, or deleted in the table during the DDL operation.

LOCK = DEFAULT
Maximum level of concurrency for the given ALGORITHM clause (if any) and ALTER TABLE operation: Permit concurrent reads and writes if supported. If not, permit concurrent reads if supported. If not, enforce exclusive access.

LOCK = NONE
If supported, permit concurrent reads and writes. Otherwise, return an error message.

LOCK = SHARED
If supported, permit concurrent reads but block writes. Note that writes will be blocked even if concurrent writes are supported by the storage engine for the given ALGORITHM clause (if any) and ALTER TABLE operation. If concurrent reads are not supported, return an error message.

LOCK = EXCLUSIVE
Enforce exclusive access. This will be done even if concurrent reads/writes are supported by the storage engine for the given ALGORITHM clause (if any) and ALTER TABLE operation.


ALTER TABLE ...,ALGORITHM=INPLACE 
ALTER TABLE ...,ALGORITHM=COPY


alter table t1 add b int ,ALGORITHM=INPLACE,lock=none;	
#同一张表同时执行alter语句，后面的语句会被阻塞，因为要等metadata lock

alter table add key(c) ,ALGORITHM=copy,lock=exclusive;	
#lock只能选择shared(默认)、exclusive


ALTER TABLE tbl_name FORCE	
	
	

myisam_sort_buffer_size   #加快myisam的插入速度



##存在数据字符编码转换
gbk -> utf8

1.以utf8字符编码导出
mysqldump --default-character-set=utf8

2.修改导出格式中的创建表的语句，字符编码修改为utf8

3.导入


###编码

mysql存储的字符编码
create table(...) default charset=utf8;

mysql用于转换客户端二进制到存储二进制的编码
set names utf8;

终端编码
终端将字符串转换成二进制的编码 




#在线DDL工具

都需要有主键或唯一键
任何表都可以

#percona

percona-toolkit(perl)
#online ddl
bin/pt-online-schema-change --alter="add key(c1,c2)" --execute u=root,p=,h=127.0.0.1,P=3306,D=test,t=aa2


#github(go)

gh-ost -execute --allow-on-master -conf /data/hadoop/mysql5530/etc/my.cnf -alter "add x int" -database test -table a -user root -password 

#在主库执行，从库会复制


#facebook 
OnlineSchemaChange(python)


./osc_cli copy --allow-drop-column --mysql-user root --mysql-password "" --socket /data/hadoop/mysql5530/data/mysql5530.sock --database test --ddl-file-list new_create.sql 

#sql文件为新的表的建表语句
#只能在本地修改
#表要有主键





tungsten-replicator
##
支持多种数据库的复制工具
mysql复制到其他数据源

			       
设置多线程复制
set global slave_parallel_workers=30



元数据锁


#第三方存储引擎

##spider存储引擎
本身只存路由信息，转发访问后端数据

DDL语句不传输到后端？

mysqldump只导出spider的建表语句


##tokuDB



 
