# MySQL操作审计方案


## 1.设置变量init_connect记录每次登陆+binlog+slowlog联合审计
有super权限账号的不会被init_connect记录，没有退出信息。对现有架构影响较小。
```sql
-- 在配置文件设置  
-- in-it_connect="INSERT INTO accesslog.accesslog(`id`,`user`,`login_date`) VALUES (connection_id(),user(),now());"  
SET GLOBAL init_connect="INSERT INTO accesslog.accesslog(`id`,`user`,`login_date`) VALUES (connection_id(),user(),now());"  
  
CREATE DATABASE accesslog;  
CREATE TABLE `accesslog`.`accesslog`   
(`id` int(11),  
`user` char(100) ,  
`login_date` datetime,  
`logout_date` datetime DEFAULT '2000-01-01 00:00:00',  
key (`id`)  
);  

```


## 2.开启通用日志
文件会比较大，可能需要定时外部切换日志以及定期删除，可能会有性能影响。没有粒度过滤，所有的语句都会被记录。没有对应用户操作的信息。
```sql
SET GLOBAL general_log=ON;
```


## 3.安装开源审计插件
MariaDB 的审计server_audit.so，MariaDB原生支持，MySQL>=5.5（使用MariaDB10.3.9的插件测试）。至少需要升级到MySQL5.5，有一定风险，有可能需要研发修改服务中数据库相关的代码，以及可能存在未知的错误需要反复测试。
```shell
# 升级数据库 
# 需要逐级升级 即 5.1 -> 5.5 -> 5.6 -> 5.7
# 以 5.1 升 5.5 为例
# 1. 停止5.1的实例，移动相关数据文件（data目录、binlog目录）到备份目录
# 2. 使用相同my.cnf安装5.5实例（可能有些不兼容参数需要修改，主要目的是保持与原来的文件结构一致） ，安装完毕删除相关数据文件。
# 3. 复制原来5.1的相关数据文件到原来的位置。启动5.5实例。
# 4. 5.5实例运行升级
./mysql_upgrade -u root -p -h 127.0.0.1 -P 3306

```
```sql
-- mysql安装审计插件
-- 查看插件目录的位置
SHOW VARIABLES like '%plugin_dir%';
-- 上传从MariaDB服务获取的server_audit.so文件到插件目录 
-- 安装插件
INSTALL PLUGIN server_audit SONAME 'server_audit.so';
-- 查看相关配置参数
SHOW GLOBAL VARIABLES LIKE '%server_audit%';  
-- 至少需要启用该参数
SET GLOBAL server_audit_logging=ON
```
```shell
-- 审计日志输出样例
20201130 23:07:48,localhost.localdomain,root,localhost,1,2,QUERY,,'set global server_audit_logging=on',0
20201130 23:07:51,localhost.localdomain,root,localhost,1,2,QUERY,,'show databases',0
20201130 23:08:33,localhost.localdomain,root,localhost,1,2,QUERY,,'show databases',0
20201130 23:08:34,localhost.localdomain,,,1,0,DISCONNECT,,,0
20201130 23:08:44,localhost.localdomain,root,localhost,2,0,FAILED_CONNECT,,,1045
20201130 23:08:45,localhost.localdomain,,,2,0,DISCONNECT,,,0
20201130 23:08:46,localhost.localdomain,root,localhost,3,0,CONNECT,,,0
20201130 23:08:46,localhost.localdomain,,,3,0,DISCONNECT,,,0
```
```
#日志格式
timestamp       Time at which the event occurred. If syslog is used, the format is defined by syslogd.
syslog_host     Host from which the syslog entry was received.
syslog_ident    For identifying a system log entry, including the MariaDB server.
syslog_info     For providing information for identifying a system log entry.
serverhost      The MariaDB server host name.
username        Connected user.
host            Host from which the user connected.
connectionid    Connection ID number for the related operation.
queryid         Query ID number, which can be used for finding the relational table events and related queries. For TABLE events, multiple lines will be added.
operation       Recorded action type: CONNECT, QUERY, READ, WRITE, CREATE, ALTER, RENAME, DROP.
database        Active database (as set by USE).
object          Executed query for QUERY events, or the table name in the case of TABLE events.
retcode         Return code of the logged operation.
```
参考文档 https://mariadb.com/kb/en/mariadb-audit-plugin/


## 4.抓包解析
通过抓取mysql服务所在的网卡流量，由mysql协议解析传输的信息。  
参考工具(mysql-sniffer)[https://github.com/Qihoo360/mysql-sniffer]


## 5.开发连接中间件
所有连接都通过中间件，对现有架构破坏太大，不具可行性。


## 6.企业版（自带审计插件）
需要付费，且版本要升级。

