from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Dict
from app.services.llm_factory import LLMFactory
from app.services.search_service import SearchService

app = FastAPI(title="LLM Chat API")

# CORS设置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中要设置具体的域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]

class ReasonRequest(BaseModel):
    messages: List[Dict[str, str]]

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """聊天接口"""
    try:
        chat_service = LLMFactory.create_chat_service()
        async def format_stream():
            # 添加一个初始换行，让输出更整洁
            yield "data: \n\n"
            async for chunk in chat_service.generate_stream(request.messages):
                yield f"data: {chunk}\n\n"
                
        return StreamingResponse(
            format_stream(),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/reason")
async def reason_endpoint(request: ReasonRequest):
    """推理接口"""
    try:
        reasoner = LLMFactory.create_reasoner_service()
        async def format_stream():
            yield "data: \n\n"
            # 直接使用请求中的 messages
            async for chunk in reasoner.generate_stream(request.messages):
                yield f"data: {chunk}\n\n"
                
        return StreamingResponse(
            format_stream(),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search_endpoint(request: ChatRequest):
    """带搜索功能的聊天接口"""
    try:
        search_service = SearchService()
        async def format_stream():
            yield "data: \n\n"
            async for chunk in search_service.generate_stream(request.messages):
                yield f"data: {chunk}\n\n"
                
        return StreamingResponse(
            format_stream(),
            media_type="text/event-stream"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "ok"} 