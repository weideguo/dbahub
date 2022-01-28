SQL语句执行顺序
from
where
start with     ---start with {expression} connect by {expression}实现递归查询，prior表示父节点跟子节点的联系
connect by
group by
having
model   ---oracle特有，允许像访问数组的元素访问记录中的某个项
select
union、minus、intersect
order by


--复合类型：记录型（相当于结构体）、集合型（相当于数组）
--索引表（Index-By Table），嵌套表（Nested Table），可变数组（Varray）
type t_emp is record (empno empno%type,ename ename%type);  	--记录型
type emp_table is table of t_emp index by binary_integer;	--集合型/索引表
type varray_name is varray(5) of char(10);   --可变数组,创建有5个成员的数组,类型为char(10),不能删除数组中间的元素

--批绑定，PL/SQL引擎与SQL引擎之间传送SQL语句的过程为上下文切换，批绑定一次性的从PL/SQL引擎中
--传递给SQL引擎
--FORALL语句
forall i in a.first..a.last loop

end loop;
--BULK COLLECT
select * bulk collect into v_x from xyz;
fetch v_x bulk into collect x_x;
 
 
alter {procedure|function|trigger} pft_name compile;  ---编译触发器、存储过程、函数
 
 
set serveroutput on  ---设置在sql plus环境中看到DBMS_OUTPUT.PUT_LINE方法的输出结果

[PL/SQL]
create or replace procedure showavesal(p_deptno number)
as					---is或as都可以
v_sal number(6,2);
begin
select avg(sal) into v_sal from emp where deptno=p_deptno;
DBMS_OUTPUT.PUT_LINE(v_sal);
end showavesal;
 
declare
	i number(4);
begin
	for i in 1 .. 500 loop
		insert into wdg_test values('wei',i);
	end loop;
	commit;
end;
 
---匿名存储过程
declare
v_sal emp.ename%type;
begin
select ename into v_sal from emp where deptno=7844;
DBMS_OUTPUT.PUT_LINE(v_sal);
end;
 
create or replace procedure v_showname
as
	v_name emp.ename%type;  
begin    
	select ename into v_name from emp where empno=7844;
	DBMS_OUTPUT.PUT_LINE(v_name);
end v_showname;
 
create or replace procedure area(v_number number)
as
num number ;
begin
select v_number into num from dual;
DBMS_OUTPUT.PUT_LINE(v_number);
end area;

create or replace procedure showall(p_ename char)
as 
v_emp emp%rowtype;
begin
select * into v_emp from emp where ename=p_ename;
DBMS_OUTPUT.PUT_LINE(v_emp.ename || v_emp.sal);
end showall;
 
declare
	cursor c_emp is select empno,ename from emp where deptno=10;  --游标
	v_emp10 c_emp%rowtype;
begin
	open c_emp;
	loop
		fetch c_emp into v_emp10;
		exit when c_emp%NOTFOUND;
		DBMS_OUTPUT.PUT_LINE(v_emp10.empno||' '||v_emp10.ename);
	end loop;
	close c_emp;
end;

--使用游标变量
declare
	type emp_cursor is ref cursor return emp%rowtype;
	v_emp emp_cursor;
	c_emp emp%rowtype;
begin
	open v_emp for select * from emp;
	loop
		fetch v_emp into c_emp;
		exit when v_emp%NOTFOUND;
		DBMS_OUTPUT.PUT_LINE(c_emp.ename||' '||c_emp.empno);
	end loop;
	close v_emp;
end;	


	
declare
	x_emp emp%rowtype;
	cursor v_emp is select * from emp;
begin
	DBMS_OUTPUT.PUT_LINE('empno ename');
	open v_emp;
	loop
		fetch v_emp into x_emp;
		exit when v_emp%NOTFOUND;
		DBMS_OUTPUT.PUT_LINE(x_emp.empno||' '||x_emp.ename);
	end loop;
	close v_emp;
end;


--使用out返回参数
--in 输入
--in out 输入同时可以返回
create or replace procedure ptest(
p_ename  emp.ename%type,
p_deptno out emp.deptno%type
)
is
begin
select deptno into p_deptno from emp where ename=p_ename;
--exception
--when NO_DATA_FOUND THEN
	--DBMS_OUTPUT.PUT_LINE('name not found!');
