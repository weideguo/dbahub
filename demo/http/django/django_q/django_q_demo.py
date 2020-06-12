#coding:utf8
"""
#需要额外于django启动
python manage.py qcluster
#启用django-admin
#进入django-admin的页面可以管理
"""

"""
#调用模块

cat > my_model.py << EOF
#coding:utf8
import time

def my_func(*args,**kwargs):
    with open("/tmp/1.txt","w") as f:
        f.write(str(time.time())) 
        #由async_task之后的参数传入
        f.write(str(args)) 
        #没有传入值
        #f.write(str(kwargs))
    
    time.sleep(10) 

def my_callback(task):
    #task.args        #传给调用函数的参数
    #task.stopped     #调用函数运行结束时间
    #task.result      #调用函数返回的结果
    with open("/tmp/2.txt","w") as f:
        f.write(str(time.time())) 
       
EOF

"""
#异步任务
from django_q.tasks import async_task
async_task('my_model.my_func', 'aaa', timeout=-1, task_name='test111')


#定时任务
from django_q.tasks import schedule
#数据库orm对象
from django_q.models import Schedule

#查看schedule_type
print(Schedule.TYPE)


import datetime
next_run=datetime.datetime.strptime("2020-06-01 16:23:00","%Y-%m-%d %H:%M:%S")
schedule('my_model.my_func','ccc',name='name_xxx', schedule_type='O',repeats=-1, next_run=next_run,timeout=-1)


import datetime
next_run=datetime.datetime.strptime("2020-06-01 16:09:00","%Y-%m-%d %H:%M:%S")
schedule('my_model.my_func','ccc',hook='my_model.my_callback',name='name_yyy', schedule_type='I',repeats=-1, next_run=next_run,timeout=-1)



