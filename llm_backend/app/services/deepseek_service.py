from typing import List, Dict, AsyncGenerator
import asyncio
from openai import OpenAI
from app.core.config import settings

class DeepseekService:
    def __init__(self, model: str = "deepseek-ai/DeepSeek-V3"):
        self.client = OpenAI(
            api_key=settings.DEEPSEEK_API_KEY,
            base_url=settings.DEEPSEEK_BASE_URL
        )
        self.model = model

    async def generate_stream(self, messages: List[Dict]) -> AsyncGenerator[str, None]:
        """流式生成回复"""
        try:
            stream = await asyncio.to_thread(
                self.client.chat.completions.create,
                model=self.model,
                messages=messages,
                stream=True
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            print(f"Stream generation error: {str(e)}")
            raise

    async def generate(self, messages: List[Dict]) -> str:
        try:
            response = await asyncio.to_thread(
                self.client.chat.completions.create,
                model="deepseek-ai/DeepSeek-V3",
                messages=messages,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Generation error: {str(e)}")
            raise 