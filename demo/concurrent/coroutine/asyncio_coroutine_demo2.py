#coding:utf8
#python >= 3.6

#yield from 获取子生成器返回值

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    #yield from writer.drain()
    '''
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':   #http返回值头部结束标识
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    '''
    all=yield from reader.read()
    print(all)
    
    writer.close()


if __name__=="__main__":
    tasks = [wget(host) for host in ['www.google.com', 'www.baidu.com']]
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()






