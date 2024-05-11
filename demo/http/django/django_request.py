from django.http.request import QueryDict


q = QueryDict('a=1&a=2&c=3')
q.urlencode(safe=None)

q.getlist('a') 



# HttpRequest对象
from django.http.request import HttpRequest


request.GET
# 类似于字典的对象，url路径中?后提交的数据


# http请求body的数据
request.body
# 返回的是一个字符串
# 可以使用方法读数据代替
# request.read() 
# request.readline()
# curl -T "file1" $http_url           # 单个文件
# curl -T "{file1,file2}" $http_url   # 多个文件

request.data
# 返回的是一个字典对象

request.POST
# 类似于字典的对象 QueryDict


request.FILES
# 类似于字典的对象
# FILES 中的每个键为<input type="file" name="" /> 中的name，值则为对应的文件对象
# 只有在请求的方法为POST 且提交的<form>带有 enctype="multipart/form-data"的情况下才会包含数据
# curl -F "file=@/root/xxx.sh" $http_url