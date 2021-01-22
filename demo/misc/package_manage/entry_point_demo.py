#coding:utf8

__requires__ = 'Django==1.11.21'
import re
import sys
from pkg_resources import load_entry_point


execute_from_command_line=load_entry_point('Django==1.11.21', 'console_scripts', 'django-admin')

"""
#entry_point 信息文件
#cd /usr/lib64/python2.7/site-packages/Django-1.11.21.dist-info && cat entry_points.txt
[console_scripts]
django-admin = django.core.management:execute_from_command_line
"""    

#相当于执行
from django.core.management import execute_from_command_line   
