# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Deployment script for weight loss advisor agent"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import Optional

# Add the project root directory to Python path
current_dir = Path(__file__).parent
project_root = current_dir.parent
sys.path.insert(0, str(project_root))

try:
    from google.adk.agents import LlmAgent
    from google.adk.tools.agent_tool import AgentTool
    import subprocess
    import tempfile
    import shutil
    ADK_AVAILABLE = True
except ImportError:
    ADK_AVAILABLE = False
    print("⚠️  Google ADK 依赖未安装，请运行: pip install google-adk")

def deploy_to_google_cloud(
    project_id: str,
    location: str = "us-central1",
    agent_name: str = "weight-loss-advisor",
    description: str = "减肥咨询智能体",
    staging_bucket: Optional[str] = None,
    temp_folder: Optional[str] = None
):
    """Deploy the weight loss advisor agent to Google Cloud using ADK"""
    
    if not ADK_AVAILABLE:
        print("❌ Google ADK 依赖未安装，无法部署到云端")
        print("请运行: pip install google-adk")
        return False
    
    print("正在部署减肥咨询智能体到 Google Cloud...")
    print("=" * 50)
    
    try:
        # Import the agent to verify it works
        from weight_loss_advisor.agent import root_agent
        print("✅ 智能体导入成功")
        print(f"智能体名称: {root_agent.name}")
        print(f"智能体描述: {root_agent.description}")
        
        # Set up staging bucket if not provided
        if not staging_bucket:
            staging_bucket = f"gs://{project_id}-staging"
            print(f"⚠️  未指定存储桶，使用默认: {staging_bucket}")
        
        # Set up temp folder if not provided
        if not temp_folder:
            temp_folder = str(Path.home() / "adk-temp")
            os.makedirs(temp_folder, exist_ok=True)
            print(f"⚠️  未指定临时文件夹，使用默认: {temp_folder}")
        
        print(f"✅ 项目 ID: {project_id}")
        print(f"✅ 位置: {location}")
        print(f"✅ 存储桶: {staging_bucket}")
        print(f"✅ 临时文件夹: {temp_folder}")
        
        # Build ADK deploy command
        deploy_cmd = [
            "adk", "deploy", "agent_engine",
            "--project", project_id,
            "--region", location,
            "--display_name", agent_name,
            "--temp_folder", temp_folder,
            "--staging_bucket", staging_bucket,
            "--absolutize_imports", "False",  # Skip import path conversion
            "."  # Deploy current directory
        ]
        
        print("\n正在执行 ADK 部署命令...")
        print(f"命令: {' '.join(deploy_cmd)}")
        
        # Execute the deployment
        result = subprocess.run(
            deploy_cmd,
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=600  # 10 minutes timeout
        )
        
        if result.returncode == 0:
            print("✅ ADK 部署命令执行成功")
            print("部署输出:")
            print(result.stdout)
            
            # Try to extract deployment ID from output
            deployment_id = None
            for line in result.stdout.split('\n'):
                if 'reasoningEngines/' in line or 'deployment_id' in line.lower():
                    # Extract ID from line like "projects/.../reasoningEngines/123456"
                    parts = line.split('/')
                    if len(parts) > 0:
                        deployment_id = parts[-1].strip()
                        break
            
            # Save deployment info
            deployment_info = {
                "deployment_id": deployment_id,
                "display_name": agent_name,
                "description": description,
                "project_id": project_id,
                "location": location,
                "staging_bucket": staging_bucket,
                "temp_folder": temp_folder,
                "deployment_time": str(Path().cwd()),
                "full_output": result.stdout
            }
            
            deployment_file = project_root / "deployment_info.json"
            with open(deployment_file, "w", encoding="utf-8") as f:
                json.dump(deployment_info, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 部署信息已保存到: {deployment_file}")
            
            if deployment_id:
                print(f"✅ 部署 ID: {deployment_id}")
                print(f"✅ 智能体资源路径: projects/{project_id}/locations/{location}/reasoningEngines/{deployment_id}")
            
            print("\n🎉 减肥咨询智能体云端部署成功！")
            print("\n后续步骤：")
            print("1. 在 Google Cloud Console 中查看部署的智能体")
            print("2. 使用部署 ID 进行 API 调用")
            print("3. 可选：注册到 AgentSpace")
            
            return True
        else:
            print("❌ ADK 部署命令执行失败")
            print("错误输出:")
            print(result.stderr)
            print("标准输出:")
            print(result.stdout)
            return False
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        return False
    except subprocess.TimeoutExpired:
        print("❌ 部署超时（10分钟）")
        return False
    except Exception as e:
        print(f"❌ 云端部署错误: {e}")
        return False


def deploy_weight_loss_advisor():
    """Deploy the weight loss advisor agent locally"""
    
    print("正在本地部署减肥咨询智能体...")
    print("=" * 50)
    
    try:
        # Import the agent
        from weight_loss_advisor.agent import root_agent
        
        print("✅ 智能体导入成功")
        print(f"智能体名称: {root_agent.name}")
        print(f"智能体描述: {root_agent.description}")
        print(f"输出键: {root_agent.output_key}")
        
        # List available tools
        print(f"\n可用工具数量: {len(root_agent.tools)}")
        for i, tool in enumerate(root_agent.tools, 1):
            print(f"  {i}. {tool.agent.name}")
        
        print("\n🎉 减肥咨询智能体本地部署成功！")
        print("\n使用方法：")
        print("1. 导入智能体：from weight_loss_advisor.agent import root_agent")
        print("2. 运行智能体：await root_agent.run('您的减肥咨询请求')")
        print("3. 测试智能体：python test_agent.py")
        
        return True
        
    except ImportError as e:
        print(f"❌ 导入错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 部署错误: {e}")
        return False


def main():
    """Main function with command line argument parsing"""
    parser = argparse.ArgumentParser(description="部署减肥咨询智能体")
    parser.add_argument("--create", action="store_true", help="本地部署智能体")
    parser.add_argument("--cloud", action="store_true", help="部署到 Google Cloud")
    parser.add_argument("--project-id", type=str, help="Google Cloud 项目 ID")
    parser.add_argument("--location", type=str, default="us-central1", help="Google Cloud 位置 (默认: us-central1)")
    parser.add_argument("--agent-name", type=str, default="weight-loss-advisor", help="智能体名称 (默认: weight-loss-advisor)")
    parser.add_argument("--description", type=str, default="减肥咨询智能体", help="智能体描述")
    parser.add_argument("--staging-bucket", type=str, help="Google Cloud 存储桶 (可选)")
    parser.add_argument("--temp-folder", type=str, help="临时文件夹路径 (可选)")
    
    args = parser.parse_args()
    
    if args.cloud:
        if not args.project_id:
            print("❌ 部署到 Google Cloud 需要指定 --project-id 参数")
            print("使用方法: python deployment/deploy.py --cloud --project-id YOUR_PROJECT_ID")
            print("可选参数: --staging-bucket, --temp-folder")
            return False
        
        success = deploy_to_google_cloud(
            project_id=args.project_id,
            location=args.location,
            agent_name=args.agent_name,
            description=args.description,
            staging_bucket=args.staging_bucket,
            temp_folder=args.temp_folder
        )
    else:
        # Default to local deployment
        success = deploy_weight_loss_advisor()
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
