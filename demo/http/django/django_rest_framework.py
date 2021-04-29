rest_framework 通过请求时

#使用该类返回
from rest_framework.response import Response

curl "http://127.0.0.1" -H "accept: text/html"          #返回rest framework的web调试页面

curl "http://127.0.0.1" -H "accept: application/json"   #返回json格式数据

