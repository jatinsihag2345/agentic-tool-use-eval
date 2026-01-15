from typing import Dict, Any, List, Optional, Tuple
from .models import ToolDefinition, ToolCall, ToolErrorType


class ToolCallValidator:
    """
    Validates model generated tool calls against JSON function schemas.
    Flags argument hallucinations, missing parameters, and type errors.
    """

    def __init__(self, tools: List[ToolDefinition]):
        self.tool_map: Dict[str, ToolDefinition] = {t.name: t for t in tools}

    def validate_call(self, call: ToolCall) -> Tuple[bool, Optional[ToolErrorType], Optional[str]]:
        if call.tool_name not in self.tool_map:
            return False, ToolErrorType.UNKNOWN_TOOL, f"Tool '{call.tool_name}' is not in available tools."

        tool_def = self.tool_map[call.tool_name]
        param_map = {p.name: p for p in tool_def.parameters}

        # 1. Check for missing required arguments
        for p in tool_def.parameters:
            if p.required and p.name not in call.arguments:
                return False, ToolErrorType.MISSING_REQUIRED_ARG, f"Missing required parameter '{p.name}'"

        # 2. Check for argument hallucinations (keys not present in schema)
        for arg_name, arg_val in call.arguments.items():
            if arg_name not in param_map:
                return False, ToolErrorType.ARGUMENT_HALLUCINATION, f"Argument '{arg_name}' does not exist in tool schema"

            # 3. Type check
            p = param_map[arg_name]
            if p.type_name == "string" and not isinstance(arg_val, str):
                return False, ToolErrorType.ARGUMENT_TYPE_MISMATCH, f"Parameter '{arg_name}' must be string"
            elif p.type_name == "integer" and not isinstance(arg_val, int):
                return False, ToolErrorType.ARGUMENT_TYPE_MISMATCH, f"Parameter '{arg_name}' must be integer"
            elif p.type_name == "number" and not isinstance(arg_val, (int, float)):
                return False, ToolErrorType.ARGUMENT_TYPE_MISMATCH, f"Parameter '{arg_name}' must be number"
            elif p.type_name == "boolean" and not isinstance(arg_val, bool):
                return False, ToolErrorType.ARGUMENT_TYPE_MISMATCH, f"Parameter '{arg_name}' must be boolean"
            elif p.type_name == "array" and not isinstance(arg_val, list):
                return False, ToolErrorType.ARGUMENT_TYPE_MISMATCH, f"Parameter '{arg_name}' must be array"

            # 4. Enum validation
            if p.enum_values and arg_val not in p.enum_values:
                return False, ToolErrorType.ARGUMENT_TYPE_MISMATCH, f"Value '{arg_val}' not in allowed enum {p.enum_values}"

        return True, None, None
