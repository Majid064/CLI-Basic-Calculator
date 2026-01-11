"""Unit tests for error classes."""

from src.errors import (
    CalculatorError,
    DivisionByZeroError,
    IncompleteExpressionError,
    InvalidNumberError,
    InvalidOperatorError,
)


# T039: Tests for error classes (US4)
class TestDivisionByZeroError:
    """Tests for DivisionByZeroError."""

    def test_division_by_zero_error_message(self) -> None:
        """Test that DivisionByZeroError has correct message."""
        error = DivisionByZeroError()
        assert error.message == "Error: Cannot divide by zero"
        assert str(error) == "Error: Cannot divide by zero"

    def test_division_by_zero_is_calculator_error(self) -> None:
        """Test that DivisionByZeroError inherits from CalculatorError."""
        error = DivisionByZeroError()
        assert isinstance(error, CalculatorError)


class TestInvalidNumberError:
    """Tests for InvalidNumberError."""

    def test_invalid_number_error_message(self) -> None:
        """Test that InvalidNumberError has correct message."""
        error = InvalidNumberError("abc")
        assert error.message == "Error: 'abc' is not a valid number"
        assert error.input_value == "abc"

    def test_invalid_number_preserves_input(self) -> None:
        """Test that InvalidNumberError preserves the invalid input."""
        error = InvalidNumberError("xyz123")
        assert error.input_value == "xyz123"
        assert "xyz123" in error.message


class TestInvalidOperatorError:
    """Tests for InvalidOperatorError."""

    def test_invalid_operator_error_message(self) -> None:
        """Test that InvalidOperatorError has correct message."""
        error = InvalidOperatorError("$")
        assert "not a valid operator" in error.message
        assert "$" in error.message
        assert "Use +, -, *, /" in error.message

    def test_invalid_operator_preserves_input(self) -> None:
        """Test that InvalidOperatorError preserves the invalid operator."""
        error = InvalidOperatorError("plus")
        assert error.input_value == "plus"


class TestIncompleteExpressionError:
    """Tests for IncompleteExpressionError."""

    def test_incomplete_expression_error_message(self) -> None:
        """Test that IncompleteExpressionError has correct message."""
        error = IncompleteExpressionError()
        assert "Incomplete expression" in error.message
        assert "<number> <operator> <number>" in error.message

    def test_incomplete_expression_is_calculator_error(self) -> None:
        """Test that IncompleteExpressionError inherits from CalculatorError."""
        error = IncompleteExpressionError()
        assert isinstance(error, CalculatorError)
