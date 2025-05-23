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


-- 索引加载到内存统计
SELECT 
  its.database_name as db_name,
  its.table_name as table_name,
  its.index_name as index_name,
  ibp.PAGE_TYPE,
  COALESCE(ibp.records, 0) as pool_rows,
  its.n_rows as total_rows,
  COALESCE(ibp.records, 0)/its.n_rows AS pct_cached,
  COALESCE(ibp.n_pages, 0)/its.n_leaf_pages AS page_pct_cached
FROM 
  (
    SELECT DISTINCT
      database_name,
      table_name,
      index_name,
      CONCAT('`', database_name, '`.`', table_name, '`') AS full_table_name, 
      n_leaf_pages,
      n_rows
    FROM 
      mysql.innodb_table_stats
    join (
        select database_name,table_name,index_name,
        max(stat_value) as n_leaf_pages 
        from mysql.innodb_index_stats 
        where stat_name='n_leaf_pages'
        group by database_name,table_name,index_name
    ) t_pages
    using (database_name, table_name)
    WHERE 
      database_name = 'my_test_db'                -- 库名
  ) its
LEFT JOIN 
  (
    SELECT 
      TABLE_NAME,
      INDEX_NAME,
      PAGE_TYPE, 
      SUM(NUMBER_RECORDS) AS records,
      COUNT(PAGE_NUMBER) AS n_pages
    FROM 
      INFORMATION_SCHEMA.INNODB_BUFFER_PAGE
    WHERE 
      TABLE_NAME LIKE '%`my_test_db`%'            -- 库名
    GROUP BY 
      TABLE_NAME, INDEX_NAME, PAGE_TYPE
  ) ibp 
ON 
  its.full_table_name = ibp.TABLE_NAME and its.index_name = ibp.INDEX_NAME
ORDER BY table_name, index_name;
 
 
-- 操作系统线程id与mysql连接id
SELECT 
    p.ID AS mysql_connection_id,        -- mysqll连接id
    p.USER,
    p.HOST,
    p.DB,
    p.COMMAND,
    p.TIME,
    p.STATE,
    p.INFO,
    t.THREAD_OS_ID
FROM 
    performance_schema.threads t
LEFT JOIN 
    information_schema.processlist p 
    ON t.PROCESSLIST_ID = p.ID
WHERE 
    t.THREAD_OS_ID = 48349;              -- 操作系统的线程id

