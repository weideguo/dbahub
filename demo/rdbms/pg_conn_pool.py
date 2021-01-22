
conn_conf={
"host"     : "127.0.0.1"
,"port"    : 5432
,"database": "my_gp_database"
,"user"    : "my_gp_user"
,"password": "my_pg_passwd"
,"min_conn": 4
,"max_conn": 10
}
                 

import psycopg2
import psycopg2.pool
                                                
gp_pool = psycopg2.pool.ThreadedConnectionPool(minconn=conn_conf['min_conn'], maxconn=conn_conf['max_conn'],
                                               database=conn_conf['database'], host=conn_conf['host'],
                                               port=conn_conf['port'], user=conn_conf['user'],
                                               password=conn_conf['password'])
                                                   
                                                   
conn = gp_pool.getconn()
#cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
cur = conn.cursor()

sql="select * from information_schema.tables; "
params=[]
cur.execute(sql, params)
data = cur.fetchall()


gp_pool.putconn(conn)
                                                   

                                                   
       
"""                                                                                    
psql db_game_data  -U  gp_gl_user -h 10.13.190.115 -p 5432 -W       

"""