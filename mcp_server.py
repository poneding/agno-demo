from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")


@mcp.tool
def add_two_numbers(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The sum of the two numbers.
    """
    print(f"Adding {a} and {b}")
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="localhost", port=8010)
