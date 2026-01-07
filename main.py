import asyncio
import os
from textwrap import dedent
from typing import Any

from agno.agent import Agent, RunOutput
from agno.db.sqlite import SqliteDb
from agno.models.dashscope import DashScope
from agno.models.lmstudio import LMStudio
from agno.models.openai import OpenAILike
from agno.run import RunContext
from agno.run.agent import RunInput
from agno.tools.mcp import MCPTools
from agno.utils.pprint import pprint_run_response

from llm import model


def sum_numbers(a: int, b: int) -> int:
    """
    Returns the sum of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The sum of the two numbers.
    """

    print(f"Summing {a} and {b}")
    return a + b


# llm = DashScope(
#     id="qwen3-max-preview",
#     base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
#     api_key="sk-31934c0e504d41869faee7d128e8cb7e",
# )


def pre_hook_example(run_context: RunContext) -> None:
    print("Running pre-hook to add dependencies to context...")
    dependencies = run_context.dependencies

    if not dependencies:
        dependencies = {}
    dependencies["num1"] = 123456
    dependencies["num2"] = 654321
    run_context.dependencies = dependencies


# Create the Agent
# agno_agent = Agent(
#     name="Calculation Agent",
#     description="An agent that can perform basic calculations and store results in a database.",
#     model=llm,
#     # Add a database to the Agent
#     db=SqliteDb(db_file="agno.db"),
#     # Add the Agno MCP server to the Agent
#     # tools=[sum_numbers],
#     tools=[MCPTools(url="http://localhost:8010/mcp", transport="streamable-http")],
#     # dependencies={
#     #     "num1": 234324,
#     #     "num2": 4325435,
#     # },
#     add_dependencies_to_context=True,
#     # Add the previous session history to the context
#     add_history_to_context=True,
#     markdown=True,
#     pre_hooks=[pre_hook_example],
#     debug_mode=True,
#     debug_level=2,
# )


# # Run agent and return the response as a variable
# response: RunOutput = agno_agent.run(
#     "使用 add_two_numbers 工具计算 {num1} 和 {num2} 两数之和，并将结果存入数据库。"
# )

# # Print the response in markdown format
# pprint_run_response(response, markdown=True)


async def run_agent(message: str) -> None:
    """Run the agent with the given message."""

    mcp_tools = MCPTools(
        url="http://localhost:8010/mcp",
        transport="streamable-http",
    )
    await mcp_tools.connect()

    try:
        agent = Agent(
            model=model,
            # tools=[mcp_tools],
            tools=[sum_numbers],
            instructions=dedent(
                """You are a calculation agent that can perform basic arithmetic operations using the provided tools."""
            ),
            markdown=True,
            pre_hooks=[pre_hook_example],
            debug_mode=True,
            debug_level=2,
        )

        # Run the agent
        await agent.aprint_response(message, stream=True)
    finally:
        # Always close the connection when done
        await mcp_tools.close()


# Example usage
if __name__ == "__main__":
    # Basic example - exploring project license
    asyncio.run(run_agent("calculate the sum of {num1} and {num2}."))
