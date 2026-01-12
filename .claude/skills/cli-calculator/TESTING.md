# Testing Guide

Complete test cases and validation for the CLI Calculator.

## Test Structure

```
tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_calculator.py    # Core operation tests
│   ├── test_parser.py        # Parser validation tests
│   └── test_errors.py        # Exception class tests
└── integration/
    ├── __init__.py
    └── test_cli.py           # End-to-end CLI tests
```

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/unit/test_calculator.py

# Run specific test class
uv run pytest tests/unit/test_calculator.py::TestAdd

# Run with coverage
uv run pytest --cov=src
```

## Unit Tests

### test_calculator.py

```python
"""Unit tests for calculator operations."""

import pytest
from src.calculator import add, subtract, multiply, divide, calculate, format_result
from src.errors import DivisionByZeroError, InvalidOperatorError


class TestAdd:
    """Tests for add function."""

    def test_add_positive_integers(self) -> None:
        assert add(2, 3) == 5

    def test_add_with_zero(self) -> None:
        assert add(5, 0) == 5

    def test_add_negative_numbers(self) -> None:
        assert add(-2, -3) == -5

    def test_add_mixed_signs(self) -> None:
        assert add(-5, 3) == -2


class TestSubtract:
    """Tests for subtract function."""

    def test_subtract_positive_integers(self) -> None:
        assert subtract(10, 4) == 6

    def test_subtract_to_negative(self) -> None:
        assert subtract(3, 10) == -7

    def test_subtract_negative_from_positive(self) -> None:
        assert subtract(5, -3) == 8


class TestMultiply:
    """Tests for multiply function."""

    def test_multiply_positive_integers(self) -> None:
        assert multiply(6, 7) == 42

    def test_multiply_by_zero(self) -> None:
        assert multiply(100, 0) == 0

    def test_multiply_negatives(self) -> None:
        assert multiply(-3, -4) == 12

    def test_multiply_mixed_signs(self) -> None:
        assert multiply(-5, 3) == -15


class TestDivide:
    """Tests for divide function."""

    def test_divide_even(self) -> None:
        assert divide(10, 2) == 5

    def test_divide_with_remainder(self) -> None:
        assert divide(10, 3) == pytest.approx(3.333333, rel=1e-5)

    def test_divide_by_zero_raises_error(self) -> None:
        with pytest.raises(DivisionByZeroError):
            divide(10, 0)

    def test_divide_negative(self) -> None:
        assert divide(-10, 2) == -5


class TestDecimalOperations:
    """Tests for decimal number support."""

    def test_add_decimals(self) -> None:
        assert add(3.5, 2.5) == 6.0

    def test_subtract_decimals(self) -> None:
        assert subtract(5.5, 2.3) == pytest.approx(3.2, rel=1e-9)

    def test_multiply_decimals(self) -> None:
        assert multiply(2.5, 4.0) == 10.0

    def test_divide_decimals(self) -> None:
        assert divide(7.5, 2.5) == 3.0


class TestCalculate:
    """Tests for calculate dispatcher."""

    def test_calculate_addition(self) -> None:
        assert calculate(5, "+", 3) == 8

    def test_calculate_subtraction(self) -> None:
        assert calculate(10, "-", 4) == 6

    def test_calculate_multiplication(self) -> None:
        assert calculate(6, "*", 7) == 42

    def test_calculate_division(self) -> None:
        assert calculate(20, "/", 4) == 5

    def test_calculate_invalid_operator(self) -> None:
        with pytest.raises(InvalidOperatorError):
            calculate(5, "%", 3)


class TestFormatResult:
    """Tests for result formatting."""

    def test_format_whole_number(self) -> None:
        assert format_result(8.0) == "8"

    def test_format_decimal_number(self) -> None:
        assert format_result(3.5) == "3.5"

    def test_format_zero(self) -> None:
        assert format_result(0.0) == "0"

    def test_format_negative_whole(self) -> None:
        assert format_result(-5.0) == "-5"

    def test_format_negative_decimal(self) -> None:
        assert format_result(-3.14) == "-3.14"
```

### test_parser.py

```python
"""Unit tests for expression parser."""

import pytest
from src.parser import parse_expression
from src.errors import (
    IncompleteExpressionError,
    InvalidNumberError,
    InvalidOperatorError,
)


class TestParseValidExpressions:
    """Tests for valid expression parsing."""

    def test_parse_integers(self) -> None:
        left, op, right = parse_expression(["5", "+", "3"])
        assert left == 5.0
        assert op == "+"
        assert right == 3.0

    def test_parse_decimals(self) -> None:
        left, op, right = parse_expression(["3.5", "+", "2.5"])
        assert left == 3.5
        assert op == "+"
        assert right == 2.5

    def test_parse_all_operators(self) -> None:
        for op in ["+", "-", "*", "/"]:
            left, parsed_op, right = parse_expression(["10", op, "5"])
            assert parsed_op == op


