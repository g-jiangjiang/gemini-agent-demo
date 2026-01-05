# Gemini Agent Demo

一个基于 Google Gemini 的轻量级 AI Agent 开发脚手架。

## 🛠️ 快速开始
1. 安装依赖: `pip install -U google-generativeai python-dotenv`
2. 创建 `.env` 文件并填入你的 `GEMINI_API_KEY`。
3. 运行项目: `python main.py`

## 📂 目录结构

- `main.py`: 交互入口，负责信号捕获与 UI 反馈。
- `agent_core.py`: Agent 初始化中心，处理消息路由与异常兜底。
- `tools.py`: 业务逻辑插件库，支持动态参数注入。
- `config.py`: 集中化参数管理（模型选择、温度控制、密钥加载）。
- `logger.py`: 封装日志处理逻辑，支持文件审计。
