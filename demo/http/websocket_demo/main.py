#coding:utf8
import os
import json

from flask_socketio import SocketIO
from flask import Flask,request,render_template


app = Flask(__name__)
socket_io = SocketIO(app)

"""
websocket的测试
"""

@app.route("/listen", methods=['post', 'get'])
def listen_func():
    """"
    监听发送来的消息,并使用socketio向所有客户端发送消息
    """
    mes = {"message": "unknown error"}
    data = request.args['data'] if request.args.get('data') else request.form.get('data')
    if data is not None:
        import time
        time.sleep(3)
        #websocket的返回值
        # js的io_client.on绑定事件 "mes"
        socket_io.emit(data=data, event="mes")  
        mes['message'] = "success"
    else:
        pass
    
    #普通返回值
    return json.dumps(mes)


#与js的io_client.emit 请求的路径一致
@socket_io.on("login")
def quotations_func(mes):
    """
    接收websocket主动请求
    """
    sid = request.sid  # io客户端的sid, socketio用此唯一标识客户端.
    host = request.host
    print(mes,sid,host)
    #mes为主动请求为js的 io_client.emit 提交的值
    socket_io.emit(event="login", data=json.dumps({"message": "you are connect"}))


@app.route("/")
def test_func():
    """
    测试页面
    web前端会自动循环向后端发起请求
    位于templates目录下
    """
    return render_template("test.html")


if __name__ == '__main__':
    socket_io.run(app=app, host="0.0.0.0", port=9002, debug=True)
