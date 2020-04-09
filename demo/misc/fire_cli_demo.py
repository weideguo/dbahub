#!/bin/env python
#coding:utf8

import fire

class MyCMD(object):
    """put some description at here"""

    def f1(self, number):
        """function description for f1"""
        return 2 * number
        
    def f2(self, number):
        """function description for f2"""
        return 3 * number

if __name__ == '__main__':
    fire.Fire(MyCMD)
  
  
"""
#命令行界面
#不支持中文？
fire_cli_demo.py 
fire_cli_demo.py --help   #查看帮助
"""