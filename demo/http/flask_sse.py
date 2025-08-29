# 
# Server-Sent Events
# 实现由后端推送消息给web前端

from flask import Flask, Response, request
import time
import json
import random

app = Flask(__name__)

def generate_sse_events():
    """生成 SSE 事件流"""
    #while True:
    for i in range(10):
        data = {
            "timestamp": int(time.time()),
            "value": random.randint(1, 100),
            "message": "Hello from server!"
        }
        
        # 格式: data: {json}\n\n
        # data是关键字，格式要固定
        yield f"data: {json.dumps(data)}\n\n"
        
        time.sleep(1)
    
    # 服务器关闭sse，推荐由客户端主动关闭
    return 
       

@app.route("/sse")
def sse():
    # 返回响应，MIME 类型为 text/event-stream
    # Content-Type: text/event-stream
    return Response(
        generate_sse_events(),
        mimetype="text/event-stream"
    )


@app.route("/")
def index():
    return """
    <h1>SSE 实时数据接收</h1>
    <button onclick="closeSSE()">关闭SSE连接</button>
    <div id="output"></div>
    
    <script>
      const eventSource = new EventSource("/sse");
      
      function closeSSE() {
        eventSource.close()
      }
      
      const output = document.getElementById("output");
      eventSource.onmessage = function(event) {
        console.log(event.data);           //
        
        const data = JSON.parse(event.data);
        const div = document.createElement("div");
        div.textContent = `[${new Date().toLocaleTimeString()}] ---- ${data.value}  ${data.message}`;
        output.appendChild(div);
      };
      
      eventSource.onerror = function(err) {
        console.error("SSE error:", err);
        eventSource.close();                 // 出现断开则不再重连，没有这个则服务端断开后web客户端会重新发起连接
      };
      
      eventSource.addEventListener("close", () => {
        console.log("SSE 连接已关闭");
      });
    </script>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)