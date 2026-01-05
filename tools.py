from logger import logger


def get_order_status(order_id: str):
    """根据订单号查询物流状态。"""
    database = {
        "123": "已发货，预计明天到达",
        "456": "订单已取消",
    }

    logger.info(f"正在查询订单: {order_id}")

    return database.get(order_id, "找不到该订单信息")


def get_joke_topic(topic: str):
    """获取笑话主题。如果主题不在预设范围内，将引导系统进入兜底逻辑。"""
    valid_topics = ["天气", "宠物", "童年"]

    logger.info(f"收到用户请求主题: {topic}")

    # 核心逻辑：显式判定
    if topic not in valid_topics:
        logger.warning(f"主题 '{topic}' 不在范围内，准备触发兜底...")
        # 这里直接在函数内部调用兜底函数，并返回结果
        # 这样 AI 拿到的直接就是最终答案，没有反驳的机会
        return get_fallback_joke()

    import random
    selected_topic = random.choice(valid_topics)
    logger.info(f"系统匹配主题: {selected_topic}")
    return f"请围绕 '{selected_topic}' 讲个笑话。"


def get_fallback_joke():
    """兜底的笑话。当get_joke_topic这里无法满足时，调用此工具"""
    logger.info(f"\n> 系统日志：正在调用本地函数讲个笑话")

    return "松下为什么没索尼强? 答案:panasonic"
