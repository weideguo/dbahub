#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#python >= 3.6
# async/await的使用 为协程的语法糖


import threading
import asyncio
import time 
import requests_async as requests



async def wget(url):
    #print('Hello world! (%s) %s %s' % (threading.currentThread(),url,str(time.time())))
    #await asyncio.sleep(10)
    response = await requests.get(url)    #await需要在async函数内？
    print(response.status_code)
    print(response.text)
    #print('Hello again! (%s) %s %s' % (threading.currentThread(),url,str(time.time())))

if __name__ == "__main__":

    #loop = asyncio.get_event_loop()
    #tasks = [wget('https://www.google.com'), wget('https://www.baidu.com')]
    tasks = [wget(x) for x in ['https://www.google.com','https://www.baidu.com']]
    
    #异步执行 被卡住的task不会阻塞另外的task
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    #阻塞至所有task执行结束
    print("all done")
    loop.close()
 
