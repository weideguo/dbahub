#通过dll调用windows的函数

from ctypes import *  
user32 = windll.LoadLibrary('user32.dll')  
user32.MessageBoxA(0,'this is content','this is title',0) 
