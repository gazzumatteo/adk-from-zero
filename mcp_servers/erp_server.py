"""
Custom MCP server for ERP system using FastMCP.

Exposes three main tools:
- get_catalog(category) - Retrieve products by category
- check_availability(product_id) - Check stock availability
- request_quote(product_id, quantity) - Generate product quote
"""

from typing import Any

from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("ERP System")


# Mock data for demonstration
PRODUCTS_DB: dict[str, dict[str, Any]] = {
    "LAPTOP-001": {
        "id": "LAPTOP-001",
        "name": "ProBook 15",
        "category": "electronics",
        "price": 1299.99,
        "stock": 42,
    },
    "LAPTOP-002": {
        "id": "LAPTOP-002",
        "name": "UltraBook X1",
        "category": "electronics",
        "price": 1899.99,
        "stock": 15,
    },
    "MONITOR-001": {
        "id": "MONITOR-001",
        "name": "4K DisplayPro",
        "category": "electronics",
        "price": 599.99,
        "stock": 28,
    },
    "DESK-001": {
        "id": "DESK-001",
        "name": "Standing Desk Pro",
        "category": "furniture",
        "price": 899.99,
        "stock": 8,
    },
    "CHAIR-001": {
        "id": "CHAIR-001",
        "name": "Ergonomic Chair",
        "category": "furniture",
        "price": 499.99,
        "stock": 35,
    },
}


@mcp.tool()
def get_catalog(category: str) -> dict[str, Any]:
    """
    Get product catalog for a specific category.

    Args:
        category: Product category to retrieve (e.g., 'electronics', 'furniture')

    Returns:
        Dictionary with products matching the category
    """
    matching_products = {
        product_id: product
        for product_id, product in PRODUCTS_DB.items()
        if product["category"].lower() == category.lower()
    }

    if not matching_products:
        return {
            "status": "not_found",
            "message": f"No products found in category '{category}'",
            "products": [],
        }

    return {
        "status": "success",
        "category": category,
        "count": len(matching_products),
        "products": matching_products,
    }


@mcp.tool()
def check_availability(product_id: str) -> dict[str, Any]:
    """
    Check stock availability for a specific product.

    Args:
        product_id: The product ID to check

    Returns:
        Dictionary with availability status and stock level
    """
    if product_id not in PRODUCTS_DB:
        return {
            "status": "not_found",
            "message": f"Product '{product_id}' not found in catalog",
            "product_id": product_id,
        }

    product = PRODUCTS_DB[product_id]

    return {
        "status": "success",
        "product_id": product_id,
        "product_name": product["name"],
        "in_stock": product["stock"] > 0,
        "available_quantity": product["stock"],
        "price": product["price"],
    }


@mcp.tool()
def request_quote(product_id: str, quantity: int) -> dict[str, Any]:
    """
    Request a price quote for a specific product and quantity.

    Args:
        product_id: The product ID to quote
        quantity: Number of units requested

    Returns:
        Dictionary with quote details including total price and availability
    """
    if product_id not in PRODUCTS_DB:
        return {
            "status": "not_found",
            "message": f"Product '{product_id}' not found",
            "product_id": product_id,
        }

    product = PRODUCTS_DB[product_id]

    # Check if sufficient stock available
    has_stock = quantity <= product["stock"]

    # Calculate total with 10% bulk discount for orders > 5
    unit_price = product["price"]
    if quantity > 5:
        unit_price *= 0.9

    total_price = unit_price * quantity

    return {
        "status": "success",
        "product_id": product_id,
        "product_name": product["name"],
        "requested_quantity": quantity,
        "unit_price": product["price"],
        "discounted_unit_price": unit_price if quantity > 5 else product["price"],
        "total_price": total_price,
        "available_quantity": product["stock"],
        "can_fulfill": has_stock,
        "lead_time_days": 3 if has_stock else 10,
        "quote_valid_until": "2026-04-21",
    }


if __name__ == "__main__":
    # Run the MCP server on stdio
    mcp.run()
