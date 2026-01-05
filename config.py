import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "models/gemini-2.5-flash"
    TEMPERATURE = 0.7  # 控制 AI 的随机性
    SYSTEM_INSTRUCTION = """你是一个专业的业务助手。
    1. 优先调用工具处理用户请求。
    2. 如果工具返回了结果，请严格基于工具结果回答，不要编造。
    3. 保持专业、简洁的语气。"""
