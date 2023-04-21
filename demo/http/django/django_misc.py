from django.http.request import QueryDict


q = QueryDict('a=1&a=2&c=3')
q.urlencode(safe=None)

q.getlist('a') 

