#!/bin/env python
# -*- coding: utf-8 -*-
# 通过标准输入获取`docker inspect $container_id_or_name`信息，进行使用runlike进行解析
# 需要预先安装runlike模块 `pip install runlike`
from json import loads
from runlike.inspector import Inspector

class  InspectorCli(Inspector):
    def __init__(self, inspect_str):
        self.inspect_str = inspect_str
        container = ""
        no_name = True
        pretty = True
        super(InspectorCli, self).__init__(container, no_name, pretty) 
    
    def inspect(self):
        try:        
            _inspect_str = self.inspect_str.decode("utf8")
            # python2，str类型为二进制格式，需要转成unicode
        except:
            _inspect_str = self.inspect_str
            # python3, str类型为unicode，无需转换
            pass
        # runlike==0.7.0
        self.facts = loads(_inspect_str)
        # runlike==1.4.14
        self.container_facts = self.facts


import sys
import argparse

if __name__ == "__main__":
    def _argparse():
        _parser = argparse.ArgumentParser(add_help=True, description="解析`docker inspect $container_id`的输出，使用--help查看")
        _parser.add_argument("--file", "-f" , type=argparse.FileType("r"), default=sys.stdin, dest="FILE",  help="`docker inspect $container_id_or_name` 的输出可以以文件或者标准输入传入")
        return _parser.parse_args()
    
    __parser = _argparse()
    f = __parser.FILE 

    inspect_str = ""
    while True:
        data = f.readline()
        if data == "": #EOF
            break

        inspect_str = inspect_str + data
    
    
    ins = InspectorCli(inspect_str)
    ins.inspect()
    print(ins.format_cli())

"""
cat $docker_inspect_output | ./runlike_cli.py
./runlike_cli.py -f $docker_inspect_output

# runlike==1.4.14 也已经支持标准输入
cat $docker_inspect_output | python3 /usr/bin/runlike -s -p
"""
