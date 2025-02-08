# LLM Backend Service

一个基于 FastAPI 的 LLM 后端服务，支持 Deepseek V3 / R1 API 和 Ollama 本地模型，提供流式输出的对话和推理能力。

## 项目结构

```
llm_backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── chat.py
│   ├── core/
│   │   └── config.py
│   └── services/
│       ├── deepseek_service.py
│       ├── ollama_service.py
│       └── llm_factory.py
├── main.py
├── .env.example          # 环境变量示例文件
├── .gitignore           # Git 忽略文件配置
├── requirements.txt
└── README.md
```

## 环境要求

- Python 3.10+
- Ollama (可选，如果需要使用本地模型)

## 安装步骤

1. 克隆项目
```bash
git clone <your-repo-url>
cd llm_backend
```

2. 创建并激活虚拟环境
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 创建配置文件
```bash
# 复制示例配置文件
cp .env.example .env
```

## 配置说明

创建 `.env` 文件并配置以下内容：

```env
# Deepseek settings
DEEPSEEK_API_KEY=your-api-key
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1

# Ollama settings
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_CHAT_MODEL=qwen2.5:1.5b
OLLAMA_REASON_MODEL=deepseek-r1:32b

# Service selection (deepseek or ollama)
CHAT_SERVICE=deepseek
REASON_SERVICE=ollama
```

配置说明：
- `DEEPSEEK_API_KEY`: Deepseek API 密钥
- `DEEPSEEK_BASE_URL`: Deepseek API 地址
- `OLLAMA_BASE_URL`: Ollama 服务地址
- `OLLAMA_CHAT_MODEL`: Ollama 聊天模型名称
- `OLLAMA_REASON_MODEL`: Ollama 推理模型名称
- `CHAT_SERVICE`: 聊天服务类型 (deepseek 或 ollama)
- `REASON_SERVICE`: 推理服务类型 (deepseek 或 ollama)

## 启动服务

```bash
# 开发模式
uvicorn main:app --reload --port 8000

# 生产模式
uvicorn main:app --host 0.0.0.0 --port 8000
```

服务启动后访问：
- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/health

## API 接口

### 聊天接口
```bash
POST /chat
Content-Type: application/json

{
    "messages": [
        {"role": "user", "content": "你好"}
    ]
}
```

### 推理接口
```bash
POST /reason
Content-Type: application/json

{
    "messages": [
        {"role": "user", "content": "分析这段代码"}
    ]
}
```

## 前端项目

本项目配套的前端实现请参考：[My-DeepSeek-Web](https://github.com/MuYuCheney/My-DeepSeek-Web)

前端项目提供了完整的用户界面，支持：
- 智能对话
- Markdown 渲染
- 代码高亮
- 流式输出
- 聊天记录

## 注意事项

1. `.env` 文件包含敏感信息，已添加到 `.gitignore`，不会上传到代码仓库
2. `.venv` 虚拟环境目录也已添加到 `.gitignore`
3. 使用 Ollama 时需要确保 Ollama 服务已启动且可访问
4. 建议在生产环境中配置 CORS 和安全设置

## License

MIT 