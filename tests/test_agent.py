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

"""Test script for weight loss advisor agent"""

import asyncio
from weight_loss_advisor.agent import root_agent


async def test_weight_loss_advisor():
    """Test the weight loss advisor agent with sample input"""
    
    # Sample user input
    user_input = """
    我想开始减肥，请帮我制定一个全面的减肥计划。
    
    我的基本信息：
    - 身高：165厘米
    - 当前体重：70公斤
    - 目标体重：60公斤
    - 年龄：28岁
    - 性别：女性
    - 运动经验：初学者
    - 每周可用于运动的时间：3-4次，每次1小时
    - 饮食偏好：无特殊限制，但希望健康均衡
    - 预算：中等预算
    """
    
    try:
        # Run the agent
        result = await root_agent.run(user_input)
        print("减肥咨询智能体测试结果：")
        print("=" * 50)
        print(result)
        
    except Exception as e:
        print(f"测试过程中出现错误：{e}")


if __name__ == "__main__":
    asyncio.run(test_weight_loss_advisor())
