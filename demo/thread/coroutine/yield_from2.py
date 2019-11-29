#python >= 3.3

#协程函数（async def 或者 @asyncio.coroutine）
#协程函数所返回的协程对象



import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.google.com', 'www.baidu.com']]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()



######################################################################


import asyncio
import requests_async as requests


@asyncio.coroutine
def wget(host):
    response=yield from requests.get(host)
    print(response.status_code)
    print(response.text)
    
    

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['http://www.google.com', 'http://www.baidu.com']]

loop.run_until_complete(asyncio.wait(tasks))
loop.close()


