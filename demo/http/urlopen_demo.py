#!/usr/bin/python
#--encoding=utf8
import urllib2
import urllib

#http://xxxx/post/getdata_db.php?db_type=3454624&db_project=12345
url="http://xxxx/post/getdata_db.php"
db_type="3454624"
db_project="12345"
	 
postdata=dict(db_type=db_type,db_project=db_project)
postdata_dict=urllib.urlencode(postdata)
request = urllib2.Request(url,postdata_dict)
response=urllib2.urlopen(request)
res = response.read()


#download
from urllib import urlopen

f=open('/data/Demo2.zip','wb')            	  
u=urlopen('https://github.com/rest-client/rest-client/archive/master.zip')
f.write(u.read())
f.close()


# 关闭https证书检查
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


