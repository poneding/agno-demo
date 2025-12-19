import asyncio
import os
import sys

from agno.agent import Agent
from agno.utils.pprint import apprint_run_response

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from llm.openai_like import model

# 添加项目根目录到Python路径


agent = Agent(
    model=model,
)


async def streaming():
    async for response in agent.arun(input="给我讲个笑话", stream=True):
        print(response.content, end="", flush=True)


async def streaming_print():
    await agent.aprint_response(input="给我讲个笑话", stream=True)


async def streaming_pprint():
    await apprint_run_response(agent.arun(input="给我讲个笑话", stream=True))


asyncio.run(streaming_pprint())
