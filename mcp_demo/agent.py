from agno.agent import Agent
from agno.tools.mcp import MCPTools

from llm.lm_studio import model


async def main():
    calc_mp = MCPTools(transport="streamable-http", url="http://localhost:8000/mcp")
    await calc_mp.connect()

    agent = Agent(
        model=model,
        tools=[calc_mp],
        instructions="调用mcp工具进行计算。",
        markdown=True,
    )

    # Run agent and return the response as a variable
    await agent.aprint_response("计算3456加7890的结果。")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
