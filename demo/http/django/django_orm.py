#coding:utf8

#链接池使用
#pip install django-db-connection-pool

#setting.py
DATABASES = {
    'default': {
        'ENGINE': 'dj_db_conn_pool.backends.mysql'
        'POOL_OPTIONS' : {
            'POOL_SIZE': 10,
            'MAX_OVERFLOW': 10
        }
        
    }
}


#models.py
from django.db import models
class MyModel(models.Model):
    id = models.AutoField(ID', primary_key=True)
    col1 = models.CharField('字段1', max_length=50)
    col2 = models.CharField('字段2', max_length=50)



#mymodule.py
filter_dict={}
filter_dict['id'] = 11
#查询
r1 = MyModel.objects.filter(**filter_dict)

search="xxx"
#模糊查询
from django.db.models import Q
r = r1.filter(Q(col1__icontains=search) | Q(col2__icontains=search))

#事务
from django.db import transaction
with transaction.atomic():
    """
    orm transaction operation in here
    """

#select is_manual from SqlWorkflow where id=35 limit 1;
SqlWorkflow.objects.filter(id=35).values('is_manual').first() 

#get 结果只有一个
#先select * from from SqlWorkflow; 然后再在python中过滤
SqlWorkflow.objects.get(id=35).is_manual

