
"""
from django.db import models
class MyModel(models.Model):
    id = models.AutoField(ID', primary_key=True)
    col1 = models.CharField('字段1', max_length=50)
    col2 = models.CharField('字段2', max_length=50)
"""
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




