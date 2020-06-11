#使用django的admin模块

#settings.py

INSTALLED_APPS += ['django.contrib.admin']

#登陆验证使用的model
"""
#my_appp/models.py 
from django.contrib.auth.models import AbstractUser
my_appp/models.py 
class Users(AbstractUser):
    pass
"""

AUTH_USER_MODEL = "my_appp.Users"



#urls.py
#from django.conf.urls import url,include
from django.urls import include, path
from django.contrib import admin
#使用django自带的auth模块，进入该路径可以进行权限管理
urlpatterns += [path('admin/', admin.site.urls)]



#models.py
#默认每个模型都有add/change/delete/view权限，存储于django默认权限表 auth_permission
#add_logentry

#自定义权限
class MyPermission(models.Model):
    class Meta:
        managed = True
        #自定义权限
        permissions = (
            ('permission1', '自定义权限1'),
            ('permission2', '自定义权限2'),
            ('permission3', '自定义权限3'),


#通过管理页面对用户/组授权


#权限使用
#views.py
def view1(request):
    user=request.user
    
    #登陆验证
    user.is_authenticated
    user.is_superuser
    
    #权限鉴定
    user.has_perm('my_app.permission1')



from django.contrib.auth.decorators import permission_required
@permission_required('sql.permission2', raise_exception=True)
def view2(request):
    pass



#中间件
#settings.py
#MIDDLEWARE += "path_to_middleware.MyMiddleware"

from django.utils.deprecation import MiddlewareMixin

class MyMiddleware(MiddlewareMixin):
    
    #异常的处理
    def process_exception(self, request, exception):
        import traceback
        print(traceback.format_exc())
    
    
    #访问前的处理
    #比如用于登陆验证，没有登陆则跳转到登陆页面
    #@staticmethod
    #def process_request(request):
    def process_request(self, request):
        if not request.user.is_authenticated:
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect('/login/')
    
    
    #执行view函数前的处理，在process_request之后
    def process_view(self, request, view_func, view_args, view_kwargs):
        print("will run function for view")
    
    
    #响应时的处理，即为执行view函数后的处理（比如用于处理添加http头，如set-cookie）
    def process_response(self, request, response):
        
        return response
    
    
    