#安装
#pip install celery
#pip install django-celery 

#settings.py
INSTALLED_APPS = ['djcelery']

import djcelery
from celery import platforms
from celery.schedules import crontab
platforms.C_FORCE_ROOT = True
djcelery.setup_loader()
#redis :// [: password@] host [: port] [/ database][? [timeout=timeout[d|h|m|s|ms|us|ns]]
BROKER_URL = 'redis://:{}@{}:{}/0'              # redis broker
CELERY_RESULT_BACKEND = 'redis://:{}@{}:{}/1'   # redis backend
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_ENABLE_UTC = True
CELERY_IMPORTS = ('model1.sub_model1',)         # from model1.sub_model1 import XXX
CELERYBEAT_SCHEDULE = {                         
    'mycron_task': {
        'task': 'model1.sub_model1.mycron_task',  # from model1.sub_model1 import mycron_task        
        'schedule': crontab(),                  #执行格式如同linux的crontab
        'agrs':()
    }
}
CELERY_BUSINESS_PARAMS = {
    'username':'定时处理器',
    'handle_type': 'execute',
    'date_format': '%Y-%m-%d %H:%M'
}




#启动
python manage.py celery worker 



#使用如同正常的celery




#管理
#启用django-admin
#进入django-admin的页面可以管理


