"""Input parsing and validation for the calculator.

This module handles parsing command-line arguments into a structured
expression that can be evaluated by the calculator.
"""

from src.calculator import Operator
from src.errors import (
    IncompleteExpressionError,
    InvalidNumberError,
    InvalidOperatorError,
)

VALID_OPERATORS = {op.value for op in Operator}


def parse_expression(args: list[str]) -> tuple[float, str, float]:
    """Parse command-line arguments into an expression.

    Args:
        args: List of command-line arguments (expected: [number, operator, number]).

    Returns:
        A tuple of (left_operand, operator, right_operand).

    Raises:
        IncompleteExpressionError: If wrong number of arguments.
        InvalidNumberError: If operand is not a valid number.
        InvalidOperatorError: If operator is not valid.
    """
    if len(args) != 3:
        raise IncompleteExpressionError()

    left_str, operator, right_str = args

    # Validate operator
    if operator not in VALID_OPERATORS:
        raise InvalidOperatorError(operator)

    # Parse left operand
    try:
        left = float(left_str)
    except ValueError:
        raise InvalidNumberError(left_str)

    # Parse right operand
    try:
        right = float(right_str)
    except ValueError:
        raise InvalidNumberError(right_str)

    return left, operator, right
