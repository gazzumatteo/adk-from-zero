"""
Agent templates for common agent roles.

Provides standard configurations that can be customized
for creating specialized agents.
"""

# Dictionary of agent templates by role
AGENT_TEMPLATES: dict[str, dict] = {
    "quality_monitor": {
        "capabilities": [
            "monitor_defect_rates",
            "analyze_quality_trends",
            "generate_alerts",
            "produce_reports",
        ],
        "tools": [
            "get_defect_metrics",
            "check_compliance",
            "generate_quality_report",
        ],
        "model": "gemini-3-flash-preview",
        "config": {
            "temperature": 0.5,
            "max_tokens": 2000,
            "alerts_enabled": True,
            "report_frequency": "daily",
        },
    },
    "data_analyst": {
        "capabilities": [
            "analyze_trends",
            "identify_patterns",
            "create_visualizations",
            "generate_insights",
        ],
        "tools": [
            "query_data",
            "calculate_statistics",
            "generate_charts",
            "create_reports",
        ],
        "model": "gemini-3.1-pro-preview",
        "config": {
            "temperature": 0.7,
            "max_tokens": 3000,
            "deep_analysis": True,
            "visualization_enabled": True,
        },
    },
    "customer_service": {
        "capabilities": [
            "handle_inquiries",
            "resolve_issues",
            "provide_support",
            "escalate_tickets",
        ],
        "tools": [
            "search_knowledge_base",
            "get_customer_history",
            "create_ticket",
            "update_ticket",
        ],
        "model": "gemini-3-flash-preview",
        "config": {
            "temperature": 0.6,
            "max_tokens": 1500,
            "escalation_threshold": 3,
            "response_style": "friendly",
        },
    },
    "inventory_manager": {
        "capabilities": [
            "track_inventory",
            "forecast_demand",
            "generate_orders",
            "monitor_stock_levels",
        ],
        "tools": [
            "get_inventory_levels",
            "forecast_demand",
            "check_suppliers",
            "generate_purchase_orders",
        ],
        "model": "gemini-3-flash-preview",
        "config": {
            "temperature": 0.4,
            "max_tokens": 2000,
            "reorder_point": 100,
            "forecast_period_days": 30,
        },
    },
}


def get_template(role: str) -> dict:
    """
    Get a template for a specific agent role.

    Args:
        role: Agent role name

    Returns:
        Template dictionary or empty dict if not found
    """
    return AGENT_TEMPLATES.get(role, {})


def list_available_roles() -> list[str]:
    """
    List all available agent template roles.

    Returns:
        List of role names
    """
    return list(AGENT_TEMPLATES.keys())


def customize_template(role: str, customizations: dict) -> dict:
    """
    Customize a template with specific settings.

    Args:
        role: Agent role
        customizations: Dictionary of customizations

    Returns:
        Customized template dictionary
    """
    template = get_template(role)

    if not template:
        return customizations

    # Merge customizations with template
    result = template.copy()

    # Update config with customizations
    if "config" in result:
        result["config"].update(customizations.get("config", {}))

    # Update other fields
    for key, value in customizations.items():
        if key != "config":
            result[key] = value

    return result
