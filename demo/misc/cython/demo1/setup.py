from distutils.core import setup
from Cython.Build import cythonize

setup(name='Hello World app',
     ext_modules=cythonize('hello.py'))


#编译为 .c，再进一步编译为 .so
#python setup.py build_ext --inplace

#使用编译后的.so 文件当成模块进行import
#from hello import hello
