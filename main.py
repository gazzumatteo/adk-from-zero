"""
Order Pipeline - Main Entry Point

Demonstrates multi-agent team coordination through a complete order workflow.
Run with: python main.py
"""

import os
from google.adk.session import InMemorySessionService
from agent import root_agent, sequential_pipeline, parallel_enrichment


def main() -> None:
    """
    Run the order orchestration pipeline.

    Demonstrates:
    - SequentialAgent for ordered tasks
    - ParallelAgent for concurrent work
    - LoopAgent for iterative quality checks
    """
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set. See .env.example")

    session_service = InMemorySessionService()
    session_id = "order-pipeline-001"

    print("\n" + "=" * 60)
    print("ACME MANUFACTURING - ORDER PROCESSING PIPELINE")
    print("=" * 60)
    print("\nMulti-Agent Team Orchestration")
    print("Sequential → Parallel → Loop Patterns\n")

    # Example order request
    sample_order = """
    Customer: TechCorp Industries
    Product: High-precision bearing assemblies
    Quantity: 500 units
    Delivery Required: 8 weeks
    Special Requirements: ISO 9001 certification, documentation required
    """

    print(f"Processing Order:{sample_order}\n")

    try:
        # Run the orchestrator pipeline
        response = root_agent.generate_content(
            f"Process this order request: {sample_order}",
            session=session_service.get_session(session_id),
        )

        print(f"Order Orchestrator Response:\n{response.text}\n")

        # Demonstrate the sequential pipeline
        print("\n" + "-" * 60)
        print("DEMONSTRATING SEQUENTIAL PIPELINE")
        print("-" * 60)

        seq_response = sequential_pipeline.generate_content(
            f"Process order for 500 bearing assemblies needed in 8 weeks.",
            session=session_service.get_session(f"{session_id}-seq"),
        )

        print(f"Sequential Pipeline Output:\n{seq_response.text}\n")

        # Demonstrate parallel enrichment
        print("\n" + "-" * 60)
        print("DEMONSTRATING PARALLEL ENRICHMENT")
        print("-" * 60)

        par_response = parallel_enrichment.generate_content(
            "Provide market and competitive analysis for bearing assemblies.",
            session=session_service.get_session(f"{session_id}-par"),
        )

        print(f"Parallel Enrichment Output:\n{par_response.text}\n")

    except Exception as e:
        print(f"Error: {e}")
        return

    # Interactive mode for additional orders
    print("\n" + "=" * 60)
    print("Interactive Mode - Process Additional Orders")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input("Enter order details (or 'quit' to exit): ").strip()

            if user_input.lower() in ("quit", "exit"):
                print("\nThank you for using Order Pipeline. Goodbye!")
                break

            if not user_input:
                continue

            response = root_agent.generate_content(
                user_input,
                session=session_service.get_session(session_id),
            )

            print(f"\nOrchestrator: {response.text}\n")

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
