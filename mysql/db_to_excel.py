#!/usr/bin/env python2.7
#coding=utf-8
import ConfigParser
import codecs
#import mysql.connector
import MySQLdb
import xlwt
import time

config_file='config.conf'
cp=ConfigParser.SafeConfigParser()
with codecs.open(config_file,'r',encoding='utf-8') as f:
    cp.readfp(f)
	
def to_excel():
    db_user=cp.get('database','user')
    db_password=cp.get('database','password')
    db_host=cp.get('database','host')
    db_port=cp.get('database','port')
    db_name=cp.get('database','db_name')
    tb_name=cp.get('database','tb_name')
    get_sql='select * from '+tb_name
    #conn = mysql.connector.connect(user=db_user, password=db_password, host=db_host,port=int(db_port),database=db_name,charset='utf8')
    conn = MySQLdb.connect(user=db_user, passwd=db_password, host=db_host,port=int(db_port),db=db_name,charset='utf8')
    cursor=conn.cursor()
    cursor.execute(get_sql)
    results=cursor.fetchall()
    
    wb = xlwt.Workbook(encoding='utf-8')
    sheet = wb.add_sheet('stats')
    sheet_header=cp.get('output','column_name').split(',')
    n=0
    for sheet_h in sheet_header:
        try:
            sheet.write(0,n,sheet_h.encode('utf8'))
        except:
            sheet.write(0,n,sheet_h.encode('gbk'))
        n=n+1
    
    i=1
    for result in results:
        for j in range(len(sheet_header)):
            sheet.write(i,j,result[j])
        i=i+1
    wb.save(cp.get('output','filename'))
    conn.commit()
    conn.close()
	
if  __name__ == '__main__':
    print "%s"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    to_excel()
    print "%s"%time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
