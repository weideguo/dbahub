-- 一些管理用的sql

----空间占用查询
----所有数据的大小：
select concat(round(sum(data_length/1024/1024),2),'MB') as data from information_schema.tables;
----指定数据库的大小：
select concat(round(sum(data_length/1024/1024),2),'MB') as data from information_schema.tables where table_schema='schema_name';
----指定数据库各表的大小：
select TABLE_SCHEMA,TABLE_NAME,concat(round(sum(data_length/1024/1024/1024),2),'G') as data from information_schema.tables where TABLE_SCHEMA='schema_name' group by TABLE_NAME;

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
When innodb_stats_on_metadata is enabled, InnoDB updates non-persistent statistics when metadata statements such as 
SHOW TABLE STATUS or SHOW INDEX are run, or when accessing the INFORMATION_SCHEMA.TABLES or INFORMATION_SCHEMA.STATISTICS tables. 
(These updates are similar to what happens for ANALYZE TABLE.) 

表的统计信息查询
select * from mysql.innodb_table_stats;

#设置表的统计信息的收集计划
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
