from typing import List, Dict, AsyncGenerator
import httpx
import json
from app.core.config import settings

class OllamaService:
    def __init__(self, model_name: str = "deepseek-r1:1.5b"):
        self.base_url = settings.OLLAMA_BASE_URL
        self.model_name = model_name
        self.default_options = {
            "temperature": 0.7,
            "top_p": 0.9
        }

    async def generate_stream(self, messages: List[Dict]) -> AsyncGenerator[str, None]:
        """流式生成回复"""
        try:
            prompt = self._format_messages(messages)
            
            timeout = httpx.Timeout(30.0, connect=10.0, read=None)
            
            async with httpx.AsyncClient(timeout=timeout) as client:
                async with client.stream('POST', f"{self.base_url}/api/generate", json={
                    "model": self.model_name,
                    "prompt": prompt,
                    "stream": True,
                    "options": self.default_options
                }) as response:
                    async for line in response.aiter_lines():
                        if line:
                            try:
                                data = json.loads(line)
                                if data.get("response"):
                                    yield data["response"]
                            except json.JSONDecodeError as e:
                                print(f"JSON decode error: {str(e)}, line: {line}")
                                continue
        except Exception as e:
            print(f"Stream generation error: {str(e)}")
            raise

    def _format_messages(self, messages: List[Dict]) -> str:
        """将消息列表格式化为 prompt"""
        formatted_messages = []
        for msg in messages:
            role = msg["role"]
            content = msg["content"]
            if role == "system":
                formatted_messages.append(content)
            else:
                formatted_messages.append(f"<|{role}|>{content}")
        
        formatted_messages.append("<|Assistant|>")
        return "\n".join(formatted_messages) 