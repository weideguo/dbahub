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
