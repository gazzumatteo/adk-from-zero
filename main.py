"""
Enterprise RAG - Main Entry Point

Demonstrates Retrieval-Augmented Generation with knowledge base search.
Run with: python main.py
"""

import os
from google.adk.session import InMemorySessionService

from agent import root_agent


def main() -> None:
    """
    Run the librarian agent with knowledge base search.

    Demonstrates:
    - Retrieval-Augmented Generation (RAG) pattern
    - Knowledge base search and retrieval
    - Source attribution and citations
    - Multi-turn knowledge exploration
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. See .env.example")

    session_service = InMemorySessionService()
    session_id = "librarian-session-001"

    print("\n" + "=" * 60)
    print("ACME COMPANY - KNOWLEDGE LIBRARIAN")
    print("=" * 60)
    print("\nEnterprise RAG with Knowledge Base Search")
    print("Ask questions about company policies, procedures, and best practices.\n")

    # Example queries showing RAG in action
    example_queries = [
        {
            "query": "What is our remote work policy?",
            "context": "HR/Policy Question",
        },
        {
            "query": "Can you explain our system architecture?",
            "context": "Technical Documentation",
        },
    ]

    # Demonstrate RAG with example queries
    print("=" * 60)
    print("DEMONSTRATING KNOWLEDGE BASE SEARCH")
    print("=" * 60)

    for i, example in enumerate(example_queries, 1):
        print(f"\nExample {i}: {example['context']}")
        print(f"Question: {example['query']}\n")

        try:
            response = root_agent.generate_content(
                example["query"],
                session=session_service.get_session(session_id),
            )

            print(f"Librarian:\n{response.text}\n")
            print("-" * 60)

        except Exception as e:
            print(f"Error: {e}")
            continue

    # Interactive mode
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE - Ask the Librarian")
    print("=" * 60)
    print("\nSample questions you can ask:")
    print("- What is the remote work policy?")
    print("- What are the data security requirements?")
    print("- What's our system architecture?")
    print("- What are the code review guidelines?")
    print("- What knowledge categories are available?\n")

    while True:
        try:
            user_query = input("Your question: ").strip()

            if user_query.lower() in ("quit", "exit", "bye"):
                print(
                    "\nThank you for using the Knowledge Librarian. Have a great day!"
                )
                break

            if not user_query:
                continue

            # Query the librarian
            response = root_agent.generate_content(
                user_query,
                session=session_service.get_session(session_id),
            )

            print(f"\nLibrarian:\n{response.text}\n")

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try another question.\n")


if __name__ == "__main__":
    main()
