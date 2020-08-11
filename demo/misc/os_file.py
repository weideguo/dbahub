# -*- coding: UTF-8 -*-

import os, sys

fd = os.open( "foo.txt", os.O_RDWR|os.O_CREAT )


os.write(fd, "This is test")

#
fd2 = 1000
os.dup2(fd, fd2);

#
os.lseek(fd2, 0, 0)
str = os.read(fd2, 100)
print(str)

os.close( fd )


#列出目录下匹配的文件名
import glob
glob.glob("/tmp/python*")



