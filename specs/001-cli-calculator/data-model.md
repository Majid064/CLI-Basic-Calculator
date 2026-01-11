# Data Model: CLI Calculator

**Feature**: 001-cli-calculator
**Date**: 2026-01-10
**Status**: Complete

## Overview

This is a stateless CLI calculator with no persistent data. The data model defines the runtime structures used for input parsing and error handling.

## Entities

### Expression

Represents a parsed arithmetic expression.

| Field | Type | Description | Validation |
|-------|------|-------------|------------|
| left_operand | float | First number in the expression | Must be a valid floating-point number |
| operator | Operator | The arithmetic operation to perform | Must be one of: +, -, *, / |
| right_operand | float | Second number in the expression | Must be a valid floating-point number |

**Invariants**:
- Both operands must be finite numbers (not NaN or infinity)
- For division, right_operand must not be zero

### Operator (Enumeration)

Defines valid arithmetic operators.

| Value | Symbol | Operation |
|-------|--------|-----------|
| ADD | + | Addition |
| SUBTRACT | - | Subtraction |
| MULTIPLY | * | Multiplication |
| DIVIDE | / | Division |

### CalculatorError (Base Error)

Base class for all calculator-specific errors.

| Field | Type | Description |
|-------|------|-------------|
| message | str | User-friendly error message |
| input_value | str | Optional - the problematic input |

**Subclasses**:

| Error Type | Trigger | Message Template |
|------------|---------|------------------|
| DivisionByZeroError | Division where right_operand = 0 | "Error: Cannot divide by zero" |
| InvalidNumberError | Non-numeric input | "Error: '{value}' is not a valid number" |
| InvalidOperatorError | Unknown operator symbol | "Error: '{op}' is not a valid operator. Use +, -, *, /" |
| IncompleteExpressionError | Wrong number of tokens | "Error: Incomplete expression. Format: <number> <operator> <number>" |

## Data Flow

```text
User Input (string)
       │
       ▼
┌──────────────────┐
│  Input Parser    │ ──▶ IncompleteExpressionError
│  (tokenize)      │ ──▶ InvalidNumberError
│                  │ ──▶ InvalidOperatorError
└──────────────────┘
       │
       ▼
   Expression
       │
       ▼
┌──────────────────┐
│  Calculator      │ ──▶ DivisionByZeroError
│  (compute)       │
└──────────────────┘
       │
       ▼
   Result (float)
       │
       ▼
┌──────────────────┐
│  Output Formatter│
└──────────────────┘
       │
       ▼
   Output (string)
```

## State Transitions

N/A - This is a stateless application. Each invocation:
1. Receives input
2. Parses → computes → formats
3. Outputs result or error
4. Exits

## Relationships

```text
Expression 1 ─────── 1 Operator
     │
     └──── validated by ────▶ CalculatorError (on failure)
```

## Validation Rules

| Rule | Field(s) | Condition | Error |
|------|----------|-----------|-------|
| V1 | left_operand, right_operand | Must parse as float | InvalidNumberError |
| V2 | operator | Must be in {+, -, *, /} | InvalidOperatorError |
| V3 | input tokens | Must have exactly 3 parts | IncompleteExpressionError |
| V4 | right_operand (for division) | Must not be 0 | DivisionByZeroError |