end ptest;

--调用out参数
declare
o_deptno emp.deptno%type;
begin
ptest('KING',o_deptno);
dbms_output.put_line(o_deptno);
end;

declare
v_deptno emp.deptno%type;
begin
ptest('SCOTT',v_deptno);
DBMS_OUTPUT.PUT_LINE(v_deptno);
end;

--创建函数
create or replace function return_maxsal
(f_deptno emp.deptno%type)
return emp.sal%type
is
	v_maxsal emp.sal%type;
begin
	select max(sal) into v_maxsal from emp where deptno=f_deptno;
	return v_maxsal;
end return_maxsal;

--调用函数，使用select或者在pl/sql中调用
select return_maxsal from dual;

create procedure dept_maxsal(p_deptno emp.deptno%type)
is
x_sal emp.sal%type;
begin
x_sal :=return_maxsal(p_deptno);
DBMS_OUTPUT.PUT_LINE(x_sal);
end;

--查看用户的所有函数、实行过程及源代码,查询数据字典视图user_source
--user_procedures,user_triggers也是数据字典
select * from user_source;
--删除函数
drop function xyz;
--函数重编译
alter function xyz compile;

--创建包规范
create or replace package p_test
is
minsal number;
maxsal number;
procedure get_minsal(p_deptno number);
procedure get_maxsal(p_deptno number);
end p_test;

--创建包体
create package body p_test
is
	procedure get_maxsal(p_deptno number)
	is
	begin
		select max(sal) into maxsal from emp where deptno=p_deptno;
		DBMS_OUTPUT.PUT_LINE(maxsal);
	end get_maxsal;
	
	procedure get_minsal(p_deptno number)
	is
	begin
		select min(sal) into minsal from emp where deptno=p_deptno;
		DBMS_OUTPUT.PUT_LINE(minsal);
	end get_minsal;
end p_test;

--包的调用
execute p_test.get_maxsal(10);

--创建程序包体
create or replace package pf_test
is
	maxsal number;
	function fget_maxsal(p_deptno number) return number;
end pf_test;

create package body pf_test
is
	function fget_maxsal(p_deptno number) 
	return number 
	is
	begin
		select max(sal) into maxsal from emp where deptno=p_deptno;
		return maxsal;
	end fget_maxsal;
end pf_test;

select pf_test.fget_maxsal(10) from dual;

--触发器,建立在表上的为DML触发器，建立在视图上的为instead of触发器
create or replace trigger trg_emp_dml
after insert or update or delete on emp
declare
v_count number;
v_sal number;
begin
	if inserting then
		select count(*) into v_count from emp;
		DBMS_OUTPUT.PUT_LINE(v_count);
	elsif updating then
		select avg(sal) into v_sal from emp;
		DBMS_OUTPUT.PUT_LINE(v_sal);
	else
		DBMS_OUTPUT.PUT_LINE('delete');
	end if;
end trg_emp_dml;

--列级触发器
create or replace trigger trg_emp_row
before insert or update or delete on emp
for each row
begin
	if inserting then
		DBMS_OUTPUT.PUT_LINE(:new.empno||' '||:new.ename);
	elsif updating then
		DBMS_OUTPUT.PUT_LINE(:old.sal||' '||:new.sal);
	else
		DBMS_OUTPUT.PUT_LINE(:old.empno||' '||:old.ename);
	end if;
end trg_emp_row;

--instead of触发器
/*
视图有下列情况不可以修改：
集合操作符号（union/union all/minus/intersect）
聚合函数
GROUP BY、CONNECT BY、START WITH等
DISTINCT操作符
多个表的连接
*/ 
--使用instead of触发器可以实现修改原本不可以修改的视图
--创建视图，使用insert会报错
create or replace view empdept
as
select empno,ename,sal,dname from emp,dept where emp.deptno=dept.deptno with check option;

create or replace trigger trig_view 
instead of insert on empdept
for each row 
declare
	v_deptno emp.deptno%type;
