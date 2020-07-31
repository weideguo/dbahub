#国际化



# -*- coding: utf-8 -*- 
import gettext
locale_path = './locale/'
zh_trans = gettext.translation('internation', locale_path, languages=['zh_CN'])
en_trans = gettext.translation('internation', locale_path, languages=['en_US'])
 
print("----中文版本----")
zh_trans.install()  # 这条语句会将_()函数自动放到python的内置命名空间中
print( _("Hello world!"))
print( _("Python is a good Language.")
 
print( "----英文版本----")
en_trans.install()
print( _("Hello world!"))
print( _("Python is a good Language."))


"""
#显式引入
#翻译时转换成unicode
_ = t.gettext

#翻译时不转换，为byte
_ = t.lgettext
"""


##################################################################
"""
#查看当前语言环境
locale
export LC_ALL="en_US"
export LC_ALL="zh_CN"
"""

# -*- coding: utf-8 -*-
import gettext
locale_path = './locale/'
# 将域APP_NAME与LOCALE_PATH目录绑定，
# 这样gettext函数会在LOCALE_PATH目录下搜索对应语言的二进制APP_NAME.mo文件
gettext.bindtextdomain('internation', locale_path)
# 声明使用现在的域，可以使用多个域，便可以为同一种语言提供多套翻译
gettext.textdomain('internation')
_ = gettext.gettext
 
print(_("Hello world!"))
print( _("Python is a good Language.") )




##################################################################
"""
#根据关键字从源码提取需要翻译的字符串
xgettext -k_ -o internation.po_en internation.py
xgettext -k_ -o internation.po_zh internation.py


#修改文本翻译文件


#生成二进制翻译文件，源码从此读取翻译信息 
#文件目录结构需要严格限定
msgfmt -o ./locale/en_US/LC_MESSAGES/internation.mo internation.po_en
msgfmt -o ./locale/zh_CN/LC_MESSAGES/internation.mo internation.po_zh
"""

