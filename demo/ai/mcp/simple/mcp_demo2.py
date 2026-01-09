from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MCP Server",host="0.0.0.0",port=8000)


@mcp.tool(
    name="add",
    description="对两个数字进行实数域的加法"
)
def add(a: int, b: int) -> int:
    return a + b

@mcp.resource(
    uri="greeting://{name}",
    name="greeting",
    description="用于演示的一个资源协议"
)
def get_greeting(name: str) -> str:
    # 访问处理 greeting://{name} 资源访问协议，然后返回
    return f"Hello, {name}!"

@mcp.prompt(
    name="translate",
    description="进行翻译的prompt"
)
def translate(message: str) -> str:
    return f"请将下面的话语翻译成中文：\n\n{message}"


if __name__ == "__main__":
    # mcp.run() 
    #mcp.run(transport="sse")              # http://${host}:${port}/sse
    mcp.run(transport="streamable-http")   # http://${host}:${port}/mcp

"""
sse、streamable-http时
python mcp_demo2.py

为stdio模式时，无需预先启动，由客户端直接运行
"""