begin
	select deptno into v_deptno from dept where dname=:new.dname;
	insert into emp(empno,ename,sal,deptno) values(:new.empno,:new.ename,:new.sal,v_deptno);
end trig_view;	


--系统触发器，建立在数据库或模式上
--变异表触发器
--变异表 激发触发器的DML语句所操作的表，触发器为之定义的表，或者由于delete cascade操作而需要修改的表，即当前表的子表
--约束表 由于引用完整性约束而需要从中读取或修改数据的表，当前表的父表
--可以创建共享信息包实现既可以更新变异表，同时可以查询变异表

raise_application_error(-2001,'error information');
--不执行操作并提示信息

create or replace trigger updatetrigger
before update on emp
for each row
declare
	v_num number;
begin
	select count(*) into v_num from emp where deptno=:new.deptno;
	if(v_num>7) then
		RAISE_APPLICATION_ERROR(-2001,'error for no reason!');
	end if;
end;

--索引表
declare
	type indextables is table of number index by binary_integer; 
	--number为数据类型，也可通过%type获取
	--binary_integer为指定索引值的类型，也可以是pls_integer或varchar2
	v_number indextables;
begin
	for i in 1..5 loop
		v_number(i):=i*10;
	end loop;
	for i in 1..5 loop
		DBMS_OUTPUT.PUT_LINE(v_number(i));
	end loop;
end;
  
--嵌套表
declare
	type nametab is table of varchar2(50);
	v_tbale nametab :=nametab('wdg','lxx','lmx');   -----  【:=】赋值符号;【=】比较符号
begin 
	for i in 1..3 loop
		DBMS_OUTPUT.PUT_LINE(v_tbale(i));
	end loop;
end;
	

--外部表
---创建目录
create or replace directory datadir as 'D:\document\db\data';
create or replace directory logdir as 'D:\document\db\log';
create or replace directory baddir as 'D:\document\db\log';

grant read on directory datadir to weideguo;
grant write on directory logdir to weideguo;
grant write on directory baddir to weideguo;

--创建外部表
create table ext_emp   --创建表 
(
	emp_id number(4),
	ename varchar(10),
	job varchar(10),
	mgr_id number(4),
	hiredate varchar(20),
	salary number(8,2),
	dept_id number(2)
)
organization external     --说明建立外部表
(   
	type oracle_loader    --指定访问驱动，可以为oracle_loader和oracle_datapump
	default directory datadir  --指定默认目录对象
	access parameters(    --设置数据源文件与表中行之间的映射关系
		records delimited by newline  --设置记录的分隔符
		badfile baddir:'empxt%a_%p.bad' --不必须 --设置坏文件的存放目录和文件名
		logfile logdir:'empxt%a_%p.log' --不必须 --设置日志文件的存放目录和文件名
		fields terminated by ','  --设置文件中字段分隔符
		missing field values are null   --不必须  --设置无值字段处理,如果有这条语句，需要放在设置分隔符语句后？
		(                               --必须与创建时的顺序一致，并且不能漏
			emp_id,ename,job,mgr_id,    
			hiredate,salary,dept_id
		)
	)
	location('example2.dat')  --数据源文件，多个使用','分隔
) 
parallel  					--不必须  --支持对外部数据源文件的并行查询
reject limit unlimited;  	--不必须  --设置多少行转换失败时返回oracle错误，默认为0. 

create table ext_xyz
(
	name,sal
)
organization external
(
	type oracle_datapump
	default directory datadir
	location('example3.dat')
)
as
select name,sal from qotest0721_2;


--使用系统文件
DECLARE
fHandle UTL_FILE.FILE_TYPE;
begin
fHandle := UTL_FILE.FOPEN('D_OUTPUT/TXT','abc.txt','w');
UTL_FILE.PUT_LINE(fHandle,'woxiahuanlxx/dxx/axx');
UTL_FILE.FCLOSE(fHandle);
end;
	
--使用判断	
select name, 
case  
when x.sal>10000 then 9999
when x.sal<10000 and x.sal>5000 then 8888
else x.sal 
end
as sal
from qotest0721_2 x;


select ename,
       case job when 'CLERK' then sal*2
                when 'SALESMAN' then sal*3
       else sal end sal_c
