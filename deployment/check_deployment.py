#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
检查部署状态的脚本
用于查询已部署的智能体信息
"""

import json
import os
from pathlib import Path

def check_deployment_info():
    """检查部署信息文件"""
    project_root = Path(__file__).parent.parent
    deployment_file = project_root / "deployment_info.json"
    
    if not deployment_file.exists():
        print("未找到部署信息文件 deployment_info.json")
        print("请先运行部署命令: python deployment/deploy.py --cloud --project-id YOUR_PROJECT_ID")
        return False
    
    try:
        with open(deployment_file, "r", encoding="utf-8") as f:
            info = json.load(f)
        
        print("部署信息:")
        print("=" * 50)
        print(f"智能体名称: {info.get('display_name', 'N/A')}")
        print(f"项目 ID: {info.get('project_id', 'N/A')}")
        print(f"位置: {info.get('location', 'N/A')}")
        print(f"部署 ID: {info.get('deployment_id', 'N/A')}")
        print(f"状态: {info.get('status', 'N/A')}")
        print(f"存储桶: {info.get('staging_bucket', 'N/A')}")
        
        if info.get('deployment_id'):
            project_id = info.get('project_id')
            location = info.get('location')
            deployment_id = info.get('deployment_id')
            resource_path = f"projects/{project_id}/locations/{location}/reasoningEngines/{deployment_id}"
            print(f"资源路径: {resource_path}")
            
            print("\n部署成功！")
            print("\n使用方法:")
            print("1. 在 Google Cloud Console 中查看:")
            print(f"   https://console.cloud.google.com/ai/platform/reasoning-engines?project={project_id}")
            print("2. 使用 REST API 调用智能体")
            print("3. 可选：注册到 AgentSpace")
        else:
            print("\n部署可能成功，但未获取到部署 ID")
            print("建议:")
            print("1. 检查 Google Cloud Console 中的 Reasoning Engines")
            print("2. 手动查找部署的智能体")
            print("3. 重新运行部署命令")
        
        return True
        
    except Exception as e:
        print(f"读取部署信息时出错: {e}")
        return False

def main():
    """主函数"""
    print("正在检查部署状态...")
    print("=" * 50)
    
    success = check_deployment_info()
    
    if success:
        print("\n检查完成")
    else:
        print("\n检查失败")
    
    return success

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
