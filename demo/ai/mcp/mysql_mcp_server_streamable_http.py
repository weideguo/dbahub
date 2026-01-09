from mysql_mcp_server import get_db_config,logger
from mysql_mcp_server import app
# app 为 mcp.server.Server 的实例

import sys
import contextlib
from collections.abc import AsyncIterator

from mcp.server.streamable_http_manager import StreamableHTTPSessionManager

from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.types import Receive, Scope, Send


def main():
    print("Starting MySQL MCP server with config:", file=sys.stderr)
    config = get_db_config()
    print(f"Host: {config['host']}", file=sys.stderr)
    print(f"Port: {config['port']}", file=sys.stderr)
    print(f"User: {config['user']}", file=sys.stderr)
    print(f"Database: {config['database']}", file=sys.stderr)

    logger.info("Starting MySQL MCP server...")
    logger.info(f"Database config: {config['host']}/{config['database']} as {config['user']}")

    return mcp_server_to_streamable_http_server(app,logger)


def mcp_server_to_streamable_http_server(app,logger):
    """
    由 mcp.server.Server 的实例运行 streamable-http 模式的web服务
    """
    session_manager = StreamableHTTPSessionManager(app=app,event_store=None,json_response=False,stateless=True)

    # ASGI handler for streamable HTTP connections
    async def handle_streamable_http(scope: Scope, receive: Receive, send: Send) -> None:
        await session_manager.handle_request(scope, receive, send)

    @contextlib.asynccontextmanager
    async def lifespan(app: Starlette) -> AsyncIterator[None]:
        """Context manager for managing session manager lifecycle."""
        async with session_manager.run():
            logger.info("Application started with StreamableHTTP session manager!")
            try:
                yield
            finally:
                logger.info("Application shutting down...")

    # Create an ASGI application using the transport
    starlette_app = Starlette(
        debug=True,
        routes=[
            Mount("/mcp", app=handle_streamable_http),
        ],
        lifespan=lifespan,
    )
    return starlette_app


starlette_app = main()

if __name__ == "__main__":    
    import uvicorn
    uvicorn.run(starlette_app, host="0.0.0.0", port=8000)

"""
uvicorn mysql_mcp_server_streamable_http:starlette_app --reload --host 0.0.0.0 --port 8000
或者
python mysql_mcp_server_streamable_http.py
"""
