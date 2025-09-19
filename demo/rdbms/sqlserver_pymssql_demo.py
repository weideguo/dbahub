"""
基于FreeTDS，更为简单
"""
import pymssql


server = "10.30.20.15"
port = 1433
user = "sa"
password = "sa_password"
database = "my_db"
charset = "utf-8"

conn = pymssql.connect(
    server=server,
    port=port,
    user=user,
    password=password',
    database=database,
    charset=charset
)

cursor = conn.cursor()

sql = "SELECT @@VERSION"
cursor.execute(sql)
row = cursor.fetchone()
print(row)


sql = "SELECT * FROM test_20250915_2"
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)



sql = "INSERT INTO test_20250915_5 VALUES(%s)"
cursor.execute(sql,("中文测试",))
conn.commit()




conn.close()

