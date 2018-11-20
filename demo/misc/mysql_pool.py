#!/bin/env python
#coding:utf8


import MySQLdb
from DBUtils.PooledDB import PooledDB
from config_api import *

pool=PooledDB(MySQLdb,mincached=5,maxcached=10,maxshared=0,maxconnections=10,host=db_host,port=db_port,user=db_user,passwd=db_password,charset=charset)

conn=pool.connection()
