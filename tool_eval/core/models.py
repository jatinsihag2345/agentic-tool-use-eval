from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum


class ToolErrorType(str, Enum):
    INVALID_JSON = "invalid_json"
    UNKNOWN_TOOL = "unknown_tool"
    MISSING_REQUIRED_ARG = "missing_required_arg"
    ARGUMENT_TYPE_MISMATCH = "argument_type_mismatch"
    ARGUMENT_HALLUCINATION = "argument_hallucination"


@dataclass
class ToolParameter:
    name: str
    type_name: str  # "string", "integer", "number", "boolean", "array", "object"
    description: str
    required: bool = True
    enum_values: Optional[List[str]] = None


@dataclass
class ToolDefinition:
    name: str
    description: str
    parameters: List[ToolParameter]


@dataclass
class ToolCall:
    tool_name: str
    arguments: Dict[str, Any]
    call_id: Optional[str] = None


@dataclass
class ToolExecutionResult:
    call_id: Optional[str]
    success: bool
    output: Any
    error_type: Optional[ToolErrorType] = None
    error_message: Optional[str] = None


@dataclass
class MultiToolTask:
    id: str
    title: str
    instruction: str
    available_tools: List[str]
    expected_tool_sequence: List[str]
    ground_truth_output: str
