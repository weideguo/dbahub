delimiter  设置结束符号

event   --类似于oracle中的job,定时调度
--mysql.event
--information_schema.events


trigger   --触发器
--information_schema.trigger

routine
function  ---函数
procedure ---存储过程
--information_schema.routines 
--mysql.proc

#查看创建语句
show create procedure `procedure_name`;    --不是definer时 需要select on mysql.proc权限
show create trigger `trigger_name`;
show create event `myevent`;


select * from mysql.proc                 ---查看存储过程的信息
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




delimiter //
create trigger db_info_to_stats
BEFORE delete on db_info
for each row
begin
delete from stats where ip=old.master_private_ip;
end;
//


drop trigger db_info_update_stats;
delimiter //
create trigger db_info_update_stats
after update on db_info
for each row
begin
declare private_ip varchar(40);
declare my_cursor cursor for select manage_private_ip from cloud_info where cloud_id=new.cloud_id;
open my_cursor;
fetch my_cursor into private_ip;
close my_cursor;

replace into stats(
db_type
,project
,channel
,manage_host
,ip
,port
,max_connections
,comment)   
values(
new.db_type           
,new.project           
,new.sub_project       
,private_ip 
,new.master_private_ip 
,new.master_port                
,new.max_connections    
,new.hardware_info   
);
end;
//
delimiter ;


drop trigger db_info_insert_stats;
delimiter //
create trigger db_info_insert_stats
after insert on db_info
for each row
begin
declare private_ip varchar(40);
declare my_cursor cursor for select manage_private_ip from cloud_info where cloud_id=new.cloud_id;
open my_cursor;
fetch my_cursor into private_ip;
close my_cursor;

replace into stats(
db_type
,project
,channel
,manage_host
,ip
,port
,max_connections
,comment)   
values(
new.db_type           
,new.project           
,new.sub_project       
,private_ip 
,new.master_private_ip 
,new.master_port                
,new.max_connections    
,new.hardware_info   
);
end;
//
delimiter ;





set global event_scheduler=on; 

CREATE EVENT myevent
ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL 1 HOUR
DO
UPDATE mytable SET mycol = mycol + 1;


delimiter ;;
CREATE EVENT `myevent_test` 
ON SCHEDULE EVERY 1 minute 
ON COMPLETION PRESERVE ENABLE 
DO 
BEGIN
insert into test20201124(opt_date) values(now());
END
;;
delimiter ;

select db,name,status from mysql.event;
--修改状态
-- update mysql.event set status='DISABLED' where name='myevent_test';   
-- update mysql.event set status='ENABLED' where name='myevent_test';   flush tables mysql.events;  --不能立即生效 需要重启？
alter event myevent_test disable;
alter event myevent_test enable;



delimiter ;;                                                 -- 
CREATE EVENT `myevent_test`                                  -- 
ON SCHEDULE EVERY 1 DAY                                      --
starts '2011-03-21 03:30:00'                                 -- 开始时间 
ON COMPLETION PRESERVE ENABLE                                -- 
DO                                                           -- 
...                                                          -- 
;;                                                           -- 
delimiter ;                                                  -- 




CREATE FUNCTION f1(s CHAR(20))
RETURNS CHAR(50) DETERMINISTIC
RETURN CONCAT('Hello, ',s,'!');


create function func_name(arg1 int,arg2 varchar(10)...)
returns varchar(10)
begin
...
end

调用
select func_name(...) from ...



delimiter //
create procedure random_insert_max()
begin
declare i int;
set i=0;
while i<8000000 do
insert into index_test1(a,b,c,d,e) values(round(rand()*10000),round(rand()*10000),round(rand()*1000),round(rand()*10000),round(rand()*10000));
set i=i+1;
end while;
end

//
delimiter ;

--插入多行
CREATE TABLE t (
a INT UNSIGNED NOT NULL AUTO_INCREMENT,
b CHAR(10),
PRIMARY KEY(a)
) ENGINE=INNODB CHARSET=LATIN1 ROW_FORMAT=COMPACT;


DELIMITER //
CREATE PROCEDURE load_t (count INT UNSIGNED)
BEGIN
SET @c=0;
WHILE @c < count DO
INSERT INTO t SELECT NULL,REPEAT(CHAR(97+RAND()*26),10);
SET @c=@c+1;
END WHILE;
END;
//
DELIMITER ;


select * from mysql.proc        ---查看存储过程的信息
DROP PROCEDURE procedure_name   ---删除存储过程




DELIMITER //  
CREATE PROCEDURE demo_in_parameter(IN p_in int)  
BEGIN   
SELECT p_in;   
SET p_in=2;   
SELECT p_in;   
END;   
//  
DELIMITER ;

DELIMITER //   
CREATE PROCEDURE proc1(OUT s int)  
BEGIN 
SELECT COUNT(*) INTO s FROM wdg_test;  
END 
//  
DELIMITER ;    


DELIMITER //   
CREATE PROCEDURE demo_inout_parameter(INOUT p_inout int)   
BEGIN 
SELECT p_inout;  
SET p_inout=2;  
SELECT p_inout;   
END;  
//   
DELIMITER ; 
 
执行存储过程
---执行结果:
SET @p_inout=1;  
CALL demo_inout_parameter(@p_inout) 


DELIMITER //  
CREATE PROCEDURE proc3()  
begin 
declare x1 varchar(5) default 'outer';     ----声明变量
begin 
declare x1 varchar(5) default 'inner';  
select x1;  
end;  
select x1;  
end;  
//  
DELIMITER ;

create procedure my_insert(in bg int,in en int)
begin
declare i int;
set i=1;
lp1: loop
insert into test.demo values(i);
set i=i+1;
if i>x then
leave lp1;
end if;
end loop;
end;
DELIMITER ;

DELIMITER // 
create procedure my_insert(in begin_num int,in end_num int)
begin
declare i int;
set i=begin_num;
while i<end_num
do
insert into test.demo values(i);
set i=i+1;
end while;
end;
DELIMITER ;

DELIMITER //
create procedure input_t(in table_n varchar(20))
begin
select table_n;
end;
DELIMITER ;


