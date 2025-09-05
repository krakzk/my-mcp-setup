from fastmcp import FastMCP

mcp = FastMCP("My mcp server")

@mcp.tool
def greet(name: str) -> str:
    """Greet user by name"""
    return f"Hello , {name}!"


@mcp.tool(
    name="Find Actor",
    description="Search characters and find the one played by the actor name passed",
    tags={"actors", "characters"},
    meta={"version": "1.1", "author":"krakz"}
)
def find_character(character: str) -> list[dict]:
    """Search characters and find the one played by the actor name passed"""
    print(f"Searching for actor who played character '{character}'")
    return [{"id": 1, "character":"Iron Man", "actor": "Robert Downey Junior"}]

if __name__ == "__main__":
    mcp.run()