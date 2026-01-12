---
description: Create a CLI calculator with TUI interface. Supports basic arithmetic (+, -, *, /), decimals, negative numbers, and error handling. Uses Python 3.11+, uv, mypy strict, ruff, pytest, and Textual TUI.
argument-hint: [project-name]
---

## User Input

```text
$ARGUMENTS
```

## Overview

This skill creates a complete CLI calculator application with:
- **CLI Mode**: Command-line interface for quick calculations
- **TUI Mode**: Beautiful terminal UI with Textual library
- **Full Test Coverage**: Unit and integration tests
- **Type Safety**: mypy strict mode
- **Code Quality**: ruff linting and formatting

## Project Structure

```
<project-name>/
├── src/
│   ├── __init__.py
│   ├── calculator.py    # Core arithmetic operations
│   ├── parser.py        # Expression parsing
│   ├── errors.py        # Custom exception hierarchy
│   ├── main.py          # CLI entry point
│   └── tui/
│       ├── __init__.py
│       ├── app.py       # Textual TUI application
│       └── styles.tcss  # TUI styling
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
├── pyproject.toml
└── .python-version
```

## Implementation Steps

### Step 1: Initialize Project

```bash
# Create project directory
mkdir <project-name>
cd <project-name>

# Initialize uv project
uv init --name calculator

# Set Python version
echo "3.11" > .python-version

# Add dependencies
uv add textual
uv add --group dev pytest mypy ruff
```

### Step 2: Create pyproject.toml

```toml
[project]
name = "calculator"
version = "0.1.0"
description = "A CLI calculator with TUI interface"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "textual>=7.1.0",
]

[project.scripts]
calc = "src.main:main"
calc-tui = "src.tui.app:main"

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

### Step 3: Create src/errors.py

```python
"""Custom exception classes for the calculator."""


class CalculatorError(Exception):
    """Base exception for calculator errors."""

    def __init__(self, message: str, input_value: str | None = None) -> None:
        """Initialize calculator error."""
        super().__init__(message)
        self.message = message
        self.input_value = input_value


class DivisionByZeroError(CalculatorError):
    """Raised when attempting to divide by zero."""

    def __init__(self) -> None:
        """Initialize division by zero error."""
        super().__init__("Error: Cannot divide by zero", None)


class InvalidNumberError(CalculatorError):
    """Raised when an invalid number is provided."""

    def __init__(self, value: str) -> None:
        """Initialize invalid number error."""
        super().__init__(f"Error: '{value}' is not a valid number", value)


class InvalidOperatorError(CalculatorError):
    """Raised when an invalid operator is provided."""

    def __init__(self, operator: str) -> None:
        """Initialize invalid operator error."""
        super().__init__(
            f"Error: '{operator}' is not a valid operator. Use +, -, *, or /",
            operator,
        )


class IncompleteExpressionError(CalculatorError):
    """Raised when expression is incomplete."""

    def __init__(self) -> None:
        """Initialize incomplete expression error."""
        super().__init__(
            "Error: Please provide a complete expression (e.g., 5 + 3)", None
        )
```

### Step 4: Create src/calculator.py

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
    """Divide a by b."""
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
    """Format result for display."""
    if value == int(value):
        return str(int(value))
    return str(value)
```

### Step 5: Create src/parser.py

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

### Step 6: Create src/main.py

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

### Step 7: Create src/__init__.py

```python
"""Calculator package."""
```

### Step 8: Create TUI - src/tui/__init__.py

```python
"""TUI package for the calculator."""

from src.tui.app import CalculatorApp

__all__ = ["CalculatorApp"]
```

### Step 9: Create TUI - src/tui/app.py

