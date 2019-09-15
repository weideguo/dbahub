#--encoding=utf-8
import cgi

html='''
<html>
<title>hello</title>
<body>
<p>
hello,world!
</p>
</body>
</html>
'''
#form=cgi.FieldStorage()
#who=form['person'].value    #url http://127.0.0.1:8000/cgi_demo.py?person=weideguo

print html

"""
WSGI
web server gateway interface

CGI
common gateway interface


#基于当前目录创建web服务
python -m CGIHTTPServer 
"""






