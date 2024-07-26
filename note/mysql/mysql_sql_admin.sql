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
