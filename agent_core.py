import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

import time
import google.generativeai as genai
from google.api_core import exceptions
from config import Config
from logger import logger
import tools


class GeminiAgent:
    def __init__(self):
        genai.configure(api_key=Config.API_KEY)
        self.model = genai.GenerativeModel(
            model_name=Config.MODEL_NAME,
            tools=[tools.get_order_status, tools.get_joke_topic, tools.get_fallback_joke],
            # 新增：注入系统指令
            system_instruction=Config.SYSTEM_INSTRUCTION
        )

        self.max_history = 10

        self.chat = self.model.start_chat(history=[], enable_automatic_function_calling=True)

    def send_query(self, user_input):

        # ... 在发送之前检查一下历史长度 ...
        if len(self.chat.history) > self.max_history:
            # 删掉最老的两轮（一问一答）
            self.chat.history = self.chat.history[2:]
            logger.info("对话历史过长，已自动清理老旧上下文以节省 Token。")

        try:
            response = self.chat.send_message(user_input)

            # 新增：Token 消耗监控（仅部分模型/版本支持 usage_metadata）
            if hasattr(response, 'usage_metadata'):
                logger.usage(
                    response.usage_metadata.prompt_token_count,
                    response.usage_metadata.candidates_token_count
                )

            # 修改：返回标准化对象（字典格式）
            return {
                "status": "success",
                "content": response.text
            }

        except exceptions.ResourceExhausted:
            logger.warning("触发频率限制 (429)")
            return {"status": "error", "content": "服务器繁忙，请稍后再试。"}
        except Exception as e:
            logger.error(f"发生未知错误: {e}")
            return {"status": "error", "content": "抱歉，系统暂时出了点小状况。"}
