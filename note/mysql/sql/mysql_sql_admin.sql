-- 一些管理用的sql

----空间占用查询
----所有数据的大小：
select concat(round(sum(data_length/1024/1024),2),'MB') as data from information_schema.tables;
----指定数据库的大小：
select concat(round(sum(data_length/1024/1024),2),'MB') as data from information_schema.tables where table_schema='schema_name';
----指定数据库各表的大小：
select TABLE_SCHEMA,TABLE_NAME,concat(round(sum(data_length/1024/1024/1024),2),'G') as data from information_schema.tables where TABLE_SCHEMA='schema_name' group by TABLE_NAME;


-- 查看正在运行的事务以及运行时间
select t.*,to_seconds(now())-to_seconds(t.trx_started) idle_time from INFORMATION_SCHEMA.INNODB_TRX t;


-- 查询事务详细信息及当前执行的SQL
select now(),(UNIX_TIMESTAMP(now()) - UNIX_TIMESTAMP(a.trx_started)) diff_sec,b.id process_id,b.user,b.host,b.db,d.SQL_TEXT 
from 
information_schema.innodb_trx a 
inner join information_schema.PROCESSLIST b on a.TRX_MYSQL_THREAD_ID=b.id 
inner join performance_schema.threads c ON b.id = c.PROCESSLIST_ID
inner join performance_schema.events_statements_current d ON d.THREAD_ID = c.THREAD_ID
where b.command = 'Sleep' ;   -- 可以只看当前休眠的会话


-- 查询事务执行过的历史sql以及事务的运行时长
select ps.id process_id,ps.user,ps.host,ps.db,esh.event_id,trx.trx_started,esh.event_name, esh.sql_text,ps.time 
from 
performance_schema.events_statements_history esh 
join performance_schema.threads th on esh.thread_id = th.thread_id 
join information_schema.processlist ps on ps.id = th.processlist_id 
left join information_schema.innodb_trx trx on trx.trx_mysql_thread_id = ps.id 
where trx.trx_id is not null and ps.user !='SYSTEM_USER' order by esh.event_id ;


-- 查询事务锁详细信息
SELECT
  tmp.*,
  c.SQL_Text blocking_sql_text,
  p.HOST blocking_host
FROM
  (
  SELECT
    r.trx_state wating_trx_state,
    r.trx_id waiting_trx_id,
    r.trx_mysql_thread_Id waiting_thread,
    r.trx_query waiting_query,
    b.trx_state blocking_trx_state,
    b.trx_id blocking_trx_id,
    b.trx_mysql_thread_id blocking_thread,
    b.trx_query blocking_query
  FROM
    information_schema.innodb_lock_waits w
    INNER JOIN information_schema.innodb_trx b ON b.trx_id = w.blocking_trx_id
    INNER JOIN information_schema.innodb_trx r ON r.trx_id = w.requesting_trx_id 
  ) tmp,
  information_schema.PROCESSLIST p,
  PERFORMANCE_SCHEMA.events_statements_current c,
  PERFORMANCE_SCHEMA.threads t
WHERE
  tmp.blocking_thread = p.id 
  AND t.thread_id = c.THREAD_ID 
  AND t.PROCESSLIST_ID = p.id;


-- 查看元数据锁  
select s.PROCESSLIST_ID,s.PROCESSLIST_INFO,s.PROCESSLIST_STATE 
from performance_schema.threads s 
join performance_schema.metadata_locks m 
on m.OWNER_THREAD_ID=s.THREAD_ID where s.PROCESSLIST_STATE like '%waiting%'



-- tps qps
--在不同的时间段查询两次取差值
show status like 'queries'
QPS=(Q1-Q2)/time

questions也可以做一定的衡量，不包含存储过程执行的语句

--需要显式提交/回滚
show status like 'Com_commit'
show status like 'Com_rollback'
TPS=(CC1+CR1-CC2-CR2)/time

--可以用从库的来判断主库的TPS，因为复制时都带有事务标识（但从库不复制rollback信息）

show global status like 'Com_%'



-- 慢查询数量
show status like 'Slow_queries'


SHOW ENGINE PERFORMANCE_SCHEMA STATUS;   -- 查看PERFORMANCE_SCHEMA库的内存使用情况


#自动统计参数
innodb_stats_*
myisam_stats_*                      


innodb_stats_auto_recalc
开启自动计算统计信息，当表10%的记录发生变化重新计算

innodb_stats_persistent
持久化存储表的统计信息，持久化信息存储于 mysql.innodb_table_stats、mysql.innodb_index_stats


innodb_stats_on_metadata 
不设置持久化存储表的统计信息时，当这个为ON则：
When innodb_stats_on_metadata is enabled, InnoDB updates non-persistent statistics when metadata statements such as 
SHOW TABLE STATUS or SHOW INDEX are run, or when accessing the INFORMATION_SCHEMA.TABLES or INFORMATION_SCHEMA.STATISTICS tables. 
(These updates are similar to what happens for ANALYZE TABLE.) 


#单独设置表的统计信息的收集计划
ALTER TABLE tbl_name STATS_PERSISTENT=0, STATS_SAMPLE_PAGES=20, STATS_AUTO_RECALC=1, ALGORITHM=INPLACE, LOCK=NONE; 
                      


##更新表的统计信息 During the analysis, the table is locked with a read lock for InnoDB and MyISAM.
# 执行期间 read lock, 最后需要flush lock
analyze table table_name;

##修复myisam的表
repair table table_name;    

MyISAM, ARCHIVE, and CSV tables.

#checks a table or tables for errors.
CHECK TABLE 
InnoDB, MyISAM, ARCHIVE, and CSV tables. 
For MyISAM tables, the key statistics are updated as well.

#消除碎片和链接 online DDL
optimize table table_name; 

#innodb 使用以下语句代替 optimize
alter table table_name engine=innodb;


delete语句不会回收磁盘空间，因而会出现大量碎片。使用truncate相当语句drop+create，因此磁盘空间得到释放。


##比较表的差异
checksum table table_name;
