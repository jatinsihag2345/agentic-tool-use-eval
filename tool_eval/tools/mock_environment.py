from typing import List, Dict, Any
from ..core.models import ToolDefinition, ToolParameter


TOOL_SQL = ToolDefinition(
    name="sql_query",
    description="Executes a read-only SQL query against the internal database.",
    parameters=[
        ToolParameter(name="query", type_name="string", description="SQL SELECT query"),
        ToolParameter(name="database", type_name="string", description="Database name, e.g. 'analytics' or 'users'")
    ]
)

TOOL_CALCULATOR = ToolDefinition(
    name="calculator",
    description="Evaluates a mathematical arithmetic expression.",
    parameters=[
        ToolParameter(name="expression", type_name="string", description="Arithmetic expression e.g. '(120 * 4) / 3'")
    ]
)

TOOL_FILESYSTEM = ToolDefinition(
    name="read_file",
    description="Reads file contents from the sandbox storage.",
    parameters=[
        ToolParameter(name="path", type_name="string", description="Relative file path"),
        ToolParameter(name="max_bytes", type_name="integer", description="Maximum bytes to read", required=False)
    ]
)

TOOL_WEATHER = ToolDefinition(
    name="get_weather",
    description="Fetches current meteorological data for a designated city.",
    parameters=[
        ToolParameter(name="city", type_name="string", description="Target city name"),
        ToolParameter(name="unit", type_name="string", description="Temperature unit", required=False, enum_values=["celsius", "fahrenheit"])
    ]
)

STANDARD_TOOLS: List[ToolDefinition] = [
    TOOL_SQL,
    TOOL_CALCULATOR,
    TOOL_FILESYSTEM,
    TOOL_WEATHER
]
