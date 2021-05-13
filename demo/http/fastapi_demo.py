#coding:utf8
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """
    这是注释
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/items1/{item_id}")
def read_item1(item_id):
    """
    没有类型注解写法也是支持
    """
    return {"item_id": item_id}   
   
 
@app.get("/items2/")
def read_item2(q: Optional[str], q1: Optional[str] = None):
    """
    参数没有初始值则表示要强制在调用时设置值，有初始值则则不强制
    """
    return {"q": q,"q1": q1} 
   

@app.get("/test")
async def read_root2():
    """
    异步写法
    """
    return {"Hello": "World" } 
   
"""
Python 3.6+.

启动
uvicorn fastapi_demo:app --reload  --host 192.168.253.128  --port 8001


内部路径 不要占用这些路径
/docs      #api文档说明 Swagger
/redoc     #另一文档格式


"""

