#死锁示例



create table ty (
  id int not null primary key auto_increment ,
  c1 int not null default 0,
  c2 int not null default 0,
  c3 int not null default 0,
  unique key uc1(c1),
  unique key uc2(c2)
) engine=innodb ;


insert into ty(c1,c2,c3) values(1,3,4);
insert into ty(c1,c2,c3) values(6,6,10);
insert into ty(c1,c2,c3) values(9,9,14);




t1                                          |        t2
                                            |
                                            |
begin;                                      |        
                                            |
                                            |       begin;
                                            |
                                            |
                                            |
update ty set c3=2 where c2=4;              |        
                                            |        update ty set c3=2 where c2=4;
                                            |
                                            |
insert into ty (c1,c2,c3) values(3,4,2);    |
                                            |
                                            |
                                            |        insert into ty (c1,c2,c3) values(3,4,2);
                                            |
                                            |
                                                    
                                                   