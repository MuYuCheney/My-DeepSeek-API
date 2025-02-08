from pydantic_settings import BaseSettings
from enum import Enum

class ServiceType(str, Enum):
    DEEPSEEK = "deepseek"
    OLLAMA = "ollama"

class Settings(BaseSettings):
    # Deepseek settings
    DEEPSEEK_API_KEY: str
    DEEPSEEK_BASE_URL: str
    
    # Ollama settings
    OLLAMA_BASE_URL: str
    OLLAMA_CHAT_MODEL: str
    OLLAMA_REASON_MODEL: str
    
    # Service selection
    CHAT_SERVICE: ServiceType = ServiceType.DEEPSEEK    # 选择聊天服务
    REASON_SERVICE: ServiceType = ServiceType.OLLAMA    # 选择推理服务
    
    # Search settings
    SERPAPI_KEY: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings() 