class TestParseNegativeNumbers:
    """Tests for negative number parsing."""

    def test_parse_negative_first_operand(self) -> None:
        left, op, right = parse_expression(["-5", "+", "3"])
        assert left == -5.0

    def test_parse_negative_second_operand(self) -> None:
        left, op, right = parse_expression(["5", "+", "-3"])
        assert right == -3.0

    def test_parse_both_negative(self) -> None:
        left, op, right = parse_expression(["-5", "+", "-3"])
        assert left == -5.0
        assert right == -3.0

    def test_parse_negative_decimal(self) -> None:
        left, op, right = parse_expression(["-3.14", "*", "2"])
        assert left == -3.14


class TestParseErrors:
    """Tests for parser error handling."""

    def test_parse_incomplete_expression_no_args(self) -> None:
        with pytest.raises(IncompleteExpressionError):
            parse_expression([])

    def test_parse_incomplete_expression_one_arg(self) -> None:
        with pytest.raises(IncompleteExpressionError):
            parse_expression(["5"])

    def test_parse_incomplete_expression_two_args(self) -> None:
        with pytest.raises(IncompleteExpressionError):
            parse_expression(["5", "+"])

    def test_parse_too_many_args(self) -> None:
        with pytest.raises(IncompleteExpressionError):
            parse_expression(["5", "+", "3", "+", "2"])

    def test_parse_invalid_first_number(self) -> None:
        with pytest.raises(InvalidNumberError) as exc_info:
            parse_expression(["abc", "+", "5"])
        assert exc_info.value.input_value == "abc"

    def test_parse_invalid_second_number(self) -> None:
        with pytest.raises(InvalidNumberError) as exc_info:
            parse_expression(["5", "+", "xyz"])
        assert exc_info.value.input_value == "xyz"

    def test_parse_invalid_operator(self) -> None:
        with pytest.raises(InvalidOperatorError) as exc_info:
            parse_expression(["5", "%", "3"])
        assert exc_info.value.input_value == "%"
```

### test_errors.py

```python
"""Unit tests for custom exception classes."""

import pytest
from src.errors import (
    CalculatorError,
    DivisionByZeroError,
    InvalidNumberError,
    InvalidOperatorError,
    IncompleteExpressionError,
)


class TestCalculatorError:
    """Tests for base CalculatorError."""

    def test_calculator_error_message(self) -> None:
        error = CalculatorError("Test message", "test_input")
        assert error.message == "Test message"
        assert error.input_value == "test_input"

    def test_calculator_error_without_input(self) -> None:
        error = CalculatorError("Test message")
        assert error.input_value is None


class TestDivisionByZeroError:
    """Tests for DivisionByZeroError."""

    def test_division_by_zero_message(self) -> None:
        error = DivisionByZeroError()
        assert error.message == "Error: Cannot divide by zero"

    def test_division_by_zero_is_calculator_error(self) -> None:
        error = DivisionByZeroError()
        assert isinstance(error, CalculatorError)

    def test_division_by_zero_no_input_value(self) -> None:
        error = DivisionByZeroError()
        assert error.input_value is None


class TestInvalidNumberError:
    """Tests for InvalidNumberError."""

    def test_invalid_number_message(self) -> None:
        error = InvalidNumberError("abc")
        assert error.message == "Error: 'abc' is not a valid number"

    def test_invalid_number_preserves_input(self) -> None:
        error = InvalidNumberError("xyz123")
        assert error.input_value == "xyz123"

    def test_invalid_number_is_calculator_error(self) -> None:
        error = InvalidNumberError("test")
        assert isinstance(error, CalculatorError)


class TestInvalidOperatorError:
    """Tests for InvalidOperatorError."""

    def test_invalid_operator_message(self) -> None:
        error = InvalidOperatorError("%")
        assert "%" in error.message
        assert "Use +, -, *, or /" in error.message

    def test_invalid_operator_preserves_input(self) -> None:
        error = InvalidOperatorError("^")
        assert error.input_value == "^"

    def test_invalid_operator_is_calculator_error(self) -> None:
        error = InvalidOperatorError("&")
        assert isinstance(error, CalculatorError)


class TestIncompleteExpressionError:
    """Tests for IncompleteExpressionError."""

    def test_incomplete_expression_message(self) -> None:
        error = IncompleteExpressionError()
        assert "complete expression" in error.message
        assert "5 + 3" in error.message

    def test_incomplete_expression_is_calculator_error(self) -> None:
        error = IncompleteExpressionError()
        assert isinstance(error, CalculatorError)

    def test_incomplete_expression_no_input_value(self) -> None:
        error = IncompleteExpressionError()
        assert error.input_value is None
```

## Integration Tests

### test_cli.py

```python
"""Integration tests for CLI calculator."""

import subprocess
import sys

import pytest


