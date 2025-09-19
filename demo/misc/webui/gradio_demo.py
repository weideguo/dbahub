"""
一个演示页面
python app.py
"""

import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch(server_name="0.0.0.0")  

"""
fn        处理输出的函数
inputs    控制输入的样式 可以为字符串、列表  列表的个数应该与函数的输入参数个数相同
outputs   控制输出的样式 可以为字符串、列表  列表的个数应该与函数的返回参数个数相同
"""

