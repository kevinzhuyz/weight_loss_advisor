# 智能体部署指南

## 快速开始

### 1. 克隆仓库
```bash
git clone https://github.com/kevinzhuyz/weight_loss_advisor.git
cd weight_loss_advisor
```

### 2. 安装 Poetry（如果未安装）
```bash
# Windows (PowerShell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# macOS/Linux
curl -sSL https://install.python-poetry.org | python3 -
```

### 3. 创建虚拟环境并安装依赖
```bash
# 创建虚拟环境
poetry install

# 激活虚拟环境
poetry shell

# 或者直接运行（无需激活）
poetry run python -m weight_loss_advisor.agent
```

### 4. 配置环境变量
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑 .env 文件，填入你的 API 密钥
# GOOGLE_API_KEY=your_api_key_here
# PROJECT_ID=your_project_id_here
```

## 详细说明

### 依赖管理
- `pyproject.toml`: 定义项目依赖和配置
- `poetry.lock`: 锁定具体版本，确保一致性
- 支持开发、部署等不同环境的依赖分组

### 环境变量
创建 `.env` 文件并配置以下变量：
```
GOOGLE_API_KEY=your_google_api_key
PROJECT_ID=your_gcp_project_id
LOCATION=us-central1
```

### 运行智能体
```bash
# 开发模式
poetry run python -m weight_loss_advisor.agent

# 生产模式
poetry run python -m weight_loss_advisor.agent --production
```

## 故障排除

### 1. Python 版本问题
确保使用 Python 3.13+：
```bash
python --version
```

### 2. 依赖安装失败
```bash
# 清理缓存
poetry cache clear --all pypi

# 重新安装
poetry install --no-cache
```

### 3. 权限问题
```bash
# 确保 Poetry 在 PATH 中
export PATH="$HOME/.local/bin:$PATH"
```

## 跨平台兼容性

此项目支持：
- Windows 10/11
- macOS 10.15+
- Linux (Ubuntu 18.04+, CentOS 7+)

所有依赖都通过 Poetry 管理，确保在不同平台上的一致性。
