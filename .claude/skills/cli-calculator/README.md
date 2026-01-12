# CLI Calculator

A simple, production-ready command-line calculator built with Python.

## Features

- **Basic Arithmetic**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Decimal Support**: Handle floating-point numbers (3.14, 2.5, etc.)
- **Negative Numbers**: Support for negative operands (-5, -3.14, etc.)
- **Error Handling**: User-friendly error messages for invalid inputs
- **Type Safety**: Full type hints with mypy strict mode
- **Test Coverage**: Comprehensive unit and integration tests

## Requirements

- Python 3.11+
- uv (package manager)

## Quick Start

### 1. Create Project

```bash
mkdir calculator && cd calculator
uv init --name calculator
echo "3.11" > .python-version
```

### 2. Add Dev Dependencies

```bash
uv add --group dev pytest mypy ruff
```

### 3. Create Directory Structure

```bash
mkdir -p src tests/unit tests/integration
touch src/__init__.py
touch tests/__init__.py tests/unit/__init__.py tests/integration/__init__.py
```

### 4. Implement Core Files

Create these files following the implementation in [SKILL.md](SKILL.md):

| File | Purpose |
|------|---------|
| `src/errors.py` | Custom exception hierarchy |
| `src/calculator.py` | Arithmetic operations |
| `src/parser.py` | Expression parsing |
| `src/main.py` | CLI entry point |

### 5. Run Calculator

```bash
uv run python -m src.main 5 + 3
# Output: 8
```

## Usage

### Basic Operations

```bash
uv run python -m src.main 10 + 5     # Addition: 15
uv run python -m src.main 10 - 5     # Subtraction: 5
uv run python -m src.main 10 "*" 5   # Multiplication: 50
uv run python -m src.main 10 / 5     # Division: 2
```

> **Note**: Quote the `*` operator to prevent shell expansion.

### Decimal Numbers

```bash
uv run python -m src.main 3.14 + 2.86    # 6
uv run python -m src.main 10 / 3         # 3.3333333333333335
```

### Negative Numbers

```bash
uv run python -m src.main -5 + 10        # 5
uv run python -m src.main 5 "*" -3       # -15
uv run python -m src.main -10 / -2       # 5
```

## Error Messages

The calculator provides clear, user-friendly error messages:

| Error | Message |
|-------|---------|
| Division by zero | `Error: Cannot divide by zero` |
| Invalid number | `Error: 'abc' is not a valid number` |
| Invalid operator | `Error: '%' is not a valid operator. Use +, -, *, or /` |
| Incomplete expression | `Error: Please provide a complete expression (e.g., 5 + 3)` |

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                        main.py                          │
│                    (CLI Entry Point)                    │
└─────────────────────────┬───────────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
┌─────────────────────┐       ┌─────────────────────┐
│     parser.py       │       │   calculator.py     │
│  (Input Validation) │       │ (Core Operations)   │
└─────────┬───────────┘       └─────────┬───────────┘
          │                             │
          └───────────┬─────────────────┘
                      ▼
          ┌─────────────────────┐
          │     errors.py       │
          │ (Exception Classes) │
          └─────────────────────┘
```

### Module Responsibilities

| Module | Responsibility |
|--------|----------------|
| `errors.py` | Define custom exceptions with user-friendly messages |
| `calculator.py` | Implement arithmetic operations and result formatting |
| `parser.py` | Parse and validate command-line arguments |
| `main.py` | Orchestrate parsing, calculation, and output |

## Quality Standards

This project follows strict quality standards:

### Type Safety
- mypy strict mode enabled
- All functions have type hints
- No `Any` types allowed

### Code Style
- ruff for linting and formatting
- Line length: 88 characters
- Python 3.11+ features

### Testing
- pytest for test framework
- Unit tests for each module
- Integration tests for CLI

## Running Quality Checks

```bash
# Run tests
uv run pytest -v

# Type checking
uv run mypy src/

# Linting
uv run ruff check .

# Formatting
uv run ruff format .
```

## Project Configuration

See `pyproject.toml` for complete configuration including:
- Project metadata
- Script entry points
- pytest configuration
- mypy strict settings
- ruff lint rules

## License

MIT License
