#通过dll调用windows的函数

from ctypes import *  
#默认在C:\Windows\System32目录下 可以指定完整目录
user32 = windll.LoadLibrary('user32.dll')  
user32.MessageBoxA(0,'this is content','this is title',0) 
