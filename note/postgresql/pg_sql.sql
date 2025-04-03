字段类型

BIT                     固定长度的位串。   
BIT VARYING(n)         
VARBIT(n)               可变长度的位串，长度为 n 位。   
BYTEA                   用于存储大型二进制对象（比如图形）的原始二进制数据。使用的存储空间是 4 字节加上二进制串的长度。   

BOOLEAN                 存储逻辑布尔值（true/false/unknown），可以是 TRUE、t、true、y、yes 和 1，或者 FALSE、f、false、n、no 和 0。   

CHAR(n)        
CHARACTER(n)            包含固定长度的字符串，用空格填充到长度 n。       
CHARACTER VARYING(n)
CHARACTER VARYING       
VARCHAR(n)              存储可变长度的字符串，最大长度为 n。不存储末尾的空格。
TEXT                    存储长度可变的大型字符串数据，最多 1 GB。PostgreSQL 自动压缩 TEXT 字符串。

DECIMAL(p,s)        
NUMERIC(p,s)            存储精确的数值，精度（p）和刻度（s）为 0 或更高。
FLOAT4      
REAL                    存储浮点数，精度为 8 或更低和 6 个小数位。
FLOAT8      
DOUBLE PRECISION        存储浮点数，精度为 16 或更低和 15 个小数位。
SMALLINT                存储有符号或无符号 2 字节整数。
INTEGER                 存储有符号或无符号 4 字节整数。
INT8        
BIGINT                  存储有符号或无符号 8 字节整数。
SERIAL      
SERIAL4                 存储自动递增的惟一整数值，最多 4 字节存储空间。
BIGSERIAL
SERIAL8                 存储自动递增的惟一整数，最多 8 字节。   

DATE                                            用 4 字节的存储空间存储日历日期（年、月、日）。       
DATETIME                                        存储日历日期和天内的时间。
TIME (WITHOUT TIME ZONE | WITH TIME ZONE)       存储天内的时间。如果不存储数据库服务器的时区，就使用 8 字节的存储空间；如果存储时区，就使用 12 字节。
TIMESTAMP (WITHOUT TIME ZONE | WITH TIME ZONE)  存储日期和时间。可以存储或不存储数据库服务器的时区，使用 8 字节存储空间。


用户定义的数据类型：
CREATE DOMAIN   创建了一个用户定义的数据类型，可以有可选的约束。
CREATE TYPE     用于使用存储过程创建复合类型(两种或多种数据类型混合的数据类型)



-- 使用虚表时设置类型
select '10.0.0.1/32'::inet;


-- 修改字段的类型
ALTER TABLE really_long_long_table_test ALTER COLUMN  id  TYPE  char(18);


-- 事务
begin;
...
commit; -- rollback;


alter table tb_old rename to tb_new;

create table (tb_new like tb_old);

explain select ...



-- sequence

create sequence sq_name increment 2 minvalue 1 no maxvalue  start with 1 cache 2 ;
alter sequence  sq_name increment 1 minvalue 1 maxvalue 999999999999 start with 100 cache 2 ;

-- 查看sequence
select * from information_schema.sequences; 


create table table_name (
id serial,                 -- 自动创建sequence
name text);


create table table_name (
id int4 not null default nextval('sequence_name'),
name text);




SELECT proname FROM pg_proc;      -- 存储过程查看


CREATE OR REPLACE PROCEDURE update_salary(emp_id INT, increase_amount DECIMAL)
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE employees 
    SET salary = salary + increase_amount 
    WHERE id = emp_id;
    
    COMMIT;
END;
$$;

CALL update_salary(123, 5000);

