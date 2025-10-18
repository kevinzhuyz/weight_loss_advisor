# Google Cloud 部署指南

本指南将帮助您将减肥咨询智能体部署到 Google Cloud Platform。

## 前置要求

### 1. 安装依赖
```bash
pip install google-cloud-aiplatform google-adk
```

### 2. 设置 Google Cloud 认证
```bash
# 安装 Google Cloud CLI
# 然后进行认证
gcloud auth login
gcloud auth application-default login
```

### 3. 设置项目
```bash
# 设置默认项目
gcloud config set project YOUR_PROJECT_ID

# 启用必要的 API
gcloud services enable aiplatform.googleapis.com
```

## 部署选项

### 本地部署
```bash
# 基本本地部署
python deployment/deploy.py --create

# 或者直接运行（默认本地部署）
python deployment/deploy.py
```

### Google Cloud 部署
```bash
# 基本云端部署
python deployment/deploy.py --cloud --project-id YOUR_PROJECT_ID

# 完整参数云端部署
python deployment/deploy.py --cloud \
  --project-id YOUR_PROJECT_ID \
  --location us-central1 \
  --agent-name weight-loss-advisor \
  --description "减肥咨询智能体"

# 指定存储桶和临时文件夹
python deployment/deploy.py --cloud \
  --project-id YOUR_PROJECT_ID \
  --staging-bucket gs://your-staging-bucket \
  --temp-folder D:\temp
```

## 参数说明

- `--create`: 本地部署智能体
- `--cloud`: 部署到 Google Cloud
- `--project-id`: Google Cloud 项目 ID（云端部署必需）
- `--location`: Google Cloud 位置（默认: us-central1）
- `--agent-name`: 智能体名称（默认: weight-loss-advisor）
- `--description`: 智能体描述（默认: 减肥咨询智能体）
- `--staging-bucket`: Google Cloud 存储桶（可选，默认: gs://{project-id}-staging）
- `--temp-folder`: 临时文件夹路径（可选，默认: ~/adk-temp）

## 部署后

部署成功后，脚本会创建一个 `deployment_info.json` 文件，包含：
- 智能体 ID
- 显示名称
- 项目 ID
- 位置
- 部署时间

## 使用部署的智能体

### 通过 Google Cloud Console
1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 导航到 AI Platform > Agents
3. 找到您的智能体并点击使用

### 通过 REST API
```python
import requests

# 使用部署信息中的 agent_id
agent_id = "projects/YOUR_PROJECT/locations/us-central1/agents/AGENT_ID"

# 调用智能体
response = requests.post(
    f"https://{location}-aiplatform.googleapis.com/v1/{agent_id}:predict",
    headers={"Authorization": f"Bearer {access_token}"},
    json={"instances": [{"input": "我想减肥，请给我建议"}]}
)
```

## 故障排除

### 常见错误
1. **认证错误**: 确保已正确设置 Google Cloud 认证
2. **权限错误**: 确保您的账户有 AI Platform 相关权限
3. **API 未启用**: 确保已启用 AI Platform API
4. **项目 ID 错误**: 确保项目 ID 正确且您有访问权限

### 检查部署状态
```bash
# 查看部署信息
cat deployment_info.json

# 列出项目中的智能体
gcloud ai agents list --project=YOUR_PROJECT_ID
```

## 成本考虑

- Google Cloud AI Platform 按使用量计费
- 建议在测试阶段设置预算警报
- 可以设置配额限制来控制成本

## 支持

如果遇到问题，请检查：
1. Google Cloud 控制台中的错误日志
2. 本地部署日志
3. 网络连接和防火墙设置
