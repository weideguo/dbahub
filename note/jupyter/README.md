# jupyter
web形式的交互编辑器  
可以直接运行python、shell、markdown等  
文件后缀ipynb，以json格式存储  


## start
```shell
#安装
pip install jupyter

#启动
nohup jupyter notebook --ip=0.0.0.0 --port=8888 &

扩展安装
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install

#设置主题
pip install jupyterthemes
jt -l
jt -t chesterish
```