```python
"""Terminal UI Calculator Application using Textual."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal
from textual.widgets import Button, Footer, Header, Static

from src.calculator import calculate, format_result
from src.errors import CalculatorError


class CalculatorApp(App[None]):
    """A beautiful terminal calculator TUI."""

    CSS_PATH = "styles.tcss"
    TITLE = "CLI Calculator"

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("c", "clear", "Clear"),
        Binding("escape", "clear", "Clear", show=False),
        Binding("enter", "calculate", "Calculate"),
        Binding("=", "calculate", "=", show=False),
        Binding("backspace", "backspace", "Back", show=False),
        Binding("0", "press_digit('0')", "0", show=False),
        Binding("1", "press_digit('1')", "1", show=False),
        Binding("2", "press_digit('2')", "2", show=False),
        Binding("3", "press_digit('3')", "3", show=False),
        Binding("4", "press_digit('4')", "4", show=False),
        Binding("5", "press_digit('5')", "5", show=False),
        Binding("6", "press_digit('6')", "6", show=False),
        Binding("7", "press_digit('7')", "7", show=False),
        Binding("8", "press_digit('8')", "8", show=False),
        Binding("9", "press_digit('9')", "9", show=False),
        Binding(".", "press_digit('.')", ".", show=False),
        Binding("+", "press_operator('+')", "+", show=False),
        Binding("-", "press_operator('-')", "-", show=False),
        Binding("*", "press_operator('*')", "*", show=False),
        Binding("/", "press_operator('/')", "/", show=False),
    ]

    def __init__(self) -> None:
        """Initialize the calculator app."""
        super().__init__()
        self.left_operand: str = ""
        self.operator: str = ""
        self.right_operand: str = ""
        self.result: str = ""
        self.error_message: str = ""

    def compose(self) -> ComposeResult:
        """Compose the UI layout."""
        yield Header()
        yield Container(
            Static("", id="display-expression"),
            Static("0", id="display-result"),
            Container(
                Horizontal(
                    Button("7", id="btn-7", classes="digit"),
                    Button("8", id="btn-8", classes="digit"),
                    Button("9", id="btn-9", classes="digit"),
                    Button("/", id="btn-div", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("4", id="btn-4", classes="digit"),
                    Button("5", id="btn-5", classes="digit"),
                    Button("6", id="btn-6", classes="digit"),
                    Button("*", id="btn-mul", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("1", id="btn-1", classes="digit"),
                    Button("2", id="btn-2", classes="digit"),
                    Button("3", id="btn-3", classes="digit"),
                    Button("-", id="btn-sub", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("C", id="btn-clear", classes="control"),
                    Button("0", id="btn-0", classes="digit"),
                    Button(".", id="btn-dot", classes="digit"),
                    Button("+", id="btn-add", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("=", id="btn-equals", classes="equals"),
                    classes="button-row",
                ),
                id="button-container",
            ),
            id="calculator-body",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        if button_id is None:
            return

        if button_id == "btn-clear":
            self.action_clear()
        elif button_id == "btn-equals":
            self.action_calculate()
        elif button_id == "btn-dot":
            self._add_digit(".")
        elif button_id.startswith("btn-") and button_id[4:].isdigit():
            self._add_digit(button_id[4:])
        elif button_id in ("btn-add", "btn-sub", "btn-mul", "btn-div"):
            op_map = {"btn-add": "+", "btn-sub": "-", "btn-mul": "*", "btn-div": "/"}
            self._set_operator(op_map[button_id])

    def action_clear(self) -> None:
        """Clear the calculator state."""
        self.left_operand = ""
        self.operator = ""
        self.right_operand = ""
        self.result = ""
        self.error_message = ""
        self._update_display()

    def action_calculate(self) -> None:
        """Perform the calculation."""
        if not self.left_operand or not self.operator:
            return

        right = self.right_operand if self.right_operand else "0"

        try:
            left_val = float(self.left_operand)
            right_val = float(right)
            result_value = calculate(left_val, self.operator, right_val)
            self.result = format_result(result_value)
            self.error_message = ""
            self.left_operand = self.result
            self.operator = ""
            self.right_operand = ""
        except CalculatorError as e:
            self.error_message = e.message
            self.result = ""
        except ValueError:
            self.error_message = "Invalid input"
            self.result = ""

        self._update_display()

    def action_backspace(self) -> None:
        """Delete the last character."""
        if self.right_operand:
            self.right_operand = self.right_operand[:-1]
        elif self.operator:
            self.operator = ""
        elif self.left_operand:
            self.left_operand = self.left_operand[:-1]
        self._update_display()

    def action_press_digit(self, digit: str) -> None:
        """Handle digit key press."""
        self._add_digit(digit)

    def action_press_operator(self, op: str) -> None:
        """Handle operator key press."""
        self._set_operator(op)

    def _add_digit(self, digit: str) -> None:
        """Add a digit to the current operand."""
        if self.error_message:
            self.error_message = ""
            self.result = ""

        if self.result and not self.operator:
            self.left_operand = ""
            self.result = ""

        if not self.operator:
            if digit == "." and "." in self.left_operand:
                return
            self.left_operand += digit
        else:
            if digit == "." and "." in self.right_operand:
                return
            self.right_operand += digit

        self._update_display()

    def _set_operator(self, op: str) -> None:
        """Set the operator."""
        if self.error_message:
            self.error_message = ""

        if not self.left_operand and op == "-":
            self.left_operand = "-"
            self._update_display()
            return

        if self.left_operand and self.operator and self.right_operand:
            self.action_calculate()

        if self.left_operand:
            self.operator = op
            self.right_operand = ""
            self._update_display()

    def _update_display(self) -> None:
        """Update the display widgets."""
        parts = []
        if self.left_operand:
            parts.append(self.left_operand)
        if self.operator:
            parts.append(self.operator)
        if self.right_operand:
            parts.append(self.right_operand)

        expression = " ".join(parts)
        self.query_one("#display-expression", Static).update(expression)

        result_widget = self.query_one("#display-result", Static)
        if self.error_message:
            result_widget.update(self.error_message)
            result_widget.add_class("error")
        else:
            display_value = self.result if self.result else "0"
            result_widget.update(display_value)
            result_widget.remove_class("error")


def main() -> None:
    """Run the calculator TUI."""
    app = CalculatorApp()
    app.run()


if __name__ == "__main__":
    main()
```

