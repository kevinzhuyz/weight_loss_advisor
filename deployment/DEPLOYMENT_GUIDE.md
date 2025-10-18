# 减肥咨询智能体 - ADK本地部署指南

## 项目概述

这是一个基于Google ADK的减肥咨询智能体系统，通过协调多个专业子智能体为用户提供全面的减肥指导。

## 系统架构

```
weight_loss_advisor/
├── agent.py                    # 主减肥咨询智能体
├── prompt.py                   # 主智能体提示词
├── requirements.txt            # 依赖包列表
├── test_local.py              # 本地测试脚本
├── sub_agents/                # 子智能体目录
│   ├── health_assessor/        # 健康评估师
│   ├── nutritionist/          # 营养师
│   ├── fitness_coach/         # 运动教练
│   └── progress_tracker/      # 进度跟踪师
└── README.md                  # 项目说明
```

## 快速开始

### 1. 安装依赖

```bash
cd weight_loss_advisor
pip install -r requirements.txt
```

### 2. 测试智能体

```bash
python test_local.py
```

### 3. 在代码中使用

```python
import asyncio
from agent import root_agent

async def main():
    # 用户输入
    user_input = """
    我想开始减肥，请帮我制定一个计划。
    
    我的信息：
    - 身高：170厘米
    - 体重：75公斤
    - 目标：65公斤
    - 年龄：30岁
    - 性别：男性
    """
    
    # 运行智能体
    result = await root_agent.run(user_input)
    print(result)

# 运行
asyncio.run(main())
```

## 智能体功能

### 主智能体 (weight_loss_coordinator)
- 协调所有子智能体
- 引导用户完成完整的减肥咨询流程
- 提供结构化的减肥建议

### 子智能体

#### 1. 健康评估师 (health_assessor)
- 评估用户当前健康状况
- 计算BMI和健康指标
- 分析减肥目标可行性
- 识别健康风险

#### 2. 营养师 (nutritionist)
- 制定个性化营养计划
- 计算每日卡路里目标
- 设计宏量营养素分配
- 提供具体餐食建议

#### 3. 运动教练 (fitness_coach)
- 设计个性化运动方案
- 制定有氧运动计划
- 安排力量训练
- 提供运动安全指导

#### 4. 进度跟踪师 (progress_tracker)
- 建立进度监测系统
- 设定减肥里程碑
- 提供调整策略
- 维持长期动机

## 使用流程

1. **健康评估**：用户提供基本信息，健康评估师分析健康状况
2. **营养计划**：营养师基于健康评估制定个性化饮食计划
3. **运动方案**：运动教练设计适合的运动计划
4. **进度跟踪**：进度跟踪师建立监测和调整机制

## 注意事项

- 本系统仅供教育和信息目的使用
- 不构成医疗建议
- 用户应在做出健康决策前咨询医疗专业人士
- 所有建议基于AI模型生成，仅供参考

## 技术依赖

- Google ADK (Agent Development Kit)
- Google Cloud AI Platform
- Google Generative AI
- Python 3.9+

## 故障排除

如果遇到导入错误，请确保：
1. 所有依赖已正确安装
2. Python路径设置正确
3. 在正确的目录中运行脚本

## 联系支持

如有问题，请检查：
1. 依赖安装是否完整
2. Python版本是否符合要求
3. 文件路径是否正确
