# CLI Interface Contract: Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-10
**Version**: 1.0.0

## Command Signature

```text
python -m calculator <number> <operator> <number>
```

Or using the installed command (after `uv run pip install -e .`):

```text
calc <number> <operator> <number>
```

## Input Specification

### Arguments

| Position | Name | Type | Required | Description |
|----------|------|------|----------|-------------|
| 1 | left_operand | number | Yes | First operand (integer or decimal, may be negative) |
| 2 | operator | string | Yes | Arithmetic operator: +, -, *, / |
| 3 | right_operand | number | Yes | Second operand (integer or decimal, may be negative) |

### Number Format

- Integers: `5`, `-10`, `0`
- Decimals: `3.14`, `-0.5`, `0.001`
- Scientific notation: Not supported (out of scope)

### Operator Format

| Symbol | Operation | Example |
|--------|-----------|---------|
| + | Addition | `5 + 3` → `8` |
| - | Subtraction | `10 - 4` → `6` |
| * | Multiplication | `6 * 7` → `42` |
| / | Division | `20 / 4` → `5` |

## Output Specification

### Success Response

**Stream**: stdout
**Format**: Single line containing the numeric result
**Exit Code**: 0

```text
<result>
```

**Result Formatting**:
- Whole numbers display without decimal: `8` not `8.0`
- Decimal results display full precision: `2.5`, `0.30000000000000004`

### Error Response

**Stream**: stderr
**Format**: Single line starting with "Error:"
**Exit Code**: 1

| Error Condition | Message |
|-----------------|---------|
| Division by zero | `Error: Cannot divide by zero` |
| Invalid number | `Error: '<input>' is not a valid number` |
| Invalid operator | `Error: '<op>' is not a valid operator. Use +, -, *, /` |
| Wrong argument count | `Error: Incomplete expression. Format: <number> <operator> <number>` |

## Examples

### Successful Operations

```bash
$ python -m calculator 5 + 3
8

$ python -m calculator 10 - 4
6

$ python -m calculator 6 "*" 7
42

$ python -m calculator 20 / 4
5

$ python -m calculator 3.5 + 2.5
6.0

$ python -m calculator -5 + 3
-2

$ python -m calculator 10 - -4
14
```

Note: On most shells, `*` must be quoted to prevent glob expansion.

### Error Cases

```bash
$ python -m calculator 10 / 0
Error: Cannot divide by zero

$ python -m calculator abc + 5
Error: 'abc' is not a valid number

$ python -m calculator 5 $ 3
Error: '$' is not a valid operator. Use +, -, *, /

$ python -m calculator 5 +
Error: Incomplete expression. Format: <number> <operator> <number>
```

## Behavior Notes

1. **Whitespace**: Arguments are space-separated; extra spaces between args are handled by the shell
2. **Precision**: Results maintain Python float precision (~15-17 significant digits)
3. **Overflow**: Python handles arbitrary precision integers; float overflow returns `inf`
4. **Negative zero**: `-0.0` displays as `0`

## Versioning

This contract follows semantic versioning:
- **MAJOR**: Breaking changes to input/output format
- **MINOR**: New operators or features (backward compatible)
- **PATCH**: Bug fixes, message improvements
