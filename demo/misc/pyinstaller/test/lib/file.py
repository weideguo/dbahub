#coding:utf8
import os
import sys

def read(filename):
    if not os.path.isfile(filename):
        print("file not exit")
        sys.exit(-1)
    
    with open(filename) as f:
        l=f.readline()
        while l:
            print(l)
            l=f.readline()
