"""
Procurement Tool Functions

Real-world tool implementations for inventory, supplier quotes, orders, and notifications.
These functions would typically integrate with backend systems (databases, APIs, etc.).
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class InventoryItem:
    """Represents an inventory record."""

    name: str
    sku: str
    quantity: int
    unit_price: float


@dataclass
class SupplierQuote:
    """Represents a supplier's price quote."""

    supplier: str
    unit_price: float
    lead_time_days: int
    minimum_order: int


def check_inventory(product_name: str, quantity_needed: int) -> dict[str, Any]:
    """
    Check current inventory levels for a product.

    Args:
        product_name: Name of the product to check
        quantity_needed: Required quantity for the order

    Returns:
        Dictionary with availability status and current stock level.

    Real implementation would query a database or API.
    Here we mock some inventory data for demonstration.
    """
    # Mock inventory database
    inventory = {
        "Widget A": InventoryItem("Widget A", "SKU-001", 150, 25.50),
        "Sprocket B": InventoryItem("Sprocket B", "SKU-002", 45, 15.00),
        "Bearing C": InventoryItem("Bearing C", "SKU-003", 0, 12.75),
    }

    item = inventory.get(product_name)

    if not item:
        return {
            "available": False,
            "reason": f"Product '{product_name}' not found in inventory system",
        }

    if item.quantity >= quantity_needed:
        return {
            "available": True,
            "product": item.name,
            "sku": item.sku,
            "current_stock": item.quantity,
            "requested_qty": quantity_needed,
            "unit_price": item.unit_price,
        }
    else:
        return {
            "available": False,
            "product": item.name,
            "current_stock": item.quantity,
            "requested_qty": quantity_needed,
            "shortage": quantity_needed - item.quantity,
        }


def get_supplier_quotes(product_name: str, quantity: int) -> dict[str, Any]:
    """
    Fetch supplier quotes for a product.

    Args:
        product_name: Name of the product
        quantity: Desired order quantity

    Returns:
        Dictionary containing quotes from multiple suppliers with pricing and lead times.

    In production, this would call supplier APIs or a quotes database.
    """
    # Mock supplier database
    supplier_data = {
        "Widget A": [
            SupplierQuote("FastParts Co", 24.50, 3, 50),
            SupplierQuote("Global Supplies Inc", 23.75, 7, 100),
            SupplierQuote("Direct Manufacturing", 25.00, 1, 200),
        ],
        "Sprocket B": [
            SupplierQuote("Industrial Parts Ltd", 14.25, 5, 75),
            SupplierQuote("OEM Direct", 13.50, 10, 150),
        ],
    }

    quotes = supplier_data.get(product_name, [])

    if not quotes:
        return {
            "found": False,
            "product": product_name,
            "reason": "No suppliers available for this product",
        }

    # Filter quotes based on quantity requirements
    viable_quotes = [q for q in quotes if quantity >= q.minimum_order]

    if not viable_quotes:
        return {
            "found": False,
            "product": product_name,
            "reason": f"Requested quantity {quantity} below all minimum orders",
        }

    return {
        "found": True,
        "product": product_name,
        "requested_qty": quantity,
        "quotes": [
            {
                "supplier": q.supplier,
                "unit_price": q.unit_price,
                "total_cost": q.unit_price * quantity,
                "lead_time_days": q.lead_time_days,
                "minimum_order": q.minimum_order,
            }
            for q in viable_quotes
        ],
    }


def place_order(
    product_name: str, quantity: int, supplier: str, unit_price: float
) -> dict[str, Any]:
    """
    Place an order with a supplier.

    Args:
        product_name: Name of the product
        quantity: Order quantity
        supplier: Supplier name
        unit_price: Agreed unit price

    Returns:
        Dictionary with order confirmation details and tracking info.

    In production, this would create an order record in an ERP/database
    and potentially trigger supplier notifications.
    """
    # Generate a mock order ID (in production, this comes from database)
    import random

    order_id = f"PO-{random.randint(100000, 999999)}"

    return {
        "success": True,
        "order_id": order_id,
        "product": product_name,
        "quantity": quantity,
        "supplier": supplier,
        "unit_price": unit_price,
        "total_cost": quantity * unit_price,
        "status": "pending_confirmation",
        "notes": f"Order placed with {supplier}. Awaiting their confirmation.",
    }


def notify_team(
    message: str, recipients: list[str], priority: str = "normal"
) -> dict[str, Any]:
    """
    Send notifications to team members.

    Args:
        message: Notification message content
        recipients: List of team member emails or IDs
        priority: Priority level (low, normal, high, urgent)

    Returns:
        Dictionary confirming notification delivery.

    In production, this would integrate with email/Slack/Teams APIs.
    """
    valid_priorities = ["low", "normal", "high", "urgent"]
    if priority not in valid_priorities:
        return {
            "success": False,
            "error": f"Invalid priority. Must be one of {valid_priorities}",
        }

    if not recipients:
        return {
            "success": False,
            "error": "At least one recipient is required",
        }

    return {
        "success": True,
        "notification_id": f"NOTIF-{hash(message) % 100000}",
        "recipients_count": len(recipients),
        "recipients": recipients,
        "priority": priority,
        "message_preview": message[:100] + ("..." if len(message) > 100 else ""),
        "status": "sent",
    }
