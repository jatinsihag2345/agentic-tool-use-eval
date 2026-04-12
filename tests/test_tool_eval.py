from tool_eval.core.models import ToolCall, ToolErrorType
from tool_eval.core.validator import ToolCallValidator
from tool_eval.tools.mock_environment import STANDARD_TOOLS


def test_tool_validator_type_mismatch():
    validator = ToolCallValidator(STANDARD_TOOLS)
    call = ToolCall(tool_name="read_file", arguments={"path": 12345})  # Should be string
    ok, err_type, msg = validator.validate_call(call)
    assert ok is False
    assert err_type == ToolErrorType.ARGUMENT_TYPE_MISMATCH


def test_unknown_tool():
    validator = ToolCallValidator(STANDARD_TOOLS)
    call = ToolCall(tool_name="non_existent_tool", arguments={})
    ok, err_type, msg = validator.validate_call(call)
    assert ok is False
    assert err_type == ToolErrorType.UNKNOWN_TOOL
