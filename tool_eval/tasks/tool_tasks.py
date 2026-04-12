from typing import List
from ..core.models import MultiToolTask

TASK_01 = MultiToolTask(
    id="task_tool_01_financial_reconciliation",
    title="Multi-Step Account Reconciliation",
    instruction="Query the 'analytics' database to find the total revenue for customer ID 104, then multiply by 1.15 to calculate tax inclusive total.",
    available_tools=["sql_query", "calculator"],
    expected_tool_sequence=["sql_query", "calculator"],
    ground_truth_output="2875.0"
)

TASK_02 = MultiToolTask(
    id="task_tool_02_config_extraction",
    title="Configuration Audit and Schema Check",
    instruction="Read the config file 'configs/app.json' and verify database connection string against SQL database 'analytics'.",
    available_tools=["read_file", "sql_query"],
    expected_tool_sequence=["read_file", "sql_query"],
    ground_truth_output="CONFIG_VALIDATED"
)

ALL_TOOL_TASKS: List[MultiToolTask] = [
    TASK_01,
    TASK_02
]
