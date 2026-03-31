"""
Dashboard tools for retrieving operational metrics.

These tools provide data that the agent uses to generate UI blueprints.
"""

from datetime import datetime, timedelta
from typing import Any


def get_kpi_data() -> dict[str, Any]:
    """
    Get key performance indicators for the dashboard.

    Returns:
        Dictionary with current KPI metrics
    """
    return {
        "revenue_today": 45230.50,
        "revenue_today_change": 12.5,
        "orders_today": 342,
        "orders_today_change": 8.2,
        "customers_online": 1247,
        "avg_order_value": 132.25,
        "conversion_rate": 3.45,
        "conversion_change": -0.5,
    }


def get_production_metrics() -> dict[str, Any]:
    """
    Get production and operational metrics.

    Returns:
        Dictionary with production data
    """
    now = datetime.now()
    hourly_data = []

    for hour in range(24):
        timestamp = (now - timedelta(hours=hour)).strftime("%H:00")
        value = 85 + (hour % 8) * 3  # Vary between 85-109
        hourly_data.append({"hour": timestamp, "throughput": value})

    return {
        "current_efficiency": 94.2,
        "machine_uptime": 98.5,
        "defect_rate": 0.8,
        "production_queue": 234,
        "hourly_throughput": list(reversed(hourly_data)),
    }


def get_order_backlog() -> dict[str, Any]:
    """
    Get current order backlog and status breakdown.

    Returns:
        Dictionary with order backlog data
    """
    return {
        "total_backlog": 1247,
        "status_breakdown": {
            "pending": 324,
            "processing": 412,
            "ready_to_ship": 289,
            "shipped": 222,
        },
        "high_priority": 45,
        "overdue": 12,
        "average_age_hours": 18.5,
        "orders_by_region": {
            "North America": 467,
            "Europe": 389,
            "Asia Pacific": 291,
            "Other": 100,
        },
    }


def get_customer_satisfaction() -> dict[str, Any]:
    """
    Get customer satisfaction metrics.

    Returns:
        Dictionary with satisfaction data
    """
    return {
        "nps_score": 72,
        "nps_change": 3.2,
        "customer_satisfaction": 4.6,
        "satisfaction_scale": 5.0,
        "support_response_time": 2.3,
        "response_time_unit": "hours",
        "issue_resolution_rate": 96.8,
    }
