
export PYTHONPATH="/path_to_python_project_home"             
#通过修改环境变量确定python项目的根目录，从而可以导入其他模块


##############################################################################


import os
import sys


print __file__                       
print os.path.dirname(__file__)                        #为相对路径

print sys.argv[0]                                       #文件名
print os.path.realpath(sys.argv[0])
print os.path.dirname(os.path.realpath(sys.argv[0]))    #为绝对路径

print os.path.abspath(__file__)                         #文件的绝对路径

sys.path.append(os.path.dirname(os.path.realpath(sys.argv[0]))+"/../")      #切换到上层目录以导入其他模块




##################################################################################
python -m pack1.subpack1.real_name                     #以-m方式启动 pack1/subpack1/real_name.py  即可以pack1为路径导入其他模块 


###real_name.py
import pack1.subpack2


####################
pack1
|
+-----------+
|           |  
subpack1   subpack2
|
real_name.py
