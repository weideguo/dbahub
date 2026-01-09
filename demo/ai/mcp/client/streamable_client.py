import asyncio

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client


async def main():
    async with streamablehttp_client("http://10.30.20.76:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            # 列出所有的tool
            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")


if __name__ == "__main__":
    asyncio.run(main())