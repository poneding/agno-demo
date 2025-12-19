from fastmcp import FastMCP

mcp = FastMCP("数学计算 MCP 服务")


@mcp.tool(description="加法计算")
def add(a: float, b: float) -> str:
    print(f"Adding {a} and {b}")
    result = a + b
    return f"{a} + {b} = {result}"


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
