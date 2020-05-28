#coding:utf8

import pymysql
import prettytable as pt
tb = pt.PrettyTable()

sql = '''
select * from a;
'''

conn = pymysql.connect(host='127.0.0.1', user='test', passwd='test',
                       db='test', port=1039, charset="utf8mb4")
cur = conn.cursor()
ret = cur.execute(sql)
result = cur.fetchall()
cur.close()
conn.close()

tb.field_names = [i[0] for i in cur.description]
for row in result:
    tb.add_row(row)

#美化显示结果
print(tb)