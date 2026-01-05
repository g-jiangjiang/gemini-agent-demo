import logging
import sys

# 1. 配置日志格式（用于记录到文件或调试台）
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("agent.log", encoding="utf-8"),  # 记录到文件，方便以后查
    ]
)

# 2. 获取原生的 logger
_raw_logger = logging.getLogger("GeminiAgent")


# 3. 定义一个对外的类，实现“一行日志 + 一行 print”
class SmartLogger:
    @staticmethod
    def info(msg, user_friendly=True):
        # 记录标准的系统日志
        _raw_logger.info(msg)

        # 如果需要给用户看，就额外 print 一行干净的提示
        if user_friendly:
            print(f"> [系统反馈]: {msg}")

    @staticmethod
    def error(msg):
        _raw_logger.error(msg)
        print(f"❌ 出错了: {msg}")

    @staticmethod
    def warning(msg):
        _raw_logger.warning(msg)
        print(f"⚠️ 警告: {msg}")

    @staticmethod
    def usage(prompt_tokens, completion_tokens):
        total = prompt_tokens + completion_tokens
        # 记录到日志文件
        _raw_logger.info(f"[Token Usage] Input: {prompt_tokens}, Output: {completion_tokens}, Total: {total}")


# 创建实例供全项目使用
logger = SmartLogger()
