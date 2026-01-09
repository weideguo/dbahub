
from mysql_mcp_server import get_db_config,logger
from mysql_mcp_server import app
# app 为 mcp.server.Server 的实例

import sys

from mcp.server.sse import SseServerTransport

from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.responses import Response
from starlette.requests import Request


def main():
    print("Starting MySQL MCP server with config:", file=sys.stderr)
    config = get_db_config()
    print(f"Host: {config['host']}", file=sys.stderr)
    print(f"Port: {config['port']}", file=sys.stderr)
    print(f"User: {config['user']}", file=sys.stderr)
    print(f"Database: {config['database']}", file=sys.stderr)

    logger.info("Starting MySQL MCP server...")
    logger.info(f"Database config: {config['host']}/{config['database']} as {config['user']}")

    return mcp_server_to_sse_server(app)


def mcp_server_to_sse_server(app):
    """
    由 mcp.server.Server 的实例运行 sse 模式的web服务
    """
    sse = SseServerTransport("/messages/")
    async def handle_sse(request: Request):
        async with sse.connect_sse(request.scope, request.receive, request._send) as streams:  
            await app.run(streams[0], streams[1], app.create_initialization_options())
        return Response()
    
    starlette_app = Starlette(
        debug=True,
        routes=[ 
            Route("/sse", endpoint=handle_sse, methods=["GET"]),
            Mount("/messages/", app=sse.handle_post_message),
        ],
    )
    return starlette_app

    
starlette_app = main()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(starlette_app, host="0.0.0.0", port=8000)

"""
uvicorn mysql_mcp_server_sse:starlette_app --reload --host 0.0.0.0 --port 8000
或者
python mysql_mcp_server_sse.py
"""