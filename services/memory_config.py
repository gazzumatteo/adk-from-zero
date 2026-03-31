"""
Memory and Context Configuration

Demonstrates memory services for persistent context in conversations.
Memory banks store and retrieve relevant information across sessions.
"""

from typing import Optional, Any


class SimpleMemoryBank:
    """
    Simple in-memory storage for conversation context.

    Useful for development and demonstration purposes.
    Production systems would use persistent backends.
    """

    def __init__(self):
        """Initialize empty memory storage."""
        self.memory = {}

    def store(self, customer_id: str, key: str, value: Any) -> None:
        """
        Store a key-value pair in memory.

        Args:
            customer_id: Customer identifier
            key: Memory key
            value: Value to store
        """
        if customer_id not in self.memory:
            self.memory[customer_id] = {}
        self.memory[customer_id][key] = value

    def retrieve(self, customer_id: str, key: str) -> Optional[Any]:
        """
        Retrieve a value from memory.

        Args:
            customer_id: Customer identifier
            key: Memory key

        Returns:
            Stored value or None if not found
        """
        return self.memory.get(customer_id, {}).get(key)

    def get_context(self, customer_id: str) -> dict:
        """
        Get all stored context for a customer.

        Args:
            customer_id: Customer identifier

        Returns:
            Dictionary of all stored context
        """
        return self.memory.get(customer_id, {})


def get_memory_service(service_type: str = "simple") -> object:
    """
    Factory function to get memory service.

    Args:
        service_type: Type of memory service
                     'simple': In-memory storage
                     'vertex': Vertex AI Memory Bank (production)

    Returns:
        Configured memory service instance

    Memory services handle:
    - Storing conversation context
    - Retrieving customer history
    - Building contextual understanding
    - Long-term information retention
    """
    if service_type == "simple":
        return SimpleMemoryBank()

    elif service_type == "vertex":
        # Production-grade memory backed by Vertex AI
        # Provides semantic search and context retrieval
        try:
            from google.adk.memory import VertexAiMemoryBankService

            return VertexAiMemoryBankService()
        except ImportError:
            raise ImportError(
                "VertexAiMemoryBankService requires additional dependencies. "
                "Install: pip install google-cloud-aiplatform"
            )

    else:
        raise ValueError(f"Unknown memory service type: {service_type}")


class ContextBuilder:
    """
    Builds rich context from memories for agent interactions.

    Aggregates relevant information from:
    - Customer profile
    - Complaint history
    - Ticket references
    - Previous resolutions
    """

    def __init__(self, memory_bank: object):
        """
        Initialize context builder.

        Args:
            memory_bank: Memory service for retrieving stored context
        """
        self.memory_bank = memory_bank

    def build_customer_context(
        self, customer_id: str, customer_info: dict, history: list
    ) -> str:
        """
        Build a comprehensive context string for the agent.

        Args:
            customer_id: Customer identifier
            customer_info: Customer profile information
            history: Customer's complaint/ticket history

        Returns:
            Formatted context string for agent instructions

        This context is provided to the agent to inform decision-making.
        """
        # Store relevant info for later retrieval
        self.memory_bank.store(customer_id, "profile", customer_info)
        self.memory_bank.store(customer_id, "history", history)

        # Build context string
        context = f"""
CUSTOMER CONTEXT FOR {customer_id}:

Profile:
- Name: {customer_info.get('name')}
- Account Type: {customer_info.get('account_type')}
- Customer Since: {customer_info.get('registration_date')}
- Total Orders: {customer_info.get('total_orders')}
- Lifetime Value: ${customer_info.get('lifetime_value')}

Previous Issues: {len(history)}
{self._format_history(history)}

Context for current interaction:
- Review customer history for patterns
- Apply lessons from previous resolutions
- Prioritize long-term customer satisfaction
- Offer proactive solutions when appropriate
"""
        return context

    def _format_history(self, history: list) -> str:
        """Format history for readable display."""
        if not history:
            return "- No previous issues"

        formatted = []
        for issue in history[:3]:  # Show last 3 issues
            formatted.append(
                f"- {issue['date']}: {issue['issue']} "
                f"({issue['status']}, resolved in {issue['resolution_time_days']} days)"
            )
        return "\n".join(formatted)
