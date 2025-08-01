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

# 设置扩展支持
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install

# 安装扩展
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension

#设置主题
pip install jupyterthemes
jt -l
jt -t chesterish
```

```shell
# docker中使用
docker pull jupyter/base-notebook:latest

# 映射到服务器8080
mkdir /data/work
chown -R 1000:100 /data/work    # jupyter docker环境默认映射到主机的账号
docker run -d -p 8080:8888 -v /data/work:/home/jovyan jupyter/base-notebook:latest

```

## 新版本
* JupyterLab        未来趋势
* Jupyter Notebook  简单交互
* nbclassic         丰富的交互
