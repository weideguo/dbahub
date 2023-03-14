import os
import re
from setuptools import setup,Extension

setup(name='extend-demo',
      version="0.0.1",
      description='extend demo in cpp',
      author="weideguo",
      author_email="weideguo93@foxmail.com",
      maintainer='weideguo',
      maintainer_email='weideguo93@foxmail.com',
      python_requires='==3.7.*',
      ext_modules = [Extension('extenddemo/maths',["src/maths.cpp"])],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3.7']
      )