"""
Receptionist Agent - Main Entry Point

Demonstrates basic agent interaction with InMemorySessionService.
Run with: python main.py
"""

import os
from typing import Optional

from google.adk.session import InMemorySessionService

from agent import root_agent


def main() -> None:
    """
    Run the receptionist agent in an interactive CLI loop.

    Uses InMemorySessionService to maintain conversation state.
    Each user input is processed and agent response is printed.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. See .env.example")

    # Initialize session service to track conversation state
    session_service = InMemorySessionService()

    # Create a new conversation session
    session_id = "receptionist-session-001"

    print("\n" + "=" * 60)
    print("ACME MANUFACTURING - RECEPTIONIST AGENT")
    print("=" * 60)
    print("\nWelcome! Chat with our receptionist agent.")
    print("Type 'quit' or 'exit' to end the conversation.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            # Exit on user request
            if user_input.lower() in ("quit", "exit", "bye"):
                print("\nReceptionist: Thank you for visiting Acme Manufacturing. Have a great day!")
                break

            # Skip empty inputs
            if not user_input:
                continue

            # Process user message through the agent
            # The agent handles understanding the input and generating appropriate response
            response = root_agent.generate_content(
                user_input,
                session=session_service.get_session(session_id),
            )

            print(f"\nReceptionist: {response.text}\n")

        except KeyboardInterrupt:
            print("\n\nConversation interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
