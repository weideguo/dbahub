```
pip install pyinstaller

打包py文件成exe

#直接打包 
#生成build和dist目录，可执行文件位于dist目录下
#只需要保留dist目录？
pyinstaller demo.py


#高阶用法
#主要用于打包时同时复制静态资源文件
#生成demo.spec文件
pyi-makespec demo.py
#执行打包
pyinstaller demo.spec
```
