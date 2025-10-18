# Weight Loss Advisor Agent

这是一个基于AI的减肥咨询智能体系统，通过协调多个专业子智能体为用户提供全面的减肥指导。

## 功能特点

- **健康评估师**：评估用户当前健康状况，计算BMI，分析减肥目标可行性
- **营养师**：制定个性化营养计划，包括卡路里目标、宏量营养素分配和餐食建议
- **运动教练**：设计适合的运动方案，包括有氧运动、力量训练和灵活性训练
- **进度跟踪师**：建立全面的进度监测系统，包括体重、身体测量和里程碑设定

## 系统架构

```
weight_loss_advisor/
├── agent.py                    # 主减肥咨询智能体
├── prompt.py                   # 主智能体提示词
├── sub_agents/                 # 子智能体目录
│   ├── health_assessor/        # 健康评估师
│   ├── nutritionist/          # 营养师
│   ├── fitness_coach/         # 运动教练
│   └── progress_tracker/      # 进度跟踪师
└── pyproject.toml             # 项目配置
```

## 使用方法

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行智能体：
```python
from weight_loss_advisor.agent import root_agent
```

## 免责声明

本系统提供的信息仅供教育和信息目的使用，不构成医疗建议。用户应在做出任何健康决策前咨询合格的医疗专业人士。
