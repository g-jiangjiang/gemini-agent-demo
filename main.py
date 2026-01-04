import google.generativeai as genai
import os
from dotenv import load_dotenv

# 1. 配置 API KEY
# 加载 .env 文件
load_dotenv()

# 从环境变量中读取
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)


# 2. 工具函数 (保持不变)
def get_order_status(order_id: str):
    """根据订单号查询物流状态。"""
    database = {
        "123": "已发货，预计明天到达",
        "456": "订单已取消",
    }
    print(f"\n> 系统日志：正在调用本地函数查询订单 {order_id}...")
    return database.get(order_id, "找不到该订单信息")


def get_fallback_joke():
    """兜底的笑话。当get_joke_topic这里无法满足时，调用此工具"""
    print(f"\n> 系统日志：正在调用本地函数讲个笑话...")
    return "为什么程序员分不清万圣节和圣诞节？因为 Oct 31 == Dec 25。"


def get_joke_topic():
    """当用户想听笑话时，调用此函数获取一个随机的笑话主题。"""
    topics = ["程序员的格子衫", "PM 的需求变更", "Bug 的自我修养"]
    import random
    topic = random.choice(topics)
    # 关键：不给完整的笑话，只给一个“引子”
    return f"请围绕 '{topic}' 这个主题，发挥你的幽默感现编一个笑话。"


# 3. 初始化模型，尝试使用更稳妥的模型标识
model = genai.GenerativeModel(
    model_name='models/gemini-2.5-flash',
    tools=[get_order_status, get_fallback_joke, get_joke_topic]
)

# 4. 开启对话
chat = model.start_chat(enable_automatic_function_calling=True)

print("--- AI Agent 已上线 (输入 'exit' 退出) ---")

while True:
    user_input = input("\n用户: ")
    if user_input.lower() == 'exit':
        break

    try:
        # Agent 开始思考并执行
        response = chat.send_message(user_input)
        print(f"AI: {response.text}")
    except Exception as e:
        print(f"\n[错误]: {e}")
        print("提示：如果遇到网络连接问题，请确保你的科学上网环境开启了‘全局模式’。")
