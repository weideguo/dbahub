# streamable_http_flask.py
from flask import Flask, Response
import time
import json
import random

app = Flask(__name__)

def generate_stream():
    """生成流式数据"""
    for i in range(10):
        data = {
            "timestamp": int(time.time()),
            "value": random.randint(1, 100),
            "message": "Hello from server!"
        }
        
        # 格式并不固定，为字符串即可
        yield f"服务端发送的streamble数据: {json.dumps(data)}\n"
        
        time.sleep(1)

    # 无需显示结束
    

@app.route("/stream")
def stream():
    return Response(
        generate_stream(),
        mimetype="text/plain" 
    )


@app.route("/")
def index():
    return """
    <h1>流式HTTP客户端</h1>
    <button onclick="closeFetchStream()">关闭流式HTTP</button>
    <div id="output"></div>
    <script>
        let controller = null;
        // 必须要异步实现流式读取
        async function fetchStream(url) {
            const response = await fetch(url,{signal: (controller = new AbortController()).signal}); 
            const reader = response.body.getReader();
            const decoder = new TextDecoder();
            while (true) {
                const {done, value} = await reader.read(); 
                if (done) break;
                
                const data = decoder.decode(value, { stream: true })
                console.log(data);
                
                const div = document.createElement("div");
                div.textContent = `[${new Date().toLocaleTimeString()}] ---- ${data}`;
                output.appendChild(div);
            }
        }
    
        fetchStream("/stream");
        
        function closeFetchStream () {
            controller.abort();
            console.log("流式HTTP已经关闭");
        }
    </script>
"""
   
    
"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>流式HTTP客户端</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .container {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        textarea, button, pre {
            width: 100%;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
            padding: 8px;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
        pre {
            border: 1px solid #ddd;
            padding: 10px;
            min-height: 200px;
            background-color: #f5f5f5;
            overflow-y: auto;
            white-space: pre-wrap;
        }
        .status {
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>流式HTTP客户端</h1>
        
        <div>
            <label for="url">请求URL:</label>
            <!--textarea id="url" placeholder="输入流式HTTP端点URL">http://192.168.85.128:5000/stream</textarea-->
            <textarea id="url" placeholder="输入流式HTTP端点URL">/stream</textarea>
        </div>
        
        <button id="fetchBtn">获取流式数据</button>
        <button id="cancelBtn" disabled>取消请求</button>
        
        <div class="status">状态: <span id="status">准备就绪</span></div>
        
        <div>
            <label>接收到的数据:</label>
            <pre id="output"></pre>
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const urlInput = document.getElementById("url");
            const fetchBtn = document.getElementById("fetchBtn");
            const cancelBtn = document.getElementById("cancelBtn");
            const statusSpan = document.getElementById("status");
            const outputPre = document.getElementById("output");
            
            let controller = null;
            
            // 获取流式数据
            fetchBtn.addEventListener("click", async () => {
                const url = urlInput.value.trim();
                if (!url) {
                    alert("请输入有效的URL");
                    return;
                }
                
                fetchBtn.disabled = true;
                cancelBtn.disabled = false;
                statusSpan.textContent = "连接中...";
                outputPre.textContent = "";
                
                try {
                    const response = await fetch(url, {
                        signal: (controller = new AbortController()).signal
                    });
                    
                    if (!response.ok) {
                        throw new Error(`HTTP错误: ${response.status}`);
                    }
                    
                    if (!response.body) {
                        throw new Error("可读流不可用");
                    }
                    
                    statusSpan.textContent = "正在接收数据...";
                    
                    const reader = response.body.getReader();
                    const decoder = new TextDecoder();
                    
                    while (true) {
                        const { done, value } = await reader.read();
                        if (done) break;
                        
                        const text = decoder.decode(value, { stream: true });
                        outputPre.textContent += text;
                        
                        // 自动滚动到底部
                        outputPre.scrollTop = outputPre.scrollHeight;
                    }
                    
                    statusSpan.textContent = "数据传输完成";
                } catch (error) {
                    if (error.name === "AbortError") {
                        statusSpan.textContent = "请求已取消";
                    } else {
                        statusSpan.textContent = `错误: ${error.message}`;
                        console.error("获取数据失败:", error);
                    }
                } finally {
                    fetchBtn.disabled = false;
                    cancelBtn.disabled = true;
                    controller = null;
                }
            });
            
            // 取消请求
            cancelBtn.addEventListener("click", () => {
                if (controller) {
                    controller.abort();
                }
            });
        });
    </script>
</body>
</html>
    """




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)

