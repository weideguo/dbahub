# 使用cpp实现python的扩展

``` shell
# install 安装到python扩展使用的目录
python3 setup.py install 
# build 只是在编译到当前目录
python3 setup.py build
```

``` python
# useage
from extenddemo import maths
maths.plus_one(1)
```
