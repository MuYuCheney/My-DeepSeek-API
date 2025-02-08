from typing import Union
from app.core.config import settings, ServiceType
from .deepseek_service import DeepseekService
from .ollama_service import OllamaService

class LLMFactory:
    @staticmethod
    def create_chat_service() -> Union[DeepseekService, OllamaService]:
        """创建聊天服务，可以选择 Deepseek 或 Ollama"""
        if settings.CHAT_SERVICE == ServiceType.DEEPSEEK:
            return DeepseekService(model="deepseek-ai/DeepSeek-V3")
        else:
            return OllamaService(model_name=settings.OLLAMA_CHAT_MODEL)

    @staticmethod
    def create_reasoner_service() -> Union[DeepseekService, OllamaService]:
        """创建推理服务，可以选择 Deepseek 或 Ollama"""
        if settings.REASON_SERVICE == ServiceType.DEEPSEEK:
            return DeepseekService(model="deepseek-reasoner")
        else:
            return OllamaService(model_name=settings.OLLAMA_REASON_MODEL) 