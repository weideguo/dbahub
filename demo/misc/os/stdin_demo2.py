#python3

import sys
import argparse


def _argparse():
    _parser = argparse.ArgumentParser(add_help=True, description="argparse如何使用样例，使用--help查看")
    _parser.add_argument("--file", "-f" , type=argparse.FileType("r"), default=sys.stdin, dest="FILE",  help="mysqldump stream")
    return _parser.parse_args()
    
__parser = _argparse()
f = __parser.FILE 


while True:
    data = f.readline()
    if data == "": #EOF
        break
    print("--%s++++" % data)  # 读取的数据带有换行符



"""
echo -e "111\n222\n\n333" | ./stdin_demo2.py
./stdin_demo2.py -f some_file.txt
"""


