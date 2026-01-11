# Quickstart: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-10

## Prerequisites

- Python 3.11 or higher
- uv package manager installed

## Setup

### 1. Initialize the Project

```bash
# From repository root
uv init

# Install development dependencies
uv add --dev pytest mypy ruff
```

### 2. Project Structure

After setup, your project should look like:

```text
.
├── pyproject.toml
├── uv.lock
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   ├── parser.py
│   ├── errors.py
│   └── main.py
└── tests/
    ├── __init__.py
    ├── unit/
    │   ├── test_calculator.py
    │   └── test_parser.py
    └── integration/
        └── test_cli.py
```

### 3. Configure pyproject.toml

Add these sections to your `pyproject.toml`:

```toml
[project]
name = "calculator"
version = "0.1.0"
description = "A simple CLI calculator"
requires-python = ">=3.11"

[project.scripts]
calc = "src.main:main"

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["."]

[tool.mypy]
python_version = "3.11"
strict = true

[tool.ruff]
line-length = 88
target-version = "py311"
```

## Running the Calculator

### Direct Module Execution

```bash
# Basic operations
uv run python -m src.main 5 + 3
uv run python -m src.main 10 - 4
uv run python -m src.main 6 "*" 7
uv run python -m src.main 20 / 4

# Decimal numbers
uv run python -m src.main 3.5 + 2.5

# Negative numbers
uv run python -m src.main -5 + 3
uv run python -m src.main 10 - -4
```

### Using the Installed Command

After installing in development mode:

```bash
uv pip install -e .
calc 5 + 3
```

## Running Tests

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/unit/test_calculator.py

# Run with coverage
uv run pytest --cov=src
```

## Running Quality Checks

```bash
# Type checking
uv run mypy src/

# Linting
uv run ruff check .

# Auto-format
uv run ruff format .
```

## Validation Checklist

After implementation, verify:

- [ ] `uv run python -m src.main 5 + 3` outputs `8`
- [ ] `uv run python -m src.main 10 / 0` outputs error to stderr
- [ ] `uv run pytest` passes all tests
- [ ] `uv run mypy src/` reports no errors
- [ ] `uv run ruff check .` reports no issues

## Troubleshooting

### "Module not found" error

Ensure you're running from the repository root and the `src/` directory has `__init__.py` files.

### Shell expansion of `*`

On Unix shells, quote the multiplication operator:

```bash
uv run python -m src.main 6 "*" 7
# or
uv run python -m src.main 6 '*' 7
```

### Permission denied on Windows

Run from a shell with appropriate permissions, or use:

```powershell
uv run python -m src.main 5 + 3
```
