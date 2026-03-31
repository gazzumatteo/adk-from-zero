"""
Pydantic models for A2UI components.

Defines the structure for various UI components that the agent
can generate as structured output.
"""

from typing import Any, Optional

from pydantic import BaseModel, Field


class UIComponent(BaseModel):
    """Base class for all UI components."""

    type: str
    id: str
    title: Optional[str] = None


class KPI(UIComponent):
    """Key Performance Indicator component."""

    type: str = "kpi"
    label: str
    value: str | int | float
    unit: Optional[str] = None
    trend: Optional[str] = Field(None, description="up, down, or stable")
    change_percent: Optional[float] = None


class Card(UIComponent):
    """Generic card component for content display."""

    type: str = "card"
    content: str
    metadata: dict[str, Any] = Field(default_factory=dict)


class Table(UIComponent):
    """Table component for structured data."""

    type: str = "table"
    headers: list[str]
    rows: list[list[str | int | float]]
    sortable: bool = False
    paginated: bool = False
    items_per_page: int = 10


class Chart(UIComponent):
    """Chart component for data visualization."""

    type: str = "chart"
    chart_type: str = Field(description="bar, line, pie, area")
    data_points: list[dict[str, Any]]
    x_axis: str
    y_axis: str
    colors: Optional[list[str]] = None


class Form(UIComponent):
    """Form component for user input."""

    type: str = "form"
    fields: list[dict[str, Any]]
    submit_label: str = "Submit"
    cancel_label: Optional[str] = None


class DashboardLayout(BaseModel):
    """Complete dashboard layout structure."""

    title: str
    description: Optional[str] = None
    components: list[KPI | Card | Table | Chart | Form] = Field(
        default_factory=list,
        discriminator="type",
    )
    layout_grid: Optional[dict[str, Any]] = None
    theme: Optional[str] = "light"
    refresh_interval: Optional[int] = None


class UIBlueprint(BaseModel):
    """Top-level UI blueprint that an agent generates."""

    version: str = "1.0.0"
    title: str
    description: str
    dashboard: DashboardLayout
    metadata: dict[str, Any] = Field(default_factory=dict)
