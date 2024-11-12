#!/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import hiredis

d = {}

class MSG:
    OK = b"+OK\r\n"
    ERROR = b"-ERROR\r\n"
    
    @staticmethod
    def normal_response(raw_msg):
        if raw_msg is None:
            return b"$-1\r\n"
        else:
            msg_len = len(raw_msg)
            return f"${msg_len}\r\n".encode("utf-8")+raw_msg+b"\r\n"


def process(req):
    print(req)
    cmd = req[0].lower()
    if cmd == b"set":
        d[req[1]] = req[2]
        return MSG.OK
    elif cmd == b"get":
        v = d.get(req[1])
        return MSG.normal_response(v)
    else:
        return MSG.ERROR

class RedisServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.hireader = hiredis.Reader()

    def data_received(self, data):
        self.hireader.feed(data)
        while True:
            req = self.hireader.gets()
            if not req:
                break
            res = process(req)
            self.transport.write(res)

async def main():
    loop = asyncio.get_running_loop()
    server = await loop.create_server(lambda: RedisServerProtocol(), "0.0.0.0", 5003)
    print("serving on {}".format(server.sockets[0].getsockname()))
    async with server:
        await server.serve_forever()

try:
    import uvloop
    uvloop.install()
    # 替换原本asyncio中的默认事件循环，更高性能
except ImportError:
    print("uvloop is not available")

asyncio.run(main())
