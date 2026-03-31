"""
Customer Service Agent - Main Entry Point

Demonstrates session management and memory persistence.
Shows multi-turn conversations with state preservation.
Run with: python main.py
"""

import os
from google.adk.session import InMemorySessionService

from agent import root_agent
from services.session_config import SessionManager, get_session_service
from services.memory_config import get_memory_service, ContextBuilder


def run_customer_interaction(
    customer_email: str, session_manager: SessionManager, context_builder: ContextBuilder
) -> None:
    """
    Run a multi-turn customer service interaction.

    Args:
        customer_email: Customer email/identifier
        session_manager: Manages session state
        context_builder: Builds context from memory
    """
    # Get or create session for this customer
    session_id = session_manager.get_customer_session(customer_email)
    if not session_id:
        session_id = session_manager.create_customer_session(customer_email)

    session = session_manager.retrieve_session(session_id)

    # Simulate customer lookup and history retrieval
    # In production, these would be tool calls from the agent
    customer_info = {
        "name": "John Smith",
        "email": customer_email,
        "account_type": "premium",
        "registration_date": "2022-01-15",
        "total_orders": 12,
        "lifetime_value": 2450.50,
    }

    history = [
        {
            "date": "2024-03-10",
            "issue": "Shipping delay",
            "status": "resolved",
            "resolution_time_days": 5,
        },
        {
            "date": "2024-02-15",
            "issue": "Product defect",
            "status": "resolved",
            "resolution_time_days": 3,
        },
    ]

    # Build context using memory service
    context = context_builder.build_customer_context(
        customer_email, customer_info, history
    )

    print(f"\nSession ID: {session_id}")
    print(f"Customer: {customer_email}")
    print("-" * 60)

    # Multi-turn conversation loop
    turn = 1
    while True:
        print(f"\nTurn {turn}:")
        try:
            user_input = input("Customer: ").strip()

            if user_input.lower() in ("quit", "exit", "bye"):
                print("\nSupport Agent: Thank you for contacting us. Have a great day!")
                break

            if not user_input:
                continue

            # Prepare full prompt with context
            full_prompt = f"{context}\n\nCustomer message: {user_input}"

            # Get agent response (maintains session state)
            response = root_agent.generate_content(
                full_prompt,
                session=session,
            )

            print(f"\nSupport Agent: {response.text}")
            turn += 1

        except KeyboardInterrupt:
            print("\n\nSession interrupted.")
            break
        except Exception as e:
            print(f"\nError: {e}")


def main() -> None:
    """
    Run the customer service agent with memory and context.

    Demonstrates:
    - Session management for multi-turn conversations
    - Memory persistence across interactions
    - Context-aware agent behavior
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. See .env.example")

    # Initialize services
    session_service = get_session_service("memory")
    session_manager = SessionManager(session_service)

    memory_bank = get_memory_service("simple")
    context_builder = ContextBuilder(memory_bank)

    print("\n" + "=" * 60)
    print("ACME CUSTOMER SUPPORT - SESSION & MEMORY DEMO")
    print("=" * 60)
    print("\nDemonstrating:")
    print("- Session management for multi-turn conversations")
    print("- Memory persistence across interactions")
    print("- Context-aware support responses\n")

    # Demonstrate multi-turn conversation with first customer
    print("=" * 60)
    print("CUSTOMER SESSION 1: john@example.com")
    print("=" * 60)

    sample_issue_1 = """
    Hi, I'm having trouble with my recent order.
    The package arrived damaged and I need a replacement.
    """

    print(f"\nInitial Request:{sample_issue_1}\n")

    try:
        # Setup session for customer 1
        session_id_1 = session_manager.create_customer_session("john@example.com")
        session_1 = session_manager.retrieve_session(session_id_1)

        # Build context
        customer_info_1 = {
            "name": "John Smith",
            "account_type": "premium",
            "registration_date": "2022-01-15",
            "total_orders": 12,
            "lifetime_value": 2450.50,
        }
        history_1 = [
            {
                "date": "2024-03-10",
                "issue": "Shipping delay",
                "resolution_time_days": 5,
                "status": "resolved",
            }
        ]
        context_1 = context_builder.build_customer_context(
            "john@example.com", customer_info_1, history_1
        )

        # Get initial response
        response = root_agent.generate_content(
            f"{context_1}\n\nCustomer message: {sample_issue_1}",
            session=session_1,
        )

        print(f"Support Agent: {response.text}\n")

        # Demonstrate follow-up turn with same session
        print("-" * 60)
        print("FOLLOW-UP (Same Session - Context Preserved)")
        print("-" * 60)

        follow_up = "Yes, please create a ticket. I prefer expedited replacement."

        print(f"\nCustomer: {follow_up}\n")

        response_2 = root_agent.generate_content(
            follow_up,
            session=session_1,
        )

        print(f"Support Agent: {response_2.text}\n")

    except Exception as e:
        print(f"Error: {e}")
        return

    # Interactive mode for testing
    print("\n" + "=" * 60)
    print("INTERACTIVE MODE - Test Session Management")
    print("=" * 60 + "\n")

    while True:
        try:
            customer_email = input(
                "Enter customer email (or 'quit' to exit): "
            ).strip()

            if customer_email.lower() in ("quit", "exit"):
                print("\nThank you for using Customer Support System. Goodbye!")
                break

            if not customer_email:
                continue

            run_customer_interaction(customer_email, session_manager, context_builder)

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
