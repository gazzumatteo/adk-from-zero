"""
Procurement Agent - Main Entry Point

Demonstrates tool usage and callback hooks in action.
Run with: python main.py
"""

import os
from google.adk.session import InMemorySessionService
from agent import root_agent


def main() -> None:
    """
    Run the procurement agent in an interactive CLI loop.

    Uses tools for inventory checks, supplier quotes, order placement,
    and team notifications.
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. See .env.example")

    session_service = InMemorySessionService()
    session_id = "procurement-session-001"

    print("\n" + "=" * 60)
    print("ACME MANUFACTURING - PROCUREMENT AGENT")
    print("=" * 60)
    print("\nWelcome! I'm your procurement specialist.")
    print("I can check inventory, get supplier quotes, place orders,")
    print("and notify the team. Type 'quit' to exit.\n")

    # Example procurement request
    example_request = """
    We need 75 units of Sprocket B urgently.
    Please check if we have stock internally, and if not,
    get supplier quotes and recommend the best option.
    """

    print(f"Example Request: {example_request.strip()}")
    print("\nProcessing...\n")

    try:
        response = root_agent.generate_content(
            example_request,
            session=session_service.get_session(session_id),
        )

        print(f"\nAgent Response:\n{response.text}\n")

    except Exception as e:
        print(f"Error: {e}")
        return

    # Interactive loop for additional requests
    while True:
        try:
            user_input = input("\nYour request: ").strip()

            if user_input.lower() in ("quit", "exit", "bye"):
                print("\nThank you for using the Procurement Agent. Goodbye!")
                break

            if not user_input:
                continue

            response = root_agent.generate_content(
                user_input,
                session=session_service.get_session(session_id),
            )

            print(f"\nAgent: {response.text}")

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
