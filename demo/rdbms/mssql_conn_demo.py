import pymssql

host='127.0.0.1',
user='my_mssql_user',
password='my_mssql_passwd',
database='my_mssql_database'

conn=pymssql.connect(host=host,user=user,password=password,database=database)






