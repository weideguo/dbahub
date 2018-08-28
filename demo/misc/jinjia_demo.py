#!/usr/bin/env python
#-*- coding:utf-8 -*-
import jinja2
import os

##创建模板环境
#
env = jinja2.Environment(loader=jinja2.FileSystemLoader('/srv/salt/config_install/model'))

##载入模板
t1 = env.get_template('hc/server%(ServerId)s/config/proxool.xml')

##设置数据源
data = {'ConfigDbIp':'10.0.0.128','ConfigDbPort':3380,'ProductDbIp':'10.0.0.129','ProductDbPort':3381,'DbIp':'10.0.0.1','DbPort':3306,'is_kuafu':True}
##替换文件中的{{ConfigDbIp}}、{{ConfigDbPort}}

##渲染
result = t1.render(data)

print result


###{{'}}'}} 转义
#######################过滤器用法###################
import base64

#定义一个过滤器
def decode_file(file):
	'''解码base64编码的文件名'''
	return base64.urlsafe_b64decode(file).split(':)_')[-1]


env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(os.path.abspath(__file__))))

#注册过滤器到模板环境
env.filters['decode_file'] = decode_file

t_filter = env.get_template('template.conf')

data = {'source_filename':'MTQ5NTY5MTk0NS42NDgwNzc6KV91bml0X2NyZWF0ZTExMS56aXA=','file_md5':'6ea46b6619f133b87350261f426dd76b','file_size':10650,'test_list':['10.0.0.129','10.0.0.1']}

result = t_filter.render(data)

print result
