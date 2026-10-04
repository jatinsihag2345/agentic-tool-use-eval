from typing import List, Dict, Set, Any


class ToolDependencyDAGValidator:
    """
    Validates that a sequence or parallel batch of tool calls satisfies causal data dependency constraints.
    """

    def __init__(self):
        pass

    def validate_execution_order(self, calls: List[Dict[str, Any]], dependencies: Dict[str, List[str]]) -> bool:
        executed_calls: Set[str] = set()

        for call in calls:
            call_id = call.get("call_id")
            required_deps = dependencies.get(call_id, [])

            for dep in required_deps:
                if dep not in executed_calls:
                    return False
            executed_calls.add(call_id)

        return True
