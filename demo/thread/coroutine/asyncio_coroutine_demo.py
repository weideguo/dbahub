#coding:utf8
#python >= 3.6
#协程函数（async def 或者 @asyncio.coroutine）
#协程函数所返回的协程对象


import asyncio
import requests_async as requests


@asyncio.coroutine
def wget(host):
    response=yield from requests.get(host)
    print(response.status_code)
    print(response.text)
    
    
if __name__=="__main__":
    #loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['http://www.google.com', 'http://www.baidu.com']]
    
    #异步执行 被卡住的task不会阻塞另外的task
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    #阻塞至所有task执行结束
    
    loop.close()