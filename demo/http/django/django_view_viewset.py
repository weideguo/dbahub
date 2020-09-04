#view

#from django.views.generic.base import View    #django原生view类
from rest_framework.views import APIView
"""
以下方法直接对应http的方法
get 
post
put
delete
"""

class YourView(APIView):
    def get(self, request, args = None): 
        return ...
    def post(self, request, args = None):
        return ...
    def put(self, request, args = None):
        return ...
    def delete(self, request, args = None):
        return ...

#路由设置
#urls.py
from django.conf.urls import url
urlpatterns +=[ url(r'^url_in_browser/(.*)', YourView.as_view(), name='your_view_name')]





#viewset
from rest_framework import viewsets

viewsets.ViewSet
viewsets.GenericViewSet
viewsets.ReadOnlyModelViewSet
viewsets.ModelViewSet

#直接设置url的定向
YourView = YourViewSet.as_view({
    'get': 'func1',
    'put': 'func2',
    'patch': 'func3',    #http中用于局部更新，类似于put
    'delete': 'func4',
    'post': 'func5'
})


#具体方法加装饰器
from rest_framework.decorators import detail_route
class YourViewSet():
    @detail_route(methods=['post'], permission_classes=[])
    def func0(self, request, *args, **kwargs):
        return ...


"""
ModelViewSet 的方法默认对应http方法
create            >  post
update            >  put
partial_update    >  patch
destroy           >  delete
list              >  get     #不能与retrieve同时存在？
retrieve          >  get     #
"""
#路由设置
#urls.py
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'url_in_browser', YourViewset, base_name='you_viewset_name')

urlpatterns += [ url(r'^', include(router.urls))]






#mixin 公共方法的类用于view类/viewset类继承  

from rest_framework import mixins

mixins.CreateModelMixin          #
mixins.ListModelMixin            #
mixins.RetrieveModelMixin        #
mixins.UpdateModelMixin          #
mixins.DestroyModelMixin         #


