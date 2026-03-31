"""
Customer Service Tool Functions

Tools for looking up customer information, complaint history, and ticket creation.
These tools maintain state and context across multiple interactions.
"""

from typing import Any
from datetime import datetime, timedelta


def lookup_customer(customer_email: str | customer_id: str) -> dict[str, Any]:
    """
    Look up customer information by email or ID.

    Args:
        customer_email: Customer email address (alternative to customer_id)
        customer_id: Customer ID (alternative to customer_email)

    Returns:
        Dictionary with customer details including account history and status.

    This tool is typically called early in support interactions to build context.
    """
    # Mock customer database
    customers = {
        "john@example.com": {
            "id": "CUST-001",
            "name": "John Smith",
            "email": "john@example.com",
            "account_type": "premium",
            "registration_date": "2022-01-15",
            "total_orders": 12,
            "lifetime_value": 2450.50,
            "account_status": "active",
            "preferred_contact": "email",
        },
        "CUST-001": {
            "id": "CUST-001",
            "name": "John Smith",
            "email": "john@example.com",
            "account_type": "premium",
            "registration_date": "2022-01-15",
            "total_orders": 12,
            "lifetime_value": 2450.50,
            "account_status": "active",
            "preferred_contact": "email",
        },
        "sarah@example.com": {
            "id": "CUST-002",
            "name": "Sarah Johnson",
            "email": "sarah@example.com",
            "account_type": "standard",
            "registration_date": "2023-06-22",
            "total_orders": 3,
            "lifetime_value": 285.00,
            "account_status": "active",
            "preferred_contact": "phone",
        },
    }

    # Look up by email or ID
    key = customer_email or customer_id
    customer = customers.get(key)

    if not customer:
        return {
            "found": False,
            "error": f"Customer not found: {key}",
        }

    return {
        "found": True,
        "customer": customer,
    }


def get_complaint_history(customer_id: str, limit: int = 10) -> dict[str, Any]:
    """
    Retrieve complaint and ticket history for a customer.

    Args:
        customer_id: Customer ID
        limit: Maximum number of records to return

    Returns:
        Dictionary containing previous complaints and their resolutions.

    This provides crucial context for handling recurring issues.
    """
    # Mock complaint history database
    complaint_history = {
        "CUST-001": [
            {
                "ticket_id": "TKT-1005",
                "date": "2024-03-10",
                "issue": "Shipping delay",
                "status": "resolved",
                "resolution": "Refunded shipping cost",
                "resolution_time_days": 5,
            },
            {
                "ticket_id": "TKT-1004",
                "date": "2024-02-15",
                "issue": "Product defect",
                "status": "resolved",
                "resolution": "Sent replacement",
                "resolution_time_days": 3,
            },
            {
                "ticket_id": "TKT-1003",
                "date": "2024-01-20",
                "issue": "Wrong item received",
                "status": "resolved",
                "resolution": "Swapped order",
                "resolution_time_days": 2,
            },
        ],
        "CUST-002": [
            {
                "ticket_id": "TKT-2001",
                "date": "2024-03-05",
                "issue": "Billing inquiry",
                "status": "resolved",
                "resolution": "Clarified charges",
                "resolution_time_days": 1,
            },
        ],
    }

    history = complaint_history.get(customer_id, [])

    return {
        "customer_id": customer_id,
        "total_complaints": len(history),
        "complaints": history[:limit],
        "recent_issue_pattern": "shipping delays" if len(history) > 2 else None,
    }


def create_ticket(
    customer_id: str,
    issue_type: str,
    description: str,
    priority: str = "normal",
    requested_resolution: str | None = None,
) -> dict[str, Any]:
    """
    Create a new support ticket for a customer.

    Args:
        customer_id: Customer ID
        issue_type: Category of issue (shipping, product, billing, etc.)
        description: Detailed description of the problem
        priority: Priority level (low, normal, high, urgent)
        requested_resolution: Customer's suggested resolution

    Returns:
        Dictionary with ticket confirmation and tracking information.

    This creates a persistent record for follow-up and resolution tracking.
    """
    valid_types = ["shipping", "product", "billing", "technical", "general"]
    valid_priorities = ["low", "normal", "high", "urgent"]

    # Validate inputs
    if issue_type not in valid_types:
        return {
            "success": False,
            "error": f"Invalid issue type. Must be one of {valid_types}",
        }

    if priority not in valid_priorities:
        return {
            "success": False,
            "error": f"Invalid priority. Must be one of {valid_priorities}",
        }

    # Generate ticket ID
    import random

    ticket_id = f"TKT-{random.randint(100000, 999999)}"
    created_date = datetime.now().isoformat()

    # Set expected resolution time based on priority
    resolution_days = {
        "low": 14,
        "normal": 7,
        "high": 2,
        "urgent": 1,
    }

    expected_resolution = (
        datetime.now() + timedelta(days=resolution_days[priority])
    ).isoformat()

    return {
        "success": True,
        "ticket_id": ticket_id,
        "customer_id": customer_id,
        "issue_type": issue_type,
        "priority": priority,
        "status": "open",
        "created_date": created_date,
        "expected_resolution_date": expected_resolution,
        "assigned_to": "support_queue",
        "description_summary": description[:100] + ("..." if len(description) > 100 else ""),
        "requested_resolution": requested_resolution,
        "next_steps": f"Ticket {ticket_id} created. A support specialist will review and contact you within 24 hours.",
    }
