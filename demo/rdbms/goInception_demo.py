#!/usr/bin/env python
# -*- coding:utf-8 -*-
#goInception的使用 衍生于Inception
#需要额外部署goInception 一个类似于mysql的服务 可以直接以mysql连接的形式连接
#用于实现SQL审核，即审核SQL DDL/DML语气，如检查建表语句是否存在主键、注释等
#

import pymysql
import prettytable as pt
tb = pt.PrettyTable()

#--check=1  #只是检查语句是否可以执行，不会往数据库中写
#要执行sql的库 需要能执行sql的权限
sql = '''/*--user=test;--password=test;--host=127.0.0.1;--port=1039;--check=1;*/
inception_magic_start;
use test_inc;
create table t1(id int primary key,c1 int);
inception_magic_commit;
'''

sql = '''/*--user=test;--password=test;--host=127.0.0.1;--port=1039;--enable-check;*/
inception_magic_start;
use test;
create table t1111(id int primary key,c1 int);
inception_magic_commit;
'''

#
#--execute=1 #执行sql
#--backup=1  #备份
#
#需要有权限 REPLICATION CLIENT,REPLICATION CLIENT
#使用binlog解析生成恢复语句存储于备份库（备份库在goInception配置文件中设置）
#如执行 create 语句，则生成 drop 语句存于备份库
sql = '''/*--user=test;--password=test;--host=127.0.0.1;--port=1039;--execute=1;--backup=1;*/ inception_magic_start;            
use `wdg`; 
create table x(a int); 
inception_magic_commit;'''

#goInception的配置
conn = pymysql.connect(host='127.0.0.1', user='', passwd='', db='', port=4000, charset="utf8mb4")
cur = conn.cursor()
ret = cur.execute(sql)
result = cur.fetchall()
cur.close()
conn.close()

tb.field_names = [i[0] for i in cur.description]
for row in result:
    tb.add_row(row)

print(tb)




