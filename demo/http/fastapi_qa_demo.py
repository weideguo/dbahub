# 使用fastapi实现简单问答的服务

from pydantic import BaseModel

import uvicorn

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 定义请求模型
class QuestionRequest(BaseModel):
    question: str


# 定义响应模型
class AnswerResponse(BaseModel):
    answer: str


################## 自定义生成回答的模块，必须更改此处
try:
    from xxx import qa_chain
    generate_answer_func = qa_chain.run
except:
    def echo(s):
        return s
    generate_answer_func = echo
#################


@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        user_question = request.question
        print(user_question)

        answer = generate_answer_func(user_question)

        answer = AnswerResponse(answer=answer)
        print(answer)
        return answer
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
    
    
    