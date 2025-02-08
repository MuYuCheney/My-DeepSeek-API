from pydantic_settings import BaseSettings
from enum import Enum

class ServiceType(str, Enum):
    DEEPSEEK = "deepseek"
    OLLAMA = "ollama"

class Settings(BaseSettings):
    # Deepseek settings
    DEEPSEEK_API_KEY: str = "sk-fb7369c51357447d9bfa082b012346d4"
    DEEPSEEK_BASE_URL: str = "https://api.deepseek.com/v1"
    
    # Ollama settings
    OLLAMA_BASE_URL: str = "http://192.168.110.131:11434"
    OLLAMA_CHAT_MODEL: str = "qwen2.5:32b"      # Ollama 聊天模型
    OLLAMA_REASON_MODEL: str = "deepseek-r1:1.5b"  # Ollama 推理模型
    
    # Service selection
    CHAT_SERVICE: ServiceType = ServiceType.DEEPSEEK    # 选择聊天服务
    REASON_SERVICE: ServiceType = ServiceType.OLLAMA    # 选择推理服务
    
    class Config:
        env_file = ".env"

settings = Settings() 