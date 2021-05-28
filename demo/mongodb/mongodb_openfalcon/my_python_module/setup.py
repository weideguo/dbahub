from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello World app',
     ext_modules=cythonize('mongodb_util.py'))


#python setup.py build_ext --inplace   #编译成.so文件
