#python >= 3.6
#基于协程的异步web服务

from sanic import Sanic
from sanic.response import json
import asyncio

app = Sanic()

@app.route("/")
async def test(request):
    #import time
    await asyncio.sleep(5)
    return json({"hello": "world"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9091)

