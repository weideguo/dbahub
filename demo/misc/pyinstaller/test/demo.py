#coding:utf8

import os
import sys
from lib import file as myfile

filename="data/my.txt"
if len(sys.argv)>=2:
    filename=sys.argv[1]

myfile.read(filename)

print("-------------------------------------")
print("read file done")