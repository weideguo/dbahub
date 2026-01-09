import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

#"../demo/mcp_stdio.py"
server_params = StdioServerParameters(
    command="python", 
    args=[
        "../mysql_mcp_server.py"
    ],
    env=None
)
 
async def run():
    # 只能通过异步方式调用
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print(f"Available tools: {[tool.name for tool in tools.tools]}")
 
            # call a tool
            #r = await session.call_tool(name="add",arguments={"x": 1,"y": 2})
            #print("resultx: ", r.content)
            #print("result: ", r.structuredContent["result"])
            # from mcp.types import CallToolResult #   # 返回类型

if __name__ == "__main__":
    asyncio.run(run())
