#!/usr/bin/env python3
"""
智能体自动安装脚本
支持 Windows、macOS 和 Linux
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, shell=True):
    """运行命令并处理错误"""
    try:
        result = subprocess.run(command, shell=shell, check=True, 
                              capture_output=True, text=True)
        print(f"✓ 成功: {command}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"✗ 错误: {command}")
        print(f"错误信息: {e.stderr}")
        return None

def check_python_version():
    """检查 Python 版本"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 13):
        print("❌ 错误: 需要 Python 3.13 或更高版本")
        print(f"当前版本: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✓ Python 版本: {version.major}.{version.minor}.{version.micro}")
    return True

def install_poetry():
    """安装 Poetry"""
    print("正在检查 Poetry...")
    
    # 检查 Poetry 是否已安装
    result = run_command("poetry --version", shell=True)
    if result:
        print("✓ Poetry 已安装")
        return True
    
    print("正在安装 Poetry...")
    system = platform.system().lower()
    
    if system == "windows":
        # Windows 安装
        cmd = "(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -"
        result = run_command(cmd, shell=True)
    else:
        # macOS/Linux 安装
        cmd = "curl -sSL https://install.python-poetry.org | python3 -"
        result = run_command(cmd, shell=True)
    
    if result:
        print("✓ Poetry 安装成功")
        # 添加到 PATH
        if system != "windows":
            run_command("export PATH=\"$HOME/.local/bin:$PATH\"", shell=True)
        return True
    else:
        print("❌ Poetry 安装失败")
        return False

def setup_environment():
    """设置环境"""
    print("正在设置环境...")
    
    # 安装依赖
    result = run_command("poetry install", shell=True)
    if not result:
        print("❌ 依赖安装失败")
        return False
    
    # 创建 .env 文件
    env_file = Path(".env")
    if not env_file.exists():
        template_file = Path("env.template")
        if template_file.exists():
            print("正在创建 .env 文件...")
            with open(template_file, 'r', encoding='utf-8') as f:
                content = f.read()
            with open(env_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print("✓ .env 文件已创建，请编辑其中的配置")
        else:
            print("⚠️  未找到 env.template 文件")
    
    return True

def main():
    """主函数"""
    print("🚀 智能体安装脚本")
    print("=" * 50)
    
    # 检查 Python 版本
    if not check_python_version():
        sys.exit(1)
    
    # 安装 Poetry
    if not install_poetry():
        sys.exit(1)
    
    # 设置环境
    if not setup_environment():
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 安装完成！")
    print("\n下一步:")
    print("1. 编辑 .env 文件，填入你的配置")
    print("2. 运行: poetry run python -m weight_loss_advisor.agent")
    print("\n详细说明请查看 SETUP_GUIDE.md")

if __name__ == "__main__":
    main()