from scott.emp;	

--行列转换
/*
ID Student Subject Score
1  张三    语文    90
2  张三    英语    95
3  李四    语文    89
4  李四    英语    78
5  王五    语文    99
6  王五    英语    94

姓名  语文  英语
张三  90    95
李四  89    78
王五  99    94

*/

select Student as '姓名',
max(case Subject when '语文' then Score else 0 end) as '语文' ,
max(case Subject when '英语' then Score else 0 end) as '英语'
from Scores
group by Student
order by Student

----以下也是可以  【SQL server】pivot为sql server的函数
/*
select Student as '姓名',
avg(语文) as '语文',
avg(英语) as '英语'
from Scores
pivot(
    avg(Score) for Subject 
    in (语文,英语)
    )as NewScores
group by Student
order by Student asc
*/
 

---删除表中多余的重复记录（多个字段），只留有rowid最小的记录 
delete from vitae a 
where (a.peopleId,a.seq) in (select peopleId,seq from vitae group by peopleId,seq having count(*) > 1) 
and rowid not in (select min(rowid) from vitae group by peopleId,seq having count(*)>1) 

xml表
create table xmltable of xmltype;
insert into xmltable values(xmltype(getclobdocument('EXP_DIR','order.xml')));    ---function getclobdocument需要自己编写 
查询xml
SELECT extractValue(value(X),'/PurchaseOrder/Reference') FROM XMLTABLE X;     --- extract(),extractValue(),和existsNode()
select * from xmltable;

CREATE OR REPLACE FUNCTION "WEIDEGUO"."GETCLOBDOCUMENT"(
dir      in varchar2,
filename in varchar2,
 charset in varchar2 default NULL)
 return CLOB deterministic
 is
    file            bfile := bfilename(dir,filename);
    charContent     CLOB := ' ';
    targetFile      bfile;
    lang_ctx        number := DBMS_LOB.default_lang_ctx;
    charset_id      number := 0;
    src_offset      number := 1 ;
    dst_offset      number := 1 ;
    warning         number;
 begin
   if charset is not null then
       charset_id := NLS_CHARSET_ID(charset);
   end if;
   targetFile := file;
   DBMS_LOB.fileopen(targetFile, DBMS_LOB.file_readonly);
   DBMS_LOB.LOADCLOBFROMFILE(charContent, targetFile,
           DBMS_LOB.getLength(targetFile), src_offset, dst_offset,
           charset_id, lang_ctx,warning);
   DBMS_LOB.fileclose(targetFile);
   return charContent;
 end;

 
启用高速缓存的function
create or replace function func1(...)
....
RESULT_CACHE RELIES_ON (table_name)   ----指定对某个表使用缓存
is
...
begin
...
end;
 
 
job
dbms_job包下的存储过程，通过job定时启动其他的存储过程
 

with t as (select level-1 n from dual connect by level <=10)
select * from t;   

with table_name as (select * from emp)
select * from table_name;
----创建一个中间表
-----可以使用多个as
-----可以使用多个as



--有条件多表插入 
--all 一条记录可以同时插入多个满足条件的表
--first 一条记录只插入第一个满足条件的表
insert all
when age>20 then into t1
when age<20 then into t2
select * from example;

--由查询创建表 CTAS
create table t 
as 
select empno,ename，sal from emp;


--连接查询
--子查询
--层次查询
select [level],column[,expression...]
from table_name
[where condition]
[start with column=vlue]
[connect by condition]
--level 伪列，表示记录的层次
where --记录选择条件
start with --层次查询起点
connect by 
--指定父记录与子记录之间的关系及分支选择条件 必须使用prior引用父记录
--如prior empno=mgr  父节点的empno等于子节点的mgr

select level,empno,ename,mgr from scott.emp 
start with ename='KING' 
connect by prior empno=mgr;    -----由根节点到子节点查询

select level,empno,ename,mgr from scott.emp 
start with ename='SMITH' 
connect by prior mgr=empno;    ----由子节点到根节点

分组函数
AVG
COUNT
MAX
MIN
STDDEV   ---标准偏差
SUM
VARIANCE   ---方差

