#coding:utf8
import asyncio

from aiohttp import web
from aiohttp.web import Response

async def index(request):
    await asyncio.sleep(0.5)
    return Response(body=b'<h1>Index</h1>')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return Response(body=text.encode('utf-8'))


#async def init(loop):
#    app = web.Application(loop=loop)
#    app.router.add_route('GET', '/', index)
#    app.router.add_route('GET', '/hello/{name}', hello)
#    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8001)
#    print('Server started at http://127.0.0.1:8001...')
#    return srv
#
#loop = asyncio.get_event_loop()
#loop.run_until_complete(init(loop))
#loop.run_forever()



app = web.Application()
app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/hello/{name}', hello)
web.run_app(app,host='127.0.0.1', port=8001)


