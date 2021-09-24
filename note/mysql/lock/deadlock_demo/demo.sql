
drop table if exists t;
CREATE TABLE t (i INT) ENGINE = InnoDB;
INSERT INTO t (i) VALUES(1);




T1                                                   |   T2

START TRANSACTION;                                   |   START TRANSACTION;
                                                     |   
SELECT * FROM t WHERE i = 1 LOCK IN SHARE MODE;      |   DELETE FROM t WHERE i = 1;
                                                     |
DELETE FROM t WHERE i = 1;                           |   -- deadlock



T1
S lock 

T2
The lock cannot be granted because it is incompatible with the S lock that T1 holds, so the request goes on the queue of lock requests for the row and T2 blocks. 

T1 
needs an X lock 
that lock request cannot be granted because T2 already has a request for an X lock and is waiting for T1 to release its S lock. 
Nor can the S lock held by T1 be upgraded to an X lock because of the prior request by B for an X lock.

 
 
