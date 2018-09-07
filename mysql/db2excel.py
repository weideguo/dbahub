#!/usr/bin/env python2.7
#coding=utf-8
#
# output table in database to excel,table should have comment
#
# vim config.conf
# [database]
# user     = "user"
# password = "password"
# host     = "host"
# port     = "port"
# db_name  = "db_name"
# tb_name  = "tb_name"
# filename = "filename"


import ConfigParser
import codecs
#import mysql.connector
import MySQLdb
import xlwt
import time
import sys
import os


file_home=sys.path[0]+'/data/'
if os.path.exists(file_home)!=True:
	os.makedirs(file_home)

config_file=sys.path[0]+'/config.conf'
cp=ConfigParser.SafeConfigParser()
with codecs.open(config_file,'r',encoding='utf-8') as f:
    cp.readfp(f)
	
db_user=cp.get('database','user')
db_password=cp.get('database','password')
db_host=cp.get('database','host')
db_port=cp.get('database','port')
db_name=cp.get('database','db_name')
tb_name=cp.get('output','tb_name')
filename=cp.get('output','filename')

def to_excel():
    get_sheet_header_sql="select COLUMN_COMMENT from information_schema.columns WHERE TABLE_SCHEMA=\'"+db_name+"\' and table_name=\'"+tb_name+"\';"
    get_sql='select * from '+tb_name
    #conn = mysql.connector.connect(user=db_user, password=db_password, host=db_host,port=int(db_port),database=db_name,charset='utf8')
    conn = MySQLdb.connect(user=db_user, passwd=db_password, host=db_host,port=int(db_port),db=db_name,charset='utf8')
    cursor=conn.cursor()
    cursor2=conn.cursor()
    cursor.execute(get_sql)
    results=cursor.fetchall()
        
    cursor2.execute(get_sheet_header_sql)
    sheet_header=cursor2.fetchall()
        
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet('stats')
    
    n=0
    for sheet_h in sheet_header:
        sheet.write(0,n,sheet_h[0].encode('utf8'))
        n=n+1
    i=1
    for result in results:
        for j in range(len(sheet_header)):			
            value=result[j]			
            sheet.write(i,j,value)
        i=i+1
    wb.save(file_home+filename)
    #reset_sql='update '+tb_name+' set flag=0'
    #cursor.execute(reset_sql)
    #conn.commit()
    conn.close()
	
	
if  __name__ == '__main__':
	print "%s"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	to_excel()
	print "%s"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))	
