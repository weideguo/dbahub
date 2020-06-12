#django admin 页面


#认证和授权/AUTHENTICATION AND AUTHORIZATION
#可以对 group/组 授权，权限来自于 自定义权限 以及 model自带权限



#admin.py 设置后可以在django admin 页面管理对应的model
from django.contrib import admin
from .models import MyTable

@admin.register(MyTable)
class MyTableAdmin(admin.ModelAdmin):
    '''
    model在django admin的管理设置
    '''
    list_display = ('field1','field2')
    search_fields=()          #使用搜索框搜索的字段
    list_display_links=()     #存在链接的字段
    ordering=()               #排序的字段
    inlines=()                #管理的其他model，查询时交联查询
    list_filter=()            #右边栏快速过滤器


#user/group等django auth模块的model 可以通过重载UserAdmin实现管理
from django.contrib.auth.admin import UserAdmin
@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    ...


#models.py
class MyTable(models.Model):
    ...
    
    class Meta:
        verbose_name = 'MyTable'
        verbose_name_plural = 'MyTable'          #在管理页面显示的名字





