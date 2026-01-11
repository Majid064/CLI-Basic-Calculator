# Feature Specification: CLI Calculator

**Feature Branch**: `001-cli-calculator`
**Created**: 2026-01-10
**Status**: Draft
**Input**: User description: "Build a basic CLI calculator that handles addition, subtraction, multiplication and division with challenges: decimal handling, division by zero, negative numbers, invalid input handling"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Arithmetic Operations (Priority: P1)

As a user, I want to perform basic arithmetic calculations (addition, subtraction, multiplication, division) through a command-line interface so that I can quickly compute results without opening a graphical application.

**Why this priority**: This is the core functionality of a calculator. Without basic arithmetic operations, the tool has no value.

**Independent Test**: Can be fully tested by running the calculator with two numbers and an operator, verifying the correct result is returned.

**Acceptance Scenarios**:

1. **Given** the calculator is started, **When** I enter `5 + 3`, **Then** the result `8` is displayed
2. **Given** the calculator is started, **When** I enter `10 - 4`, **Then** the result `6` is displayed
3. **Given** the calculator is started, **When** I enter `6 * 7`, **Then** the result `42` is displayed
4. **Given** the calculator is started, **When** I enter `20 / 4`, **Then** the result `5` is displayed

---

### User Story 2 - Decimal Number Support (Priority: P2)

As a user, I want to calculate with decimal numbers so that I can perform precise calculations involving fractions.

**Why this priority**: Decimal support significantly extends the calculator's usefulness for real-world calculations, but basic integer operations can still deliver value without it.

**Independent Test**: Can be tested by entering decimal numbers and verifying precise results are returned.

**Acceptance Scenarios**:

1. **Given** the calculator is started, **When** I enter `3.5 + 2.5`, **Then** the result `6.0` is displayed
2. **Given** the calculator is started, **When** I enter `10 / 4`, **Then** the result `2.5` is displayed
3. **Given** the calculator is started, **When** I enter `0.1 + 0.2`, **Then** the result is displayed with reasonable precision (e.g., `0.3` or `0.30000000000000004`)

---

### User Story 3 - Negative Number Support (Priority: P3)

As a user, I want to perform calculations with negative numbers so that I can handle a full range of mathematical operations.

**Why this priority**: Negative number support is important for complete arithmetic coverage but many basic calculations can be done without it.

**Independent Test**: Can be tested by entering negative numbers in calculations and verifying correct signed results.

**Acceptance Scenarios**:

1. **Given** the calculator is started, **When** I enter `-5 + 3`, **Then** the result `-2` is displayed
2. **Given** the calculator is started, **When** I enter `10 - -4`, **Then** the result `14` is displayed
3. **Given** the calculator is started, **When** I enter `-6 * -7`, **Then** the result `42` is displayed
4. **Given** the calculator is started, **When** I enter `-20 / 4`, **Then** the result `-5` is displayed

---

### User Story 4 - Error Handling (Priority: P4)

As a user, I want to receive clear error messages when I make mistakes so that I understand what went wrong and how to correct it.

**Why this priority**: Error handling improves user experience but the calculator can function for valid inputs without it.

**Independent Test**: Can be tested by entering invalid inputs and verifying appropriate error messages are displayed.

**Acceptance Scenarios**:

1. **Given** the calculator is started, **When** I enter `10 / 0`, **Then** an error message indicating division by zero is displayed
2. **Given** the calculator is started, **When** I enter `abc + 5`, **Then** an error message indicating invalid input is displayed
3. **Given** the calculator is started, **When** I enter `5 $ 3`, **Then** an error message indicating invalid operator is displayed
4. **Given** the calculator is started, **When** I enter only `5 +`, **Then** an error message indicating incomplete expression is displayed

---

### Edge Cases

- What happens when user enters extremely large numbers? (System should handle or report overflow)
- What happens when user enters empty input? (System should prompt for valid input)
- What happens when user enters extra spaces? (System should handle gracefully, e.g., `5  +  3` works)
- What happens with very small decimal numbers? (System should maintain reasonable precision)

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST perform addition of two numbers
- **FR-002**: System MUST perform subtraction of two numbers
- **FR-003**: System MUST perform multiplication of two numbers
- **FR-004**: System MUST perform division of two numbers
- **FR-005**: System MUST support decimal numbers (floating-point) as input and output
- **FR-006**: System MUST support negative numbers in calculations
- **FR-007**: System MUST display a clear error message when division by zero is attempted
- **FR-008**: System MUST display a clear error message when non-numeric input is provided
- **FR-009**: System MUST display a clear error message when an invalid operator is used
- **FR-010**: System MUST display a clear error message when the expression is incomplete
- **FR-011**: System MUST accept input in the format: `<number> <operator> <number>`
- **FR-012**: System MUST support operators: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division)

### Assumptions

- The calculator operates on exactly two operands per calculation (no chained operations like `5 + 3 + 2`)
- Input is provided as a single line in the format `number operator number`
- The calculator runs as a single-execution command (not an interactive REPL loop)
- Precision follows standard floating-point behavior for the implementation language
- Output displays the result on a single line to stdout, errors to stderr

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can perform any of the four basic operations and receive correct results within 1 second
- **SC-002**: 100% of invalid inputs (division by zero, non-numeric, invalid operator) result in a clear, user-friendly error message rather than a crash
- **SC-003**: Users can complete a calculation in a single command invocation without additional prompts
- **SC-004**: Decimal calculations maintain at least 10 digits of precision
- **SC-005**: All error messages clearly indicate what went wrong and are understandable to non-technical users
