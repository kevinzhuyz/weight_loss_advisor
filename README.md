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

## 快速开始

### 方法一：自动安装（推荐）
```bash
# 克隆仓库
git clone https://github.com/kevinzhuyz/weight_loss_advisor.git
cd weight_loss_advisor

# 运行自动安装脚本
python setup.py
```

### 方法二：手动安装
```bash
# 1. 克隆仓库
git clone https://github.com/kevinzhuyz/weight_loss_advisor.git
cd weight_loss_advisor

# 2. 安装 Poetry（如果未安装）
# Windows:
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# macOS/Linux:
curl -sSL https://install.python-poetry.org | python3 -

# 3. 安装依赖
poetry install

# 4. 配置环境变量
cp env.template .env
# 编辑 .env 文件，填入你的配置

# 5. 运行智能体
poetry run python -m weight_loss_advisor.agent
```

## 详细说明

- 📖 [完整安装指南](SETUP_GUIDE.md)
- 🚀 [部署指南](deployment/DEPLOYMENT_GUIDE.md)
- ☁️ [云部署指南](deployment/CLOUD_DEPLOYMENT_GUIDE.md)

## 免责声明

本系统提供的信息仅供教育和信息目的使用，不构成医疗建议。用户应在做出任何健康决策前咨询合格的医疗专业人士。