### Step 10: Create TUI - src/tui/styles.tcss

```css
/* Calculator TUI Stylesheet - Catppuccin Theme */

Screen {
    background: #1e1e2e;
    align: center middle;
}

#calculator-body {
    width: 50;
    height: auto;
    padding: 1 2;
    border: round #89b4fa;
    background: #313244;
}

#display-expression {
    width: 100%;
    height: 1;
    text-align: right;
    color: #a6adc8;
    padding: 0 1;
    margin-bottom: 0;
}

#display-result {
    width: 100%;
    height: 2;
    text-align: right;
    color: #cdd6f4;
    text-style: bold;
    padding: 0 1;
    margin-bottom: 1;
}

#display-result.error {
    color: #f38ba8;
}

#button-container {
    width: 100%;
    height: auto;
}

.button-row {
    width: 100%;
    height: 3;
    align: center middle;
}

Button {
    width: 1fr;
    min-width: 8;
    height: 3;
    margin: 0 1;
}

Button.digit {
    background: #45475a;
    color: #cdd6f4;
}

Button.digit:hover {
    background: #585b70;
}

Button.operator {
    background: #f9e2af;
    color: #1e1e2e;
}

Button.operator:hover {
    background: #f5c2e7;
}

Button.control {
    background: #f38ba8;
    color: #1e1e2e;
}

Button.control:hover {
    background: #eba0ac;
}

Button.equals {
    background: #a6e3a1;
    color: #1e1e2e;
    width: 100%;
}

Button.equals:hover {
    background: #94e2d5;
}

Header {
    background: #89b4fa;
    color: #1e1e2e;
}

Footer {
    background: #313244;
}
```

### Step 11: Create Tests

Create empty `__init__.py` files:
- `tests/__init__.py`
- `tests/unit/__init__.py`
- `tests/integration/__init__.py`

Create test files following TDD patterns with pytest.

### Step 12: Run Quality Gates

```bash
# Run tests
uv run pytest -v

# Run type checking
uv run mypy src/

# Run linting
uv run ruff check .

# Format code
uv run ruff format .
```

## Usage

### CLI Mode
```bash
uv run calc 5 + 3      # Output: 8
uv run calc 10 - 4     # Output: 6
uv run calc 6 "*" 7    # Output: 42  (quote * to avoid shell expansion)
uv run calc 20 / 4     # Output: 5
uv run calc 3.5 + 2.5  # Output: 6
uv run calc -5 + 3     # Output: -2
```

### TUI Mode
```bash
uv run calc-tui
```

**TUI Controls:**
- **Numbers:** Click buttons or press 0-9
- **Operators:** Click or press +, -, *, /
- **Calculate:** Click = or press Enter
- **Clear:** Click C or press C/Escape
- **Quit:** Press Q

## Features

- Basic arithmetic: +, -, *, /
- Decimal number support
- Negative number handling
- Division by zero error handling
- Invalid input error messages
- Result chaining in TUI
- Keyboard and mouse support
- Beautiful Catppuccin color theme

## Quality Standards

- **Type Safety:** mypy strict mode, 0 errors
- **Linting:** ruff check, 0 issues
- **Formatting:** ruff format, consistent style
- **Testing:** pytest, 58+ tests, 100% pass rate
