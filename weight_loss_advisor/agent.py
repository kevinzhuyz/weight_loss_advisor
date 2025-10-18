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

"""Weight Loss Coordinator: provide comprehensive weight loss guidance"""

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.health_assessor.agent import health_assessor_agent
from .sub_agents.nutritionist.agent import nutritionist_agent
from .sub_agents.fitness_coach.agent import fitness_coach_agent
from .sub_agents.progress_tracker.agent import progress_tracker_agent

MODEL = "gemini-2.5-pro"


weight_loss_coordinator = LlmAgent(
    name="weight_loss_coordinator",
    model=MODEL,
    description=(
        "guide users through a structured process to receive comprehensive weight loss "
        "advice by orchestrating a series of expert subagents. help them assess their "
        "current health status, develop personalized nutrition plans, create exercise "
        "routines, and track their progress towards their weight loss goals."
    ),
    instruction=prompt.WEIGHT_LOSS_COORDINATOR_PROMPT,
    output_key="weight_loss_coordinator_output",
    tools=[
        AgentTool(agent=health_assessor_agent),
        AgentTool(agent=nutritionist_agent),
        AgentTool(agent=fitness_coach_agent),
        AgentTool(agent=progress_tracker_agent),
    ],
)


root_agent = weight_loss_coordinator
