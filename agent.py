"""
Agent using McpToolset with filesystem and custom MCP servers.

This agent demonstrates:
- Integration with MCP servers via McpToolset
- Stdio-based connection to local MCP servers
- Using multiple MCP tools in a single agent
"""

import json
import os
from typing import Any

from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams


def create_mcp_agent() -> Agent:
    """
    Create an agent with MCP tools from filesystem and custom ERP server.

    Returns:
        Agent: Configured agent with MCP toolset integrated
    """
    # Initialize base agent
    agent = Agent(
        name="MCP-Integration-Agent",
        model="gemini-3-flash-preview",
    )

    # Create McpToolset with filesystem MCP server (built-in)
    filesystem_tools = McpToolset(
        name="filesystem",
        connection_params=StdioConnectionParams(
            command="mcp-server-filesystem",
            args=["--allowed-directories", os.path.expanduser("~")],
        ),
    )

    # Create McpToolset with custom ERP MCP server
    # Note: In production, ensure the MCP server is running separately
    erp_tools = McpToolset(
        name="erp",
        connection_params=StdioConnectionParams(
            command="python",
            args=["-m", "mcp_servers.erp_server"],
        ),
    )

    # Add both toolsets to the agent
    agent.add_tools(filesystem_tools)
    agent.add_tools(erp_tools)

    return agent


def main() -> None:
    """
    Run the MCP-integrated agent with example query.
    """
    agent = create_mcp_agent()

    # Example: Query combining filesystem and ERP tools
    prompt = """
    Please help me:
    1. Check the ERP catalog for 'electronics' products
    2. Check availability for product 'LAPTOP-001'
    3. Create a summary document in the home directory with findings

    Use the available MCP tools to complete these tasks.
    """

    print("Starting MCP Integration Agent...")
    print("-" * 60)
    print(f"Prompt: {prompt}\n")

    response = agent.run(prompt)

    print("-" * 60)
    print(f"Response:\n{response}")


if __name__ == "__main__":
    main()
