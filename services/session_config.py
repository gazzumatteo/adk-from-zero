"""
Session Service Configuration

Demonstrates session management for multi-turn conversations.
Sessions maintain conversation state and context across interactions.
"""

from google.adk.session import InMemorySessionService
from typing import Optional


def get_session_service(service_type: str = "memory") -> object:
    """
    Factory function to get appropriate session service.

    Args:
        service_type: Type of session service
                     'memory': InMemorySessionService for development
                     'vertex': VertexAiSessionService for production

    Returns:
        Configured session service instance

    Session services handle:
    - Conversation state management
    - Message history tracking
    - Context preservation across turns
    - Session lifecycle (create, get, delete)
    """
    if service_type == "memory":
        # In-memory session storage (suitable for development/testing)
        # Good for demonstrations but loses data on restart
        return InMemorySessionService()

    elif service_type == "vertex":
        # Production-grade session service backed by Vertex AI
        # Persists sessions across application restarts
        # Requires Google Cloud credentials
        try:
            from google.adk.session import VertexAiSessionService

            return VertexAiSessionService()
        except ImportError:
            raise ImportError(
                "VertexAiSessionService requires additional dependencies. "
                "Install: pip install google-cloud-aiplatform"
            )

    else:
        raise ValueError(f"Unknown session service type: {service_type}")


class SessionManager:
    """
    Manages session lifecycle and context for customer support.

    Tracks:
    - Customer identity
    - Issue context
    - Conversation history
    - Ticket references
    """

    def __init__(self, session_service: object):
        """
        Initialize session manager with a session service.

        Args:
            session_service: Session service instance (memory or Vertex)
        """
        self.session_service = session_service
        self.active_sessions = {}

    def create_customer_session(self, customer_id: str) -> str:
        """
        Create a new session for a customer.

        Args:
            customer_id: Unique customer identifier

        Returns:
            Session ID for this customer's conversation

        Sessions are keyed by customer ID to maintain continuity.
        """
        session_id = f"session-{customer_id}-{len(self.active_sessions)}"
        session = self.session_service.get_session(session_id)
        self.active_sessions[customer_id] = session_id
        return session_id

    def get_customer_session(self, customer_id: str) -> Optional[str]:
        """
        Get existing session for a customer.

        Args:
            customer_id: Customer identifier

        Returns:
            Existing session ID if found, None otherwise

        Allows resuming previous conversations with same customer.
        """
        return self.active_sessions.get(customer_id)

    def retrieve_session(self, session_id: str):
        """
        Retrieve session object from service.

        Args:
            session_id: Session identifier

        Returns:
            Session object maintaining conversation state
        """
        return self.session_service.get_session(session_id)
