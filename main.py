from agent_core import GeminiAgent
from logger import logger


def main():
    agent = GeminiAgent()
    print("--- 底座已就绪 ---")

    try:
        while True:
            user_input = input("\n用户: ")
            if user_input.lower() in ['exit', 'quit']:
                print("再见！")
                break

            response = agent.send_query(user_input)
            # 根据 status 决定是否打印
            if response["status"] == "success":
                print(f"AI: {response['content']}")
            else:
                print(f"提示: {response['content']}")

    except KeyboardInterrupt:
        # 当检测到 Ctrl+C 时执行这里
        print("\n\n> 检测到退出指令，正在关闭系统... 再见！")
    except Exception as e:
        logger.error(f"运行中发生意外错误: {e}")


if __name__ == "__main__":
    main()
