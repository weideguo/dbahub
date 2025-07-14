# 如何使用mkdocs

## 基础使用
``` shell
pip install mkdocs

# 创建项目
mkdocs new mkdocs_demo
cd mkdocs_demo

# 启动
mkdocs serve
# 指定监听的ip及端口
mkdocs serve --dev-addr 192.168.22.128:8083

# 编译 生成一个目录site存放静态文件
mkdocs build 
```

## 使用其他主题
[material](https://github.com/squidfunk/mkdocs-material)  
``` shell
pip install mkdocs-material

# mkdocs.yml
theme:
  name: material
  language: zh
  
```  
