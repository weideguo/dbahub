#!/bin/env python
#coding:utf8
#命令行格式提示
from optparse import OptionParser

options = OptionParser(usage='%prog [options]', description='model description in here')
options.add_option('-p', '--port', type='int', default=443, help='description for var p/port (default: 443)')

my_desc="中文描述"
try:
    #python3已经是unicode，不需要再转换
    my_desc=my_desc.decode('utf8')
except:
    pass

#-h 用于显示帮助，不能再修改
options.add_option('--host', type='str', default='127.0.0.1', help=my_desc)


opts, args = options.parse_args()
print(opts)
print(args)
print("########################################")
options.print_help()