group by  --分组查询
having    --对group by的结果进行筛选使用having
--rollup 生成横向统计和不分组统计
select deptno,job,avg(sal) from emp group by rollup(deptno,job);
--cube 生成横向统计、纵向统计和不分组统计
select deptno,job,avg(sal) from emp group by cube(deptno,job);
----限制分组函数结果不能使用where，需要使用having
select deptno,avg(sal) from scott.emp group by deptno having avg(sal)>2000;

--修改字段：
alter table tablename modify (column_name nvarchar2(20));
--添加字段：
alter table tablename add (column_name data_type [default value][null/not null],….);
--删除字段：
alter table tablename drop (column_name);



--merge同时完成数据的插入与更新
--两个表的字段都是empno,ename,deptno
merge into target_table t
using source_table s
on (t.empno=s.empno)
when matched then 
	update set t.ename=s.ename,t.deptno=s.deptno
when not matched then 
	insert values(s.empno,s.ename,s.deptno)

--合并查询 使用在多个select语气之间
union  		--并集，重复只保留一次
union all  	--并集，重复保留
intersect	--交集
minus		--差集	

外连接包括左连接、右连接、完整外部连接（左连接又称左外连接（left out join），右连接又称右外连接（right out join））
	左连接   ---左边的表全部显示，右边不匹配的表显示为空值
	select * from A left join B on A.a=B.b;

	右连接   ---右边的表全部显示，左边不匹配的表显示为空值
	select * from A right join B on A.a=B.b;

	全连接   ---左、右两边的表都显示，不匹配的以空值显示
	select * from A full join B on A.a=B.b；

内连接    ---左、右两边的表全部匹配
select * from A,B where A.a=B.b；
select * from A join B on A.a=B.b；

交叉连接(笛卡尔积)
select * from A,B;

oracle正则表达式
regexp_like    		
regexp_instr   		
regexp_substr  		
regexp_replace  	

select * from table_name where regexp(column_name,'regular_expression')

instr('str','str1')   计算str中str1在第几个字符之后
sub('str',n1,[n2])    截取str中第n1个字符之后,如果指定n2则指定截取的字符长度
replace('str','str1') 将str中有str1的替换为空

绑定变量
select &name name from dual;   ---需要客户端的支持

--计算行数
select count(*) from t_n;
--计算列数
select count(*) from user_tab_columns where table_name='table_name';


distinct   ---用于查询时指定输出值不重复，【distinct 】必须跟在【select】之后	

----拼音
SELECT * FROM table_name ORDER BY NLSSORT(column_name,'NLS_SORT = SCHINESE_PINYIN_M')
----笔划
SELECT * FROM table_name ORDER BY NLSSORT(column_name,'NLS_SORT = SCHINESE_STROKE_M')
----部首
SELECT * FROM table_name ORDER BY NLSSORT(column_name,'NLS_SORT = SCHINESE_RADICAL_M')


date输入格式

fm  --字符串前没有零 【to_char(hiredate,'fmyyyy-mon-dd')】为2016-jan-1
fx  --字符串前有零，默认使用这个模式 【to_char(hiredate,'fxyyyy-mon-dd')】为2016-jan-01
01-jan-2016
01 jan 2016
01-january-2016
01 january 2016
01-jan-16
01 jan 16
01-january-16
01 january 16	
01/jan/16
01/january/16	
	
【interval  day to second】 插入格式【interval '5 12:00:00.000' day to second】，【day/second】可以选【year/month/day/hour/minute/second】

timestamp with time zone	
	
	
bfile 
create tbale bfile_test(f bfile,...);
insert into bfile_test(bfilename('directory_path','file_name'),...);

clob   ---可以直接以字符串插入

blob   ----存储二进制值

long   ---可以直接以字符串插入，一个表只能有一个long的字段，推荐使用clob代替	
		
	
数据类型
一 字符串类型
1.1：CHAR类型，CHAR(size [BYTE | CHAR])，存储2,000字节，定长字符串，会用空格填充来达到其最大长度，不指定CHAR长度，则默认为1
1.2：NCHAR类型，存储2,000字节 定长字符串，包含UNICODE格式数据。
		SELECT translated_description FROM product_descriptions  WHERE translated_name = N'LCD Monitor 11/PM';   ----=插叙nchar数据类型需要转换
