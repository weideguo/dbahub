#django 国际化设置

#settings.py                     #配置文件中设置
# Internationalization
LANGUAGE_CODE = 'zh-Hans'        #确定使用哪个语言包

USE_I18N = True

LOCALE_PATHS=["locale"]         #如果使用全局目录，需要设置路径

##################################################
#由此确认名字 $site-packages/django/conf/locale/
#创建.po文件    需要在项目全局创建目录 locale ，或者在app的目录下创建
python manage.py makemessages -l zh_Hans   #语言包名要使用中下划线代替中划线，但settings.py需要使用中划线？
python manage.py makemessages -l en

python manage.py compilemessages           #修改.po文件后需要运行

##################################################
#实际代码的需要翻译的参数

from django.utils.translation import gettext as _

_('what you want to translate')            






#########################################################################################################
#动态切换需要额外增加以下设置

# settings.py
MIDDLEWARE_CLASSES += [
    'django.contrib.sessions.middleware.SessionMiddleware',       #可能需要用session
    'django.middleware.locale.LocaleMiddleware',                  #需要确定顺序
    'django.middleware.common.CommonMiddleware',
]



LANGUAGES = ( 
   ('en', 'English'), 
   ('zh-CN', '中文'), 
) 


#urls.py
urlpatterns += [ path(r'^i18n/',include('django.conf.urls.i18n')) ]




# 语言选择优先级
i18n_patterns                                         # urls.py 中设置，如 path('<slug:slug>/', news_views.details, name='detail')
request.session[settings.LANGUAGE_SESSION_KEY]        # 通过前端向 /i18n/setlang post {'language':'zh-Hans'} 设置语言选项 或 后端设置session实现语言设置 request.session['_language']='zh-Hans'
request.COOKIES[settings.LANGUAGE_COOKIE_NAME]        # settings.LANGUAGE_COOKIE_NAME 前端设置这个cookie的值
request.META['HTTP_ACCEPT_LANGUAGE']                  # HTTP 请求中的header  "Accept-Language: zh-CN"   #只需要匹配“-”之前的字符？
settings.LANGUAGE_CODE                                #




