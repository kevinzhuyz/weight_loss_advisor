#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
获取部署 ID 的脚本
通过 Google Cloud Console API 查询部署的智能体
"""

import json
import os
import subprocess
from pathlib import Path

def get_deployment_id_from_console(project_id: str, location: str = "us-central1", agent_name: str = "weight-loss-advisor"):
    """通过 Google Cloud Console 获取部署 ID"""
    
    print(f"正在查询项目 {project_id} 中的智能体...")
    
    try:
        # 方法1: 使用 gcloud 命令查询
        cmd = [
            "gcloud", "ai", "reasoning-engines", "list",
            "--project", project_id,
            "--location", location,
            "--filter", f"displayName:{agent_name}",
            "--format", "value(name)"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and result.stdout.strip():
            deployment_path = result.stdout.strip()
            # 提取部署 ID
            parts = deployment_path.split('/')
            if len(parts) > 0:
                deployment_id = parts[-1]
                print(f"找到部署 ID: {deployment_id}")
                return deployment_id, deployment_path
        
        print("未找到匹配的部署")
        return None, None
        
    except FileNotFoundError:
        print("gcloud 命令未找到，请安装 Google Cloud CLI")
        return None, None
    except Exception as e:
        print(f"查询时出错: {e}")
        return None, None

def update_deployment_info(deployment_id: str, deployment_path: str):
    """更新部署信息文件"""
    project_root = Path(__file__).parent.parent
    deployment_file = project_root / "deployment_info.json"
    
    if not deployment_file.exists():
        print("未找到部署信息文件")
        return False
    
    try:
        with open(deployment_file, "r", encoding="utf-8") as f:
            info = json.load(f)
        
        # 更新部署信息
        info["deployment_id"] = deployment_id
        info["deployment_resource_path"] = deployment_path
        info["status"] = "deployed"
        
        with open(deployment_file, "w", encoding="utf-8") as f:
            json.dump(info, f, indent=2, ensure_ascii=False)
        
        print(f"已更新部署信息文件: {deployment_file}")
        return True
        
    except Exception as e:
        print(f"更新部署信息时出错: {e}")
        return False

def main():
    """主函数"""
    print("正在获取部署 ID...")
    print("=" * 50)
    
    # 从部署信息文件中读取项目信息
    project_root = Path(__file__).parent.parent
    deployment_file = project_root / "deployment_info.json"
    
    if not deployment_file.exists():
        print("未找到部署信息文件，请先运行部署命令")
        return False
    
    try:
        with open(deployment_file, "r", encoding="utf-8") as f:
            info = json.load(f)
        
        project_id = info.get("project_id")
        location = info.get("location", "us-central1")
        agent_name = info.get("display_name", "weight-loss-advisor")
        
        if not project_id:
            print("部署信息文件中缺少项目 ID")
            return False
        
        # 查询部署 ID
        deployment_id, deployment_path = get_deployment_id_from_console(project_id, location, agent_name)
        
        if deployment_id:
            # 更新部署信息
            update_deployment_info(deployment_id, deployment_path)
            
            print("\n部署信息:")
            print(f"项目 ID: {project_id}")
            print(f"位置: {location}")
            print(f"智能体名称: {agent_name}")
            print(f"部署 ID: {deployment_id}")
            print(f"资源路径: {deployment_path}")
            
            print("\n使用方法:")
            print("1. 在 Google Cloud Console 中查看:")
            print(f"   https://console.cloud.google.com/ai/platform/reasoning-engines?project={project_id}")
            print("2. 使用 REST API 调用智能体")
            print("3. 可选：注册到 AgentSpace")
            
            return True
        else:
            print("\n未找到部署 ID，可能的原因:")
            print("1. 部署还在进行中，请稍后重试")
            print("2. 智能体名称不匹配")
            print("3. 项目或位置不正确")
            print("\n建议:")
            print("1. 检查 Google Cloud Console 中的 Reasoning Engines")
            print("2. 手动查找部署的智能体")
            print("3. 确认项目 ID 和位置是否正确")
            
            return False
            
    except Exception as e:
        print(f"处理时出错: {e}")
        return False

if __name__ == "__main__":
    import sys
    success = main()
    sys.exit(0 if success else 1)
