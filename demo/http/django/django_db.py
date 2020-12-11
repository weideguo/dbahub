#coding:utf8
from django.db import connection,transaction


cursor = connection.cursor()
"""
cursor.execute("select * from a")
data = cursor.fetchall()
cursor.close()
conn.close()
"""
#使用事务 同时提交或回滚
#with transaction.atomic(using='default'):
with transaction.atomic():
    cursor.execute("insert into a values(111,'xxxx');")
    cursor.execute("insert into a values(111,'kkk');")
    cursor.execute("insert into a values(111,'yyyy');")

cursor()

"""
# settings.py

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wdg',
        'USER': 'weideguo',
        "PORT": 1039,
        "PASSWORD": 'weideguo',
        "HOST": '127.0.0.1'
    }
}



#使用连接池 是否需要使用？
DATABASES = {
    'default': {
        ...
        'ENGINE': 'dj_db_conn_pool.backends.mysql'
        ...
        'POOL_OPTIONS' : {
            'POOL_SIZE': 10,
            'MAX_OVERFLOW': 10
        }
    }
}
"""




