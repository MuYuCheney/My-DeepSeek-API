from setuptools import setup, find_packages

setup(
    name="llm_backend",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "pydantic>=1.8.0",
        "pydantic-settings>=2.0.0",
        "openai>=1.0.0",
        "httpx>=0.24.0",
        "python-dotenv>=0.19.0",
        "tenacity>=8.0.0",
    ],
) 