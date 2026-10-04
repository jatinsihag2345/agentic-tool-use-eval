from typing import Dict, Any, List, Tuple, Optional


class NestedSchemaValidator:
    """
    Validates deeply nested parameter structures in complex function calls
    (e.g., database filters, nested configuration objects).
    """

    @staticmethod
    def validate_nested_dict(payload: Any, expected_keys: List[str]) -> Tuple[bool, Optional[str]]:
        if not isinstance(payload, dict):
            return False, f"Expected dictionary payload, got {type(payload).__name__}"
        for k in expected_keys:
            if k not in payload:
                return False, f"Missing required nested key '{k}'"
        return True, None

    @staticmethod
    def validate_array_of_strings(items: Any) -> Tuple[bool, Optional[str]]:
        if not isinstance(items, list):
            return False, f"Expected list payload, got {type(items).__name__}"
        for idx, item in enumerate(items):
            if not isinstance(item, str):
                return False, f"Item at index {idx} must be a string"
        return True, None