def run_calc(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the calculator CLI with given arguments."""
    return subprocess.run(
        [sys.executable, "-m", "src.main", *args],
        capture_output=True,
        text=True,
    )


class TestCLIBasicArithmetic:
    """Integration tests for basic arithmetic operations."""

    def test_cli_addition(self) -> None:
        result = run_calc("5", "+", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "8"

    def test_cli_subtraction(self) -> None:
        result = run_calc("10", "-", "4")
        assert result.returncode == 0
        assert result.stdout.strip() == "6"

    def test_cli_multiplication(self) -> None:
        result = run_calc("6", "*", "7")
        assert result.returncode == 0
        assert result.stdout.strip() == "42"

    def test_cli_division(self) -> None:
        result = run_calc("20", "/", "4")
        assert result.returncode == 0
        assert result.stdout.strip() == "5"


class TestCLIDecimalSupport:
    """Integration tests for decimal number support."""

    def test_cli_decimal_addition(self) -> None:
        result = run_calc("3.5", "+", "2.5")
        assert result.returncode == 0
        assert result.stdout.strip() == "6"

    def test_cli_decimal_result(self) -> None:
        result = run_calc("10", "/", "4")
        assert result.returncode == 0
        assert result.stdout.strip() == "2.5"


class TestCLINegativeNumbers:
    """Integration tests for negative number support."""

    def test_cli_negative_first_operand(self) -> None:
        result = run_calc("-5", "+", "3")
        assert result.returncode == 0
        assert result.stdout.strip() == "-2"

    def test_cli_negative_second_operand(self) -> None:
        result = run_calc("5", "+", "-3")
        assert result.returncode == 0
        assert result.stdout.strip() == "2"

    def test_cli_both_negative(self) -> None:
        result = run_calc("-5", "+", "-3")
        assert result.returncode == 0
        assert result.stdout.strip() == "-8"

    def test_cli_negative_multiplication(self) -> None:
        result = run_calc("-3", "*", "4")
        assert result.returncode == 0
        assert result.stdout.strip() == "-12"


class TestCLIErrorHandling:
    """Integration tests for error handling."""

    def test_cli_division_by_zero(self) -> None:
        result = run_calc("10", "/", "0")
        assert result.returncode == 1
        assert "Cannot divide by zero" in result.stderr

    def test_cli_invalid_number(self) -> None:
        result = run_calc("abc", "+", "5")
        assert result.returncode == 1
        assert "not a valid number" in result.stderr

    def test_cli_invalid_operator(self) -> None:
        result = run_calc("5", "%", "3")
        assert result.returncode == 1
        assert "not a valid operator" in result.stderr

    def test_cli_incomplete_expression(self) -> None:
        result = run_calc("5", "+")
        assert result.returncode == 1
        assert "complete expression" in result.stderr

    def test_cli_no_arguments(self) -> None:
        result = run_calc()
        assert result.returncode == 1
        assert "complete expression" in result.stderr
```

## Test Coverage Matrix

| Feature | Unit Tests | Integration Tests |
|---------|------------|-------------------|
| Addition | `test_calculator.py::TestAdd` | `test_cli.py::TestCLIBasicArithmetic::test_cli_addition` |
| Subtraction | `test_calculator.py::TestSubtract` | `test_cli.py::TestCLIBasicArithmetic::test_cli_subtraction` |
| Multiplication | `test_calculator.py::TestMultiply` | `test_cli.py::TestCLIBasicArithmetic::test_cli_multiplication` |
| Division | `test_calculator.py::TestDivide` | `test_cli.py::TestCLIBasicArithmetic::test_cli_division` |
| Decimals | `test_calculator.py::TestDecimalOperations` | `test_cli.py::TestCLIDecimalSupport` |
| Negatives | `test_parser.py::TestParseNegativeNumbers` | `test_cli.py::TestCLINegativeNumbers` |
| Division by Zero | `test_calculator.py::TestDivide::test_divide_by_zero_raises_error` | `test_cli.py::TestCLIErrorHandling::test_cli_division_by_zero` |
| Invalid Number | `test_parser.py::TestParseErrors::test_parse_invalid_*` | `test_cli.py::TestCLIErrorHandling::test_cli_invalid_number` |
| Invalid Operator | `test_parser.py::TestParseErrors::test_parse_invalid_operator` | `test_cli.py::TestCLIErrorHandling::test_cli_invalid_operator` |
| Incomplete Expression | `test_parser.py::TestParseErrors::test_parse_incomplete_*` | `test_cli.py::TestCLIErrorHandling::test_cli_incomplete_expression` |

## Expected Test Count

| Test File | Test Count |
|-----------|------------|
| `test_calculator.py` | ~25 tests |
| `test_parser.py` | ~12 tests |
| `test_errors.py` | ~12 tests |
| `test_cli.py` | ~15 tests |
| **Total** | **~64 tests** |

## Quality Gate Requirements

All tests must pass before deployment:

```bash
# Must show 0 failures
uv run pytest -v

# Must show "Success: no issues found"
uv run mypy src/

# Must show "All checks passed!"
uv run ruff check .
```

## Continuous Integration

Example GitHub Actions workflow:

```yaml
name: Tests
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v4
      - run: uv sync --all-groups
      - run: uv run pytest -v
      - run: uv run mypy src/
      - run: uv run ruff check .
```
