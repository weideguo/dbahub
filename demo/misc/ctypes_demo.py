#python调用动态连接库

#windows#########################################################################################
from ctypes import *

#两总引入方式均可以              
libc = windll.msvcrt
libc.time()

libc = cdll.msvcrt               
libc.time()                      

#windows动态来链接库
#位于windows的动态连接库的路径下 C:\Windows\System32 
#kernel32.dll 内存管理、数据的输入输出操作和中断处理
#msvcrt.dll   printf,malloc,strcpy等C语言库函数的具体运行实现



#linux#########################################################################################
from ctypes import *
        
#两种引入方式        
libc = cdll.LoadLibrary("libc.so.6")  
libc.time(None)       
     
libc = CDLL('libc.so.6')         
libc.time(None)                  

#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/paht_2_so    #指定使用动态连接库的路径


