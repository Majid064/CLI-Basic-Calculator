---
name: cli-calculator
description: Create a Python CLI calculator with basic arithmetic operations. Use when building calculator apps, learning Python project structure, or implementing arithmetic operations with proper error handling. Supports +, -, *, / with decimals and negative numbers.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# CLI Calculator Skill

Build a complete command-line calculator in Python with type safety, testing, and error handling.

## Overview

This skill creates a production-ready CLI calculator featuring:
- Basic arithmetic: addition, subtraction, multiplication, division
- Decimal and negative number support
- Custom exception hierarchy for error handling
- Full test coverage with pytest
- Type safety with mypy strict mode
- Code quality with ruff linting

## When to Use

- Creating a new calculator application
- Learning Python project structure with uv
- Implementing arithmetic operations with proper error handling
- Setting up a Python project with testing and type checking
- Building CLI applications with argument parsing

## Quick Start

```bash
# After implementation
uv run python -m src.main 5 + 3    # Output: 8
uv run python -m src.main 10 / 2   # Output: 5
uv run python -m src.main -5 + 3   # Output: -2
```

## Project Structure

```
project-root/
├── src/
│   ├── __init__.py        # Package marker
│   ├── calculator.py      # Core arithmetic operations
│   ├── parser.py          # Expression parsing and validation
│   ├── errors.py          # Custom exception classes
│   └── main.py            # CLI entry point
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_calculator.py
│   │   ├── test_parser.py
│   │   └── test_errors.py
│   └── integration/
│       ├── __init__.py
│       └── test_cli.py
├── pyproject.toml         # Project configuration
└── .python-version        # Python version (3.11)
```

## Implementation Guide

### Step 1: Initialize Project

```bash
uv init --name calculator
echo "3.11" > .python-version
uv add --group dev pytest mypy ruff
mkdir -p src tests/unit tests/integration
touch src/__init__.py tests/__init__.py tests/unit/__init__.py tests/integration/__init__.py
```

### Step 2: Configure pyproject.toml

```toml
[project]
name = "calculator"
version = "0.1.0"
description = "A CLI calculator for basic arithmetic operations"
requires-python = ">=3.11"
dependencies = []

[project.scripts]
calc = "src.main:main"

[dependency-groups]
dev = [
    "mypy>=1.19.1",
    "pytest>=9.0.2",
    "ruff>=0.14.11",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]

[tool.mypy]
python_version = "3.11"
strict = true
files = ["src"]

[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]
```

### Step 3: Implement Error Classes (src/errors.py)

```python
"""Custom exception classes for the calculator."""


class CalculatorError(Exception):
    """Base exception for calculator errors."""

    def __init__(self, message: str, input_value: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.input_value = input_value


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    def __init__(self) -> None:
        super().__init__("Error: Cannot divide by zero", None)


class InvalidNumberError(CalculatorError):
    """Raised when an invalid number is provided."""

    def __init__(self, value: str) -> None:
        super().__init__(f"Error: '{value}' is not a valid number", value)


class InvalidOperatorError(CalculatorError):
    """Raised when an invalid operator is provided."""

    def __init__(self, operator: str) -> None:
        super().__init__(
            f"Error: '{operator}' is not a valid operator. Use +, -, *, or /",
            operator,
        )


class IncompleteExpressionError(CalculatorError):
    """Raised when expression is incomplete."""

    def __init__(self) -> None:
        super().__init__(
            "Error: Please provide a complete expression (e.g., 5 + 3)", None
        )
```

### Step 4: Implement Calculator Core (src/calculator.py)

```python
"""Core calculator operations."""

from enum import Enum
from src.errors import DivisionByZeroError, InvalidOperatorError


class Operator(Enum):
    """Supported arithmetic operators."""
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b. Raises DivisionByZeroError if b is zero."""
    if b == 0:
        raise DivisionByZeroError()
    return a / b


def calculate(left: float, operator: str, right: float) -> float:
    """Perform calculation based on operator."""
    operations: dict[str, callable[[float, float], float]] = {
        Operator.ADD.value: add,
        Operator.SUBTRACT.value: subtract,
        Operator.MULTIPLY.value: multiply,
        Operator.DIVIDE.value: divide,
    }

    if operator not in operations:
        raise InvalidOperatorError(operator)

    return operations[operator](left, right)


def format_result(value: float) -> str:
    """Format result - whole numbers without decimal, decimals with precision."""
    if value == int(value):
        return str(int(value))
    return str(value)
```

### Step 5: Implement Parser (src/parser.py)

```python
"""Expression parsing for the calculator."""

from src.errors import (
    IncompleteExpressionError,
    InvalidNumberError,
    InvalidOperatorError,
)

VALID_OPERATORS = {"+", "-", "*", "/"}


def parse_expression(args: list[str]) -> tuple[float, str, float]:
    """Parse command line arguments into expression components."""
    if len(args) != 3:
        raise IncompleteExpressionError()

    left_str, operator, right_str = args

    if operator not in VALID_OPERATORS:
        raise InvalidOperatorError(operator)

    try:
        left = float(left_str)
    except ValueError:
        raise InvalidNumberError(left_str)

    try:
        right = float(right_str)
    except ValueError:
        raise InvalidNumberError(right_str)

    return left, operator, right
```

### Step 6: Implement CLI Entry Point (src/main.py)

```python
"""CLI entry point for the calculator."""

import sys
from src.calculator import calculate, format_result
from src.errors import CalculatorError
from src.parser import parse_expression


def main() -> None:
    """Run the calculator CLI."""
    try:
        left, operator, right = parse_expression(sys.argv[1:])
        result = calculate(left, operator, right)
        print(format_result(result))
    except CalculatorError as e:
        print(e.message, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## Usage Examples

```bash
# Basic operations
uv run python -m src.main 5 + 3      # 8
uv run python -m src.main 10 - 4     # 6
uv run python -m src.main 6 "*" 7    # 42 (quote * for shell)
uv run python -m src.main 20 / 4     # 5

# Decimals
uv run python -m src.main 3.5 + 2.5  # 6
uv run python -m src.main 10 / 3     # 3.333...

# Negative numbers
uv run python -m src.main -5 + 3     # -2
uv run python -m src.main 5 - -3     # 8

# Error handling
uv run python -m src.main 10 / 0     # Error: Cannot divide by zero
uv run python -m src.main abc + 5    # Error: 'abc' is not a valid number
```

## Quality Gates

```bash
# Run all tests
uv run pytest -v

# Type checking (strict mode)
uv run mypy src/

# Linting
uv run ruff check .

# Formatting
uv run ruff format .
```

## Additional Resources

- [README.md](README.md) - Project overview and quick start
- [TESTING.md](TESTING.md) - Complete test cases and validation
