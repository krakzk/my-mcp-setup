from fastmcp import FastMCP

mcp = FastMCP("My mcp server")

@mcp.tool
def greet(name: str) -> str:
    """Greet user by name"""
    return f"Hello , {name}!"

@mcp.tool
def addNumbers(a: int, b: int) -> int:
    """Adds two numbers"""
    return a+b

@mcp.tool(
    name="Find character"
    description="Search characters and find the one played by the actor name passed"
    tags={"actors", "characters"}
    meta={"version": "1.1", "author":"krakz"}
)
def find_character(character: str) -> list[dict]:
    """Internal description, skipped as i specified above"""
    print(f"Searching for actor who played character '{character}'")
    return [{"id": 1, "character":"Iron Man", "actor": "Robert Downey Junior"}]

if __name__ == "__main__":
    mcp.run()