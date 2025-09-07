from fastmcp import FastMCP
import json 
import requests

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
    name="find_actor",
    description="Search characters and find the one played by the actor name passed",
    tags={"actors", "characters"},
    meta={"version": "1.1", "author":"krakz"}
)
def find_actor_for_character(character: str) -> list[dict]:
    """Search characters and find the one played by the actor name passed"""
    print(f"Searching for actor who played character '{character}'")
    return [{"id": 1, "character":"Iron Man", "actor": "Robert Downey Junior"}]

@mcp.tool()
def list_doctors(state:str) -> str:
    """This tool returns doctors that may be near you.
    Args:
        state: the two letter state code that you live in. 
        Example payload: "CA"

    Returns:
        str: a list of doctors that may be near you
        Example Response "{"DOC001":{"name":"Dr John James", "specialty":"Cardiology"...}...}" 
        """
    
    url = 'https://raw.githubusercontent.com/nicknochnack/ACPWalkthrough/refs/heads/main/doctors.json'
    resp = requests.get(url)
    doctors = json.loads(resp.text)

    matches = [doctor for doctor in doctors.values() if doctor['address']['state'] == state]    
    return str(matches) 

if __name__ == "__main__":
    mcp.run(transport="http")