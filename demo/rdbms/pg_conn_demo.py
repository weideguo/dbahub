import psycopg2 

"""
参数支持
https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-PARAMKEYWORDS

connect_timeout 超时秒
client_encoding 编码
"""
conn = psycopg2.connect(database="postgres", user="pg_user", password="ps_user_password", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("select * from a")
cur.fetchall()   
conn.commit()
conn.close()
