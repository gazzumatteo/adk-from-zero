"""
Agent connecting to remote MCP server via HTTP.

This demonstrates:
- Connecting to MCP servers running on different machines
- StreamableHTTPServerParams for remote connections
- Resilience and error handling for remote tools
"""

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams


def create_remote_mcp_agent(erp_server_url: str = "http://localhost:8000") -> Agent:
    """
    Create an agent connecting to remote MCP servers.

    Args:
        erp_server_url: URL of the remote ERP MCP server

    Returns:
        Agent: Configured agent with remote MCP toolset
    """
    agent = Agent(
        name="Remote-MCP-Agent",
        model="gemini-3-flash-preview",
    )

    # Connect to remote ERP server via HTTP
    remote_erp_tools = McpToolset(
        name="remote_erp",
        connection_params=StreamableHTTPServerParams(
            url=erp_server_url,
            timeout=30,
        ),
    )

    agent.add_tools(remote_erp_tools)

    return agent


def main() -> None:
    """
    Run the remote MCP-integrated agent.
    """
    agent = create_remote_mcp_agent()

    prompt = """
    Please check the ERP system and:
    1. List all electronics products available
    2. Find the most expensive item
    3. Request a quote for 10 units of the cheapest item

    Use the remote ERP tools to complete this request.
    """

    print("Starting Remote MCP Agent...")
    print("-" * 60)
    print(f"Prompt: {prompt}\n")

    try:
        response = agent.run(prompt)
        print("-" * 60)
        print(f"Response:\n{response}")
    except ConnectionError as e:
        print(f"Error: Could not connect to MCP server: {e}")
        print("Make sure the remote MCP server is running at the specified URL.")


if __name__ == "__main__":
    main()
