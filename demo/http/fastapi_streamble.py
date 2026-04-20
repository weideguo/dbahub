import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI(title="my fastapi server")


@app.get("/stream")
async def chat_stream():
    all_steps = ["aaa","bbb","ccc","ddd"]
    
    async def event_generator():
        for step in all_steps:
            yield f"data: {step}\n\n"
          
            await asyncio.sleep(1)

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.get("/", response_class=HTMLResponse)
async def index():
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
    
if __name__ == "__main__":
    import uvicorn
    # 或uvicorn fastapi_streamble:app --reload
    uvicorn.run("fastapi_streamble:app", host="0.0.0.0", port=8000, reload=True)
    