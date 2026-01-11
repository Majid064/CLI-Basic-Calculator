"""Core arithmetic operations for the calculator.

This module provides the fundamental arithmetic operations and the
Operator enumeration used throughout the calculator.
"""

from enum import Enum

from src.errors import DivisionByZeroError, InvalidOperatorError


class Operator(Enum):
    """Valid arithmetic operators."""

    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The difference of a and b (a - b).
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First operand.
        b: Second operand.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a: Dividend.
        b: Divisor.

    Returns:
        The quotient of a and b (a / b).

    Raises:
        DivisionByZeroError: If b is zero.
    """
    if b == 0:
        raise DivisionByZeroError()
    return a / b


def calculate(left: float, operator: str, right: float) -> float:
    """Perform a calculation with the given operator.

    Args:
        left: Left operand.
        operator: The arithmetic operator (+, -, *, /).
        right: Right operand.

    Returns:
        The result of the calculation.

    Raises:
        InvalidOperatorError: If the operator is not valid.
        DivisionByZeroError: If dividing by zero.
    """
    if operator == Operator.ADD.value:
        return add(left, right)
    elif operator == Operator.SUBTRACT.value:
        return subtract(left, right)
    elif operator == Operator.MULTIPLY.value:
        return multiply(left, right)
    elif operator == Operator.DIVIDE.value:
        return divide(left, right)
    else:
        raise InvalidOperatorError(operator)


def format_result(value: float) -> str:
    """Format a calculation result for display.

    Displays whole numbers without decimal point, decimals with full precision.

    Args:
        value: The numeric result to format.

    Returns:
        Formatted string representation of the value.
    """
    if value == int(value):
        return str(int(value))
    return str(value)
