import asyncio

from fastmcp import Client

client = Client("http://localhost:8010/mcp")


async def call_tool(a: float, b: float):
    async with client:
        result = await client.call_tool("add_two_numbers", {"a": a, "b": b})
        print(result)


# CallToolResult(content=[TextContent(type='text', text='11346', annotations=None, meta=None)], structured_content={'result': 11346}, meta=None, data=11346, is_error=False)

asyncio.run(call_tool(3456, 7890))
