import sys
import argparse
from .tools.mock_environment import STANDARD_TOOLS
from .core.models import ToolCall
from .core.validator import ToolCallValidator


def test_validator():
    validator = ToolCallValidator(STANDARD_TOOLS)

    # Valid call
    c_valid = ToolCall(tool_name="sql_query", arguments={"query": "SELECT * FROM users;", "database": "analytics"})
    ok, err_type, msg = validator.validate_call(c_valid)
    assert ok is True, f"Failed on valid call: {msg}"

    # Invalid call: missing required parameter 'database'
    c_missing = ToolCall(tool_name="sql_query", arguments={"query": "SELECT 1;"})
    ok, err_type, msg = validator.validate_call(c_missing)
    assert ok is False, "Did not catch missing argument"

    # Invalid call: argument hallucination
    c_hallu = ToolCall(tool_name="calculator", arguments={"expression": "2+2", "precision": 4})
    ok, err_type, msg = validator.validate_call(c_hallu)
    assert ok is False, "Did not catch argument hallucination"

    print("\nRunning ToolCallValidator Verification:")
    print("=" * 65)
    print(" -> Valid Call:          Validated successfully")
    print(" -> Missing Arg Caught:  Validated successfully")
    print(" -> Hallucination Caught: Validated successfully")
    print("=" * 65)
    print("All tool validator checks passed!\n")


def main():
    parser = argparse.ArgumentParser(description="Agentic Tool Use Eval CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("test", help="Verify tool validator logic")

    args = parser.parse_args()
    if args.command == "test":
        test_validator()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
