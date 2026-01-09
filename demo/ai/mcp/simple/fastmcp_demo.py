import uuid
import platform
import psutil
import socket

from fastmcp import FastMCP

mcp = FastMCP(name="SystemMonitor")

@mcp.tool
def get_os_info() -> dict:
    """获取操作系统信息"""
    return {
        "system": platform.system(),
        "version": platform.version(),
        "release": platform.release(),
        "machine": platform.machine()
    }

@mcp.tool
def get_disk_usage(path: str = "/") -> dict:
    """获取磁盘使用情况（默认根目录）"""
    usage = psutil.disk_usage(path)
    return {
        "total_GB": round(usage.total / (1024**3), 2),
        "used_GB": round(usage.used / (1024**3), 2),
        "free_GB": round(usage.free / (1024**3), 2),
        "usage_percent": usage.percent
    }

@mcp.tool
def get_hardware_info() -> dict:
    """获取硬件配置"""
    return {
        "cpu_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(),
        "memory_GB": round(psutil.virtual_memory().total / (1024**3), 2),
        "hostname": socket.gethostname()
    }

@mcp.tool
def get_network_info() -> dict:
    """获取网络信息"""
    return {
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "mac_address": ":".join(["{:02x}".format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])
    }



if __name__ == "__main__":
    #
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000, log_level="DEBUG")

    """
    transport ("stdio", "sse", "streamable-http")
    http://10.30.20.76:8000/sse   sse
    http://10.30.20.76:8000/mcp   streamable-http 
    """

"""
python fastmcp_demo.py
"""
