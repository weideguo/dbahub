分区表

主键/唯一键限制
every unique key on the table must use every column in the table s partitioning expression 
如果有多个唯一键/包括主键，则构成键的部分必须使用在分区表达式中，即所有唯一键中必须包含相同列，且要使用该列进行分区
没有主键，则分区的字段没有任何限制


SELECT * FROM p1 PARTITION (p0[,p1]);                                #从指定分区查询
EXPLAIN PARTITIONS SELECT * FROM p1 WHERE column_name=10;            #查看从分区表的执行信息
ALTER TABLE tr DROP PARTITION p2;                                    #删除分区，针对RANGE/LIST分区
ALTER TABLE tr ADD PARTITION (PARTITION p_name …);                   #增加分区，针对RANGE/LIST分区
ALTER TABLE members REORGANIZE PARTITION p0,p1,p2,p3 INTO (
        PARTITION m0 …,
        PARTITION m1 …);                                             #调整RANGE/LIST分区
ALTER TABLE tr COALESCE PARTITION 4;                                 #减小HASH/KEY分区
ALTER TABLE tr ADD PARTITION PARTITIONS 6;                           #增多HASH/KEY分区
ALTER TABLE tr TRUNCATE PARTITION p_name;                            #删除分区的数据


CREATE TABLE tb_name ...
PARTITION BY RANGE  ...


CREATE TABLE employees (
    id INT NOT NULL,
    fname VARCHAR(30),
    lname VARCHAR(30),
    hired DATE NOT NULL DEFAULT '1970-01-01',
    separated DATE NOT NULL DEFAULT '9999-12-31',
    job_code INT NOT NULL,
    store_id INT NOT NULL
)
PARTITION BY RANGE (store_id) (
    PARTITION p0 VALUES LESS THAN (6),
    PARTITION p1 VALUES LESS THAN (11),
    PARTITION p2 VALUES LESS THAN (16),
    PARTITION p3 VALUES LESS THAN (21)
);


PARTITION BY RANGE COLUMNS(a,d,c) (
    PARTITION p0 VALUES LESS THAN (5,10,'ggg'),
    PARTITION p1 VALUES LESS THAN (10,20,'mmm'),
    PARTITION p2 VALUES LESS THAN (15,30,'sss'),
    PARTITION p3 VALUES LESS THAN (MAXVALUE,MAXVALUE,MAXVALUE)
);


PARTITION BY LIST(store_id) (
    PARTITION pNorth VALUES IN (3,5,6,9,17),
    PARTITION pEast VALUES IN (1,2,10,11,19,20),
    PARTITION pWest VALUES IN (4,12,13,14,18),
    PARTITION pCentral VALUES IN (7,8,15,16)
);


PARTITION BY HASH(store_id)
PARTITIONS 4;


PARTITION BY HASH( YEAR(hired) )
PARTITIONS 4;


-- 类似hash 但使用主键 或者NOT NULL唯一键  使用hash函数 PASSWORD()
PARTITION BY KEY()
PARTITIONS 2;


-- 复合分区 分区数 3 * 2 = 6 
PARTITION BY RANGE( YEAR(purchased) )
SUBPARTITION BY HASH( TO_DAYS(purchased) )
SUBPARTITIONS 2 (
    PARTITION p0 VALUES LESS THAN (1990),
    PARTITION p1 VALUES LESS THAN (2000),
    PARTITION p2 VALUES LESS THAN MAXVALUE
);


CREATE TABLE xxx (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`request_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '请求时间',
...
PRIMARY KEY (`id`,`request_time`),
...
)
PARTITION BY RANGE (UNIX_TIMESTAMP(`request_time`))
(
PARTITION p_202112 VALUES LESS THAN (1640966400),
PARTITION p_202201 VALUES LESS THAN (1643644800),
...
PARTITION pmax VALUES LESS THAN MAXVALUE);



CREATE TABLE xxx2 (
`id` bigint(20) NOT NULL AUTO_INCREMENT,
`request_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '请求时间',
...
PRIMARY KEY (`id`,`request_time`),
...
)
PARTITION BY RANGE (TO_DAYS(`request_time`))
(
PARTITION p_202112 VALUES LESS THAN (TO_DAYS('2022-01-01')),
PARTITION p_202201 VALUES LESS THAN (TO_DAYS('2022-02-01')),,
...
PARTITION pmax VALUES LESS THAN MAXVALUE);


MRG_MYISAM
--MYISAM的分区表 比较老的版本使用 5.5以上MyISAM以及支持分区表
CREATE TABLE `article_0` ( `id` BIGINT( 20 ) NOT NULL , `subject` VARCHAR( 200 ) NOT NULL , PRIMARY KEY ( `id` ) ) ENGINE = MYISAM ;
CREATE TABLE `article_1` ( `id` BIGINT( 20 ) NOT NULL , `subject` VARCHAR( 200 ) NOT NULL , PRIMARY KEY ( `id` ) ) ENGINE = MYISAM ;

CREATE TABLE `article_merge` ( `id` BIGINT( 20 ) NOT NULL , `subject` VARCHAR( 200 ) NOT NULL , PRIMARY KEY ( `id` ) ) ENGINE=MRG_MyISAM DEFAULT CHARSET=utf8 UNION=(article_0,article_1);

--插入数据只能往后端的表操作
--更新 删除可以在前端表操作
