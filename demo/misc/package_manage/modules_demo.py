#coding:utf8

import sys
help("modules")     ###python查看已经安装的模块
print(sys.path)     #查看模块的位置
"""
命令行直接查看
python -c "import sys;print(sys.path)" 
"""

#添加模块的存储路径
sys.path.append("/path_to_store_python_model")

"""
#不同的加载py文件的方式，主要是影响sys.path这个属性。
python xxx.py          #sys.path多加载脚本所在的目录
python -m xxx          #sys.path多加载执行命令时的目录
"""