#coding:utf8
#!/bin/env python3
import io
import sys

#整体设置输出的编码，因此不必每次输出都进行编码转换
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")    
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gbk")
print("中文")
