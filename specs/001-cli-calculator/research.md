# Research: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-10
**Status**: Complete

## Research Questions

### 1. CLI Input Handling Approach

**Decision**: Use `sys.argv` for command-line arguments

**Rationale**:
- Simplest approach for a basic calculator
- No external dependencies required
- Supports the required format: `python -m calculator 5 + 3`
- Alternative: stdin input would require a REPL loop (out of scope per assumptions)

**Alternatives Considered**:
| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| sys.argv | Simple, standard | Less flexible | ✅ Selected |
| argparse | Better help/validation | Overkill for this use case | Rejected |
| click | Nice CLI framework | External dependency | Rejected |
| stdin REPL | Interactive | Out of scope | Rejected |

### 2. Floating-Point Precision Handling

**Decision**: Use Python's native `float` type

**Rationale**:
- Python's float provides ~15-17 significant digits (exceeds 10-digit requirement)
- Standard IEEE 754 double-precision
- Simple and sufficient for a basic calculator
- Known limitation: `0.1 + 0.2 = 0.30000000000000004` (acceptable per spec)

**Alternatives Considered**:
| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| float | Simple, fast | Binary representation issues | ✅ Selected |
| Decimal | Exact decimal math | Slower, more complex | Rejected (YAGNI) |
| fractions.Fraction | Exact rational math | Complex output format | Rejected |

### 3. Error Handling Strategy

**Decision**: Custom exception hierarchy with user-friendly messages

**Rationale**:
- Clear separation between internal errors and user-facing messages
- Enables specific error handling for each error type
- Messages written for non-technical users (per SC-005)

**Error Types**:
| Error | Message | Exit Code |
|-------|---------|-----------|
| DivisionByZero | "Error: Cannot divide by zero" | 1 |
| InvalidNumber | "Error: '{input}' is not a valid number" | 1 |
| InvalidOperator | "Error: '{op}' is not a valid operator. Use +, -, *, /" | 1 |
| IncompleteExpression | "Error: Incomplete expression. Format: <number> <operator> <number>" | 1 |

### 4. Negative Number Parsing

**Decision**: Support negative numbers with `-` prefix, handle `- -` as subtraction of negative

**Rationale**:
- `-5` parses as negative five
- `10 - -4` parses as "10 minus negative 4" = 14
- Parser must handle operator ambiguity between subtraction and negative sign

**Parsing Strategy**:
1. Split input into exactly 3 tokens
2. First token: parse as number (may start with `-`)
3. Second token: must be operator (`+`, `-`, `*`, `/`)
4. Third token: parse as number (may start with `-`)

### 5. Output Formatting

**Decision**: Display result as-is from Python's float, strip trailing zeros for whole numbers

**Rationale**:
- `5 + 3` → `8` (not `8.0`)
- `10 / 4` → `2.5`
- `0.1 + 0.2` → `0.30000000000000004` (honest representation)

**Implementation**:
```python
def format_result(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return str(value)
```

## Technology Decisions Summary

| Concern | Decision | Rationale |
|---------|----------|-----------|
| CLI Framework | sys.argv | Simplicity, no dependencies |
| Number Type | float | Sufficient precision, simple |
| Error Handling | Custom exceptions | Clear user messages |
| Parsing | Token-based split | Handles negatives correctly |
| Output | Smart formatting | Clean integer display |

## Dependencies

**Runtime**: None (Python standard library only)

**Development**:
- pytest: Testing framework
- mypy: Type checking
- ruff: Linting and formatting

## Open Questions

None - all technical decisions resolved.
