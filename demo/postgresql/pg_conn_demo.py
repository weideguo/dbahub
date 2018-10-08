import psycopg2 


conn = psycopg2.connect(database="postgres", user="pg_user", password="ps_user_password", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("select * from a")
cur.fetchall()   
conn.commit()
conn.close()
