"""Custom error types for the calculator.

This module defines the error hierarchy used throughout the calculator
for handling invalid inputs and computation errors.
"""


class CalculatorError(Exception):
    """Base class for all calculator-specific errors.

    Attributes:
        message: User-friendly error message.
        input_value: Optional problematic input that caused the error.
    """

    def __init__(self, message: str, input_value: str | None = None) -> None:
        self.message = message
        self.input_value = input_value
        super().__init__(message)


class DivisionByZeroError(CalculatorError):
    """Raised when division by zero is attempted."""

    def __init__(self) -> None:
        super().__init__("Error: Cannot divide by zero")


class InvalidNumberError(CalculatorError):
    """Raised when a non-numeric input is provided."""

    def __init__(self, value: str) -> None:
        super().__init__(f"Error: '{value}' is not a valid number", value)


class InvalidOperatorError(CalculatorError):
    """Raised when an invalid operator is used."""

    def __init__(self, operator: str) -> None:
        super().__init__(
            f"Error: '{operator}' is not a valid operator. Use +, -, *, /", operator
        )


class IncompleteExpressionError(CalculatorError):
    """Raised when the expression has wrong number of tokens."""

    def __init__(self) -> None:
        super().__init__(
            "Error: Incomplete expression. Format: <number> <operator> <number>"
        )
