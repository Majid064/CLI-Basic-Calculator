# Implementation Plan: CLI Calculator

**Branch**: `001-cli-calculator` | **Date**: 2026-01-10 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-cli-calculator/spec.md`

## Summary

Build a command-line calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division) on two operands. The calculator accepts input in the format `<number> <operator> <number>`, supports decimal and negative numbers, and provides clear error messages for invalid inputs including division by zero.

**Technical Approach**: Implement as a simple Python CLI tool using argparse or direct stdin parsing. Operations implemented as pure functions with type hints. Input validation and error handling at the CLI boundary.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: None (standard library only)
**Storage**: N/A (stateless CLI tool)
**Testing**: pytest
**Target Platform**: Cross-platform (Windows, macOS, Linux)
**Project Type**: Single project
**Performance Goals**: Results within 1 second (trivially met for basic arithmetic)
**Constraints**: 10+ digits precision (met by Python's float)
**Scale/Scope**: Single-user CLI tool, ~200 LOC estimated

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Requirement | Status | Notes |
|-----------|-------------|--------|-------|
| I. Type Safety First | All functions have type hints | ✅ PASS | Will annotate all functions |
| II. uv Package Management | Use uv for project setup | ✅ PASS | `uv init`, `uv add --dev pytest mypy ruff` |
| III. Test-First Development | Tests cover all operations | ✅ PASS | Unit tests for each operation + edge cases |
| IV. Simplicity & YAGNI | Simple functions first | ✅ PASS | Pure functions, no classes needed |
| V. Clean Code Standards | PEP 8, docstrings, ruff | ✅ PASS | Will follow all conventions |

**Gate Status**: ✅ ALL GATES PASS - Proceed to Phase 0

## Project Structure

### Documentation (this feature)

```text
specs/001-cli-calculator/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (CLI interface spec)
└── tasks.md             # Phase 2 output (/sp.tasks command)
```

### Source Code (repository root)

```text
src/
├── __init__.py
├── calculator.py        # Core arithmetic operations
├── parser.py            # Input parsing and validation
├── errors.py            # Custom error types
└── main.py              # CLI entry point

tests/
├── __init__.py
├── unit/
│   ├── __init__.py
│   ├── test_calculator.py   # Operation unit tests
│   └── test_parser.py       # Parser unit tests
└── integration/
    ├── __init__.py
    └── test_cli.py          # End-to-end CLI tests
```

**Structure Decision**: Single project structure selected. This is a simple CLI tool with no frontend/backend split or external services. The `src/` directory contains the application code, `tests/` contains pytest tests organized by type.

## Complexity Tracking

> No violations detected. Design follows all constitution principles.

N/A - All gates pass without violations.
