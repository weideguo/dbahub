#future是一个容器，或者占位符（placeholder），用于接受异步的结果

import asyncio

async def slow_operation(future):
    await asyncio.sleep(10)
    future.set_result('Future is done!')       #指示future已结束，并设置返回值


loop = asyncio.get_event_loop()

future1 = asyncio.Future()
asyncio.ensure_future(slow_operation(future1)) # 使用ensure_future 创建Task

future2 = asyncio.Future()
asyncio.ensure_future(slow_operation(future2))

# gather Tasks，并通过run_uniti_complete来启动、终止loop，在此开始执行任务
loop.run_until_complete(asyncio.gather(future1, future2))

print(future1.result())   #获取异步结果，即future.set_result的值
print(future2.result())
loop.close()
