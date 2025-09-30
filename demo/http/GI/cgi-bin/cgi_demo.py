#!/usr/bin/env python2
# -*- coding: utf-8 -*-


html = """
<html>
<title>hello</title>
<body>
<p>
hello,world!
</p>
</body>
</html>
"""
#import cgi
#form = cgi.FieldStorage()
#who = form["person"].value    

print(html)

"""
# 基于当前目录创建web服务，cgi文件应该在当前目录的cgi-bin目录下，为Unix格式
# 即这个.py文件应该在cgi-bin目录下
python -m CGIHTTPServer 
python -m CGIHTTPServer 8000

# curl http://127.0.0.1:8000/cgi-bin/cgi_demo.py?person=weideguo
"""