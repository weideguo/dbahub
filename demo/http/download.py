#!/bin/env python
#--encoding=utf-8
from urllib import urlopen

f=open('/data/Demo2.zip','wb')            	  
u=urlopen('https://github.com/rest-client/rest-client/archive/master.zip')
f.write(u.read())
f.close()
