from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Ciao")

@mcp.tool()
def greeting(name: str) -> str:
    "Sends a greeting"
    return f"Ciao, {name}!"

if __name__ == "__main__":
    mcp.run(transport='streamable-http')