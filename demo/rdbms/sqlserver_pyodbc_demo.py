"""
可能会遇到TLS问题
"""
import pyodbc


host = "127.0.0.1"
port = "1433"
user = "sa"
password = "111111111111"
#charset = "Chinese_PRC_CI_AS"
#charset = "UTF-8"
charset = "SQL_Latin1_General_CP1_CI_AS"
# 设置怎样的值都可以？需要在创建数据库时选用正确的排序编码


connstr = """DRIVER=ODBC Driver 17 for SQL Server;SERVER={0},{1};UID={2};PWD={3};client charset = UTF-8;connect timeout=10;CHARSET={4};""".format(
            host,
            port,
            user,
            password,
            charset,
          )

conn = pyodbc.connect(connstr)


sql = "select * from mytestdb..test2"
cursor = conn.cursor()
cursor.execute(sql)
# rows = cursor.fetchmany(int(10))
rows = cursor.fetchall()
#fields = cursor.description
print(rows)
