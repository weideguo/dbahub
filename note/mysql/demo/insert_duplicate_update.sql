INSERT ... ON DUPLICATE KEY UPDATE         引发死锁

参考文档：
https://bugs.mysql.com/bug.php?id=21356
https://bugs.mysql.com/bug.php?id=52020



---demo1
CREATE TABLE `test` (
`id` int(11) NOT NULL AUTO_INCREMENT,
`c1` varchar(20) DEFAULT NULL,
`c2` varchar(20) DEFAULT NULL,
`c3` int(11) DEFAULT '0',
PRIMARY KEY (`id`),
UNIQUE KEY `idx_c1` (`c1`,`c2`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;


                                                                                   |
t1                                                                                 |     t2
begin;                                                                             |    begin;
                                                                                   |
insert into test(c1,c2) values('d','2') ON DUPLICATE KEY UPDATE c3=c3+1;           |
                                                                                   |    --因为t1加了gap lock 类似所有操作都会被锁
                                                                                   |    insert into test(c1,c2) values('c','1') ON DUPLICATE KEY UPDATE c3=c3+1;
--任意一个                                                                         |
insert into test(c1,c2) values('d','1') ON DUPLICATE KEY UPDATE c3=c3+1;           |
insert into test(c1,c2) values('c','1') ON DUPLICATE KEY UPDATE c3=c3+1;           |
                                                                                   |    ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
                                                                                   |
                                                                                   |
                                                                                   |






---demo2


CREATE TABLE `test1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderId` int(11) NOT NULL,
  `extraInfo` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `orderId` (`orderId`)
) ENGINE=InnoDB ;                                                                                     |
                                                                                                      |
                                                                                                      |
t1                                                                                                    |  t2                                                                                                             |   t3
                                                                                                      |                                                                                                                 |
begin;                                                                                                |                                                                                                                 |
INSERT INTO test1(orderId, extraInfo) VALUES (1,'') ON DUPLICATE KEY UPDATE extraInfo = '';           |  begin;                                                                                                         |
                                                                                                      |                                                                                                                 |
                                                                                                      |                                                                                                                 |
                                                                                                      |                                                                                                                 |
                                                                                                      |                                                                                                                 |
                                                                                                      |   INSERT INTO test1(orderId, extraInfo) VALUES (2,'') ON DUPLICATE KEY UPDATE extraInfo = '';                   |    begin;
                                                                                                      |                                                                                                                 |
                                                                                                      |                                                                                                                 |
                                                                                                      |                                                                                                                 |    --大于等于2均可
                                                                                                      |                                                                                                                 |    INSERT INTO test1(orderId, extraInfo) VALUES (2,'') ON DUPLICATE KEY UPDATE extraInfo = '';
                                                                                                      |                                                                                                                 |    INSERT INTO test1(orderId, extraInfo) VALUES (3,'') ON DUPLICATE KEY UPDATE extraInfo = '';
                                                                                                      |                                                                                                                 |
commit;                                                                                               |                                                                                                                 |
                                                                                                      |                                                                                                                 |
                                                                                                      |                                                                                                                 |    ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
                                                                                                      |
                                                                                                      |













