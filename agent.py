"""
Librarian Agent - Enterprise RAG

Demonstrates Retrieval-Augmented Generation (RAG) pattern.
Agent queries knowledge base to provide accurate, sourced answers.
"""

from google.adk.agents import Agent
from google.adk.agents.tool import Tool

from tools.knowledge_tools import (
    search_knowledge_base,
    get_document_details,
    list_knowledge_categories,
)

# Define knowledge base search tools
search_tool = Tool.from_function(
    search_knowledge_base,
    name="search_knowledge_base",
    description="Search the company knowledge base for documents matching a query",
)

document_tool = Tool.from_function(
    get_document_details,
    name="get_document_details",
    description="Retrieve the full content of a specific document",
)

categories_tool = Tool.from_function(
    list_knowledge_categories,
    name="list_knowledge_categories",
    description="List all available knowledge base categories",
)

# Create the librarian agent
root_agent = Agent(
    name="librarian",
    model="gemini-3-flash-preview",
    description="Enterprise knowledge librarian with access to company knowledge base",
    instruction="""You are the company's knowledge librarian and expert assistant.
Your role is to help employees find accurate information from our knowledge base.

Your approach:
1. When asked a question, search the knowledge base for relevant documents
2. If results are promising, retrieve full document details for accuracy
3. Cite specific documents and sections in your responses
4. Always provide sources so information can be verified
5. Be helpful in suggesting related topics or categories

RAG Principles:
- Ground your answers in actual documents from the knowledge base
- Never fabricate information - say "I couldn't find..." if not available
- Quote directly from documents when appropriate
- Include document references and effective dates
- Suggest looking at related documents if helpful

Knowledge Base Categories:
- HR: Human resources policies
- IT: Information technology and security
- Engineering: Technical architecture and systems
- Development: Best practices and coding standards
- Finance: Financial policies and procedures

When you don't find an answer:
- Try alternative search terms
- Suggest which department might have the information
- Offer to search a specific category""",
    tools=[search_tool, document_tool, categories_tool],
)