1.3：VARCHAR类型，与VARCHAR2同义词
1.4：VARCHAR2类型，存储4,000字节，变长字符串，它不会使用空格填充至最大长度。
1.5：NVARCHAR2类型，存储4,000字节，变长字符串，包含UNICODE格式数据。
二 数字类型
2.1：NUMBER(P,S)
			P 是Precison的英文缩写，即精度缩写，表示有效数字的位数，最多不能超过38
			S是Scale的英文缩写，可以使用的范围为-84~127。正数，表示从小数点到最低有效数字的位数；负数时，表示从最大有效数字到小数点的位数
2.2：INTEGER是NUMBER的子类型，它等同于NUMBER（38,0），存储整数
2.3：FLOAT类型，Float(n),数 n 指示位的精度，可以存储的值的数目。N 值的范围可以从 1 到 126。若要从二进制转换为十进制的精度，请将 n 乘以 0.30103。
2.4：BINARY_FLOAT
			32位单精度浮点数字数据类型。可以支持至少6位精度,每个值需要 5 个字节，包括长度字节。
	 BINARY_DOUBLE
			64位双精度浮点数字数据类型。每个值需要9个字节，包括长度字节。
三 日期类型
3.1 DATE类型
		DATE是最常用的数据类型，日期数据类型存储日期和时间信息。虽然可以用字符或数字类型表示日期和时间信息，但是日期数据类型具有特殊关联的属性。为每个日期值，Oracle 存储以下信息： 世纪、 年、 月、 日期、 小时、 分钟和秒。一般占用7个字节的存储空间。
3.2 TIMESTAMP类型
		这是一个7字节或12字节的定宽日期/时间数据类型。它与DATE数据类型不同，因为TIMESTAMP可以包含小数秒，带小数秒的TIMESTAMP在小数点右边最多可以保留9位
3.3 TIMESTAMP WITH TIME ZONE类型
		这是TIMESTAMP类型的变种，它包含了时区偏移量的值
3.4 TIMESTAMP WITH LOCAL TIME ZONE类型
3.5 INTERVAL YEAR TO MOTH
3.6 INTERVAL DAY TO SECOND
四 LOB类型
4.1 CLOB 数据类型
	它存储单字节和多字节字符数据。支持固定宽度和可变宽度的字符集。CLOB对象可以存储最多 (4 gigabytes-1) * (database block size) 大小的字符
4.2 NCLOB 数据类型
	它存储UNICODE类型的数据，支持固定宽度和可变宽度的字符集，NCLOB对象可以存储最多(4 gigabytes-1) * (database block size)大小的文本数据。
4.3 BLOB 数据类型
	它存储非结构化的二进制数据大对象，它可以被认为是没有字符集语义的比特流，一般是图像、声音、视频等文件。BLOB对象最多存储(4 gigabytes-1) * (database block size)的二进制数据。
4.4 BFILE 数据类型
	二进制文件，存储在数据库外的系统文件，只读的，数据库会将该文件当二进制文件处理。
五  RAW & LONG RAW类型
5.1 LONG类型
	它存储变长字符串，最多达2G的字符数据（2GB是指2千兆字节， 而不是2千兆字符），与VARCHAR2 或CHAR 类型一样，存储在LONG 类型中的文本要进行字符集转换。ORACLE建议开发中使用CLOB替代LONG类型。支持LONG 列只是为了保证向后兼容性。CLOB类型比LONG类型的限制要少得多。
5.2 LONG RAW 类型，能存储2GB 的原始二进制数据（不用进行字符集转换的数据）
5.3 RAW类型
	用于存储二进制或字符类型数据，变长二进制数据类型，这说明采用这种数据类型存储的数据不会发生字符集转换。这种类型最多可以存储2,000字节的信息
六 ROWID & UROWID类型	
	
	
转译符
select * from scott.emp where ename like '%\%%' escape '\';	----使用【\】转换【%】，转换符【\】可以使用其他符号代替
	
	
-- limit的实现
select owner,table_name from ALL_TABLES where rownum<=10;
