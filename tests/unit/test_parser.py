"""Unit tests for parser functions."""

import pytest

from src.errors import (
    IncompleteExpressionError,
    InvalidNumberError,
    InvalidOperatorError,
)
from src.parser import parse_expression


# T034: Tests for negative number parsing (US3)
class TestParseNegativeNumbers:
    """Tests for parsing negative numbers."""

    def test_parse_negative_first_operand(self) -> None:
        """Test parsing negative first operand."""
        left, op, right = parse_expression(["-5", "+", "3"])
        assert left == -5.0
        assert op == "+"
        assert right == 3.0

    def test_parse_negative_second_operand(self) -> None:
        """Test parsing negative second operand."""
        left, op, right = parse_expression(["10", "+", "-4"])
        assert left == 10.0
        assert op == "+"
        assert right == -4.0

    def test_parse_double_negative(self) -> None:
        """Test parsing expression with double negative (10 - -4)."""
        left, op, right = parse_expression(["10", "-", "-4"])
        assert left == 10.0
        assert op == "-"
        assert right == -4.0

    def test_parse_both_negative(self) -> None:
        """Test parsing with both operands negative."""
        left, op, right = parse_expression(["-5", "*", "-3"])
        assert left == -5.0
        assert op == "*"
        assert right == -3.0


# T040: Tests for parser error handling (US4)
class TestParseErrors:
    """Tests for parser error handling."""

    def test_parse_invalid_number(self) -> None:
        """Test that invalid numbers raise InvalidNumberError."""
        with pytest.raises(InvalidNumberError) as exc_info:
            parse_expression(["abc", "+", "5"])
        assert "abc" in str(exc_info.value.message)

        with pytest.raises(InvalidNumberError) as exc_info:
            parse_expression(["5", "+", "xyz"])
        assert "xyz" in str(exc_info.value.message)

    def test_parse_invalid_operator(self) -> None:
        """Test that invalid operators raise InvalidOperatorError."""
        with pytest.raises(InvalidOperatorError) as exc_info:
            parse_expression(["5", "$", "3"])
        assert "$" in str(exc_info.value.message)

        with pytest.raises(InvalidOperatorError) as exc_info:
            parse_expression(["5", "plus", "3"])
        assert "plus" in str(exc_info.value.message)

    def test_parse_incomplete_expression(self) -> None:
        """Test that incomplete expressions raise IncompleteExpressionError."""
        with pytest.raises(IncompleteExpressionError):
            parse_expression(["5", "+"])

        with pytest.raises(IncompleteExpressionError):
            parse_expression(["5"])

        with pytest.raises(IncompleteExpressionError):
            parse_expression([])

        with pytest.raises(IncompleteExpressionError):
            parse_expression(["5", "+", "3", "4"])


# Tests for valid parsing
class TestParseValidExpressions:
    """Tests for parsing valid expressions."""

    def test_parse_integers(self) -> None:
        """Test parsing integer expressions."""
        left, op, right = parse_expression(["5", "+", "3"])
        assert left == 5.0
        assert op == "+"
        assert right == 3.0

    def test_parse_decimals(self) -> None:
        """Test parsing decimal expressions."""
        left, op, right = parse_expression(["3.5", "+", "2.5"])
        assert left == 3.5
        assert op == "+"
        assert right == 2.5

    def test_parse_all_operators(self) -> None:
        """Test parsing with all valid operators."""
        for op in ["+", "-", "*", "/"]:
            left, parsed_op, right = parse_expression(["1", op, "2"])
            assert parsed_op == op
