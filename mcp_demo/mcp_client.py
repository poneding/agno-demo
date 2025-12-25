import asyncio

from fastmcp import Client

client = Client("http://localhost:8000/mcp")


async def call_tool(a: float, b: float):
    async with client:
        result = await client.call_tool("add", {"a": a, "b": b})
        print(result)


# CallToolResult(content=[TextContent(type='text', text='3456.0 + 7890.0 = 11346.0', annotations=None, meta=None)], structured_content={'result': '3456.0 + 7890.0 = 11346.0'}, meta=None, data='3456.0 + 7890.0 = 11346.0', is_error=False)


asyncio.run(call_tool(3456, 7890))
