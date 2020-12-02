#coding:utf8
#python>=3.6
#future是一个容器，或者占位符（placeholder），用于接受异步的结果

import asyncio
import random

async def slow_operation(future):
    x=int(random.random()*10)
    print('coroutin begin,will sleep %s' % x)
    await asyncio.sleep(x)
    future.set_result(x)       #指示future已结束，并设置返回值


if __name__=="__main__":
    loop = asyncio.get_event_loop()
    
    future1 = asyncio.Future()
    asyncio.ensure_future(slow_operation(future1)) # 使用ensure_future 创建Task
    
    future2 = asyncio.Future()
    asyncio.ensure_future(slow_operation(future2))
    
    # gather Tasks，并通过run_uniti_complete来启动、终止loop，在此开始执行任务
    loop.run_until_complete(asyncio.gather(future1, future2))
    #阻塞需要所有task执行结束
    
    #获取异步结果，即future.set_result的值
    print("get result by future %s" % future1.result())   
    print("get result by future %s" % future2.result())
    loop.close()
