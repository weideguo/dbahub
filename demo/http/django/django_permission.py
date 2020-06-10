'''
class BasePermission(object):
    """
    A base class from which all permission classes should inherit.
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True
'''     
from rest_framework.permissions import BasePermission
#自定义权限   
class IsHandleAble(BasePermission):
    #权限
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True
        
    
    #对对象的权限 
    #obj 由view的 serializer_class 确定与数据库表的orm映射关系
    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        return True

    
   
#django rest的账号认证权限
#sttings.py REST_FRAMEWORK/DEFAULT_AUTHENTICATION_CLASSES 设置使用的验证方法
from rest_framework.permissions import IsAuthenticated


#view
from rest_framework.views import APIView
class MyTest(APIView):
    permission_classes = [IsAuthenticated, IsHandleAble]
    
    ...
