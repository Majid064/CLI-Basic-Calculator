"""Unit tests for calculator operations."""

import pytest

from src.calculator import add, calculate, divide, format_result, multiply, subtract
from src.errors import DivisionByZeroError


# T012: Tests for add function
class TestAdd:
    """Tests for the add function."""

    def test_add_positive_integers(self) -> None:
        """Test adding two positive integers."""
        assert add(5, 3) == 8
        assert add(10, 20) == 30

    def test_add_with_zero(self) -> None:
        """Test adding with zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5
        assert add(0, 0) == 0


# T013: Tests for subtract function
class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_integers(self) -> None:
        """Test subtracting two positive integers."""
        assert subtract(10, 4) == 6
        assert subtract(20, 5) == 15

    def test_subtract_to_negative(self) -> None:
        """Test subtraction resulting in negative."""
        assert subtract(5, 10) == -5
        assert subtract(0, 5) == -5


# T014: Tests for multiply function
class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_integers(self) -> None:
        """Test multiplying two positive integers."""
        assert multiply(6, 7) == 42
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self) -> None:
        """Test multiplication by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0


# T015: Tests for divide function
class TestDivide:
    """Tests for the divide function."""

    def test_divide_even(self) -> None:
        """Test division with even result."""
        assert divide(20, 4) == 5
        assert divide(100, 10) == 10

    def test_divide_integer_result(self) -> None:
        """Test division resulting in integer."""
        assert divide(9, 3) == 3
        assert divide(8, 2) == 4

    def test_divide_by_zero_raises_error(self) -> None:
        """Test that division by zero raises DivisionByZeroError."""
        with pytest.raises(DivisionByZeroError):
            divide(10, 0)


# T027: Tests for decimal operations (US2)
class TestDecimalOperations:
    """Tests for decimal number operations."""

    def test_add_decimals(self) -> None:
        """Test adding decimal numbers."""
        assert add(3.5, 2.5) == 6.0
        assert add(1.1, 2.2) == pytest.approx(3.3)

    def test_subtract_decimals(self) -> None:
        """Test subtracting decimal numbers."""
        assert subtract(5.5, 2.5) == 3.0
        assert subtract(10.0, 3.3) == pytest.approx(6.7)

    def test_multiply_decimals(self) -> None:
        """Test multiplying decimal numbers."""
        assert multiply(2.5, 4.0) == 10.0
        assert multiply(1.5, 2.0) == 3.0

    def test_divide_decimals(self) -> None:
        """Test dividing decimal numbers."""
        assert divide(10.0, 4.0) == 2.5
        assert divide(7.5, 2.5) == 3.0


# T028: Test for floating point precision (US2)
class TestFloatingPointPrecision:
    """Tests for floating-point precision handling."""

    def test_floating_point_precision(self) -> None:
        """Test 0.1 + 0.2 precision behavior."""
        result = add(0.1, 0.2)
        # Python floats have known precision issues
        # Result is approximately 0.3 but may be 0.30000000000000004
        assert result == pytest.approx(0.3, rel=1e-9)


# Tests for calculate dispatcher
class TestCalculate:
    """Tests for the calculate dispatcher function."""

    def test_calculate_addition(self) -> None:
        """Test calculate with addition operator."""
        assert calculate(5, "+", 3) == 8

    def test_calculate_subtraction(self) -> None:
        """Test calculate with subtraction operator."""
        assert calculate(10, "-", 4) == 6

    def test_calculate_multiplication(self) -> None:
        """Test calculate with multiplication operator."""
        assert calculate(6, "*", 7) == 42

    def test_calculate_division(self) -> None:
        """Test calculate with division operator."""
        assert calculate(20, "/", 4) == 5


# Tests for format_result
class TestFormatResult:
    """Tests for the format_result function."""

    def test_format_whole_number(self) -> None:
        """Test formatting whole numbers without decimal."""
        assert format_result(8.0) == "8"
        assert format_result(42.0) == "42"
        assert format_result(-5.0) == "-5"

    def test_format_decimal_number(self) -> None:
        """Test formatting decimal numbers."""
        assert format_result(2.5) == "2.5"
        assert format_result(3.14159) == "3.14159"

    def test_format_zero(self) -> None:
        """Test formatting zero."""
        assert format_result(0.0) == "0"


# T033: Tests for negative number operations (US3)
class TestNegativeOperations:
    """Tests for negative number operations."""

    def test_add_negative(self) -> None:
        """Test adding with negative numbers."""
        assert add(-5, 3) == -2
        assert add(5, -3) == 2
        assert add(-5, -3) == -8

    def test_subtract_negative_from_positive(self) -> None:
        """Test subtracting negative from positive (double negative)."""
        assert subtract(10, -4) == 14
        assert subtract(5, -5) == 10

    def test_multiply_negatives(self) -> None:
        """Test multiplying negative numbers."""
        assert multiply(-6, 7) == -42
        assert multiply(6, -7) == -42
        assert multiply(-6, -7) == 42

    def test_divide_negative(self) -> None:
        """Test dividing with negative numbers."""
        assert divide(-20, 4) == -5
        assert divide(20, -4) == -5
        assert divide(-20, -4) == 5
