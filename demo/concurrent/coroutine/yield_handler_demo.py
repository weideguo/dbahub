#coding:utf8

import time 
 
def message_handler():
    message_value = ''
    while True:
        message = yield message_value  
        time.sleep(1)
        print(message+" do something here")
        message_value = message+" done"
        
        
#创建一个生成器
handler=message_handler()

#启动生成器
handler.next()

while True:
    #发送数据给生成器 并阻塞到获取结果
    #yeild xxx 类似于 return xxx
    r=handler.send("aaa")   
    
    
    