# Tasks: CLI Calculator

**Input**: Design documents from `/specs/001-cli-calculator/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Included per Constitution Principle III (Test-First Development)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below use single project structure per plan.md

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize Python project with uv in repository root using `uv init`
- [x] T002 Add development dependencies with `uv add --dev pytest mypy ruff`
- [x] T003 [P] Create src/__init__.py with package docstring
- [x] T004 [P] Create src/errors.py with CalculatorError base class and subclasses (DivisionByZeroError, InvalidNumberError, InvalidOperatorError, IncompleteExpressionError) per data-model.md
- [x] T005 [P] Create tests/__init__.py
- [x] T006 [P] Create tests/unit/__init__.py
- [x] T007 [P] Create tests/integration/__init__.py
- [x] T008 Configure pyproject.toml with project metadata, pytest settings, mypy strict mode, and ruff settings per quickstart.md

**Checkpoint**: Project structure ready - foundational implementation can begin

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [x] T009 Create src/calculator.py with Operator enum (ADD, SUBTRACT, MULTIPLY, DIVIDE) per data-model.md
- [x] T010 Create src/parser.py with stub function `parse_expression(args: list[str]) -> tuple[float, str, float]` that raises NotImplementedError
- [x] T011 Create src/main.py with CLI entry point stub that prints "Not implemented" and exits

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Basic Arithmetic Operations (Priority: P1)

**Goal**: Perform addition, subtraction, multiplication, and division with integer inputs

**Independent Test**: Run `uv run python -m src.main 5 + 3` and verify result `8`

### Tests for User Story 1

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T012 [P] [US1] Write unit tests for add function in tests/unit/test_calculator.py: test_add_positive_integers, test_add_with_zero
- [x] T013 [P] [US1] Write unit tests for subtract function in tests/unit/test_calculator.py: test_subtract_positive_integers, test_subtract_to_negative
- [x] T014 [P] [US1] Write unit tests for multiply function in tests/unit/test_calculator.py: test_multiply_positive_integers, test_multiply_by_zero
- [x] T015 [P] [US1] Write unit tests for divide function in tests/unit/test_calculator.py: test_divide_even, test_divide_integer_result
- [x] T016 [US1] Write integration test in tests/integration/test_cli.py: test_cli_addition, test_cli_subtraction, test_cli_multiplication, test_cli_division

### Implementation for User Story 1

- [x] T017 [P] [US1] Implement add(a: float, b: float) -> float function in src/calculator.py
- [x] T018 [P] [US1] Implement subtract(a: float, b: float) -> float function in src/calculator.py
- [x] T019 [P] [US1] Implement multiply(a: float, b: float) -> float function in src/calculator.py
- [x] T020 [P] [US1] Implement divide(a: float, b: float) -> float function in src/calculator.py (raise DivisionByZeroError if b == 0)
- [x] T021 [US1] Implement calculate(left: float, operator: str, right: float) -> float dispatcher in src/calculator.py
- [x] T022 [US1] Implement basic parse_expression in src/parser.py: split args, validate 3 tokens, parse numbers, validate operator
- [x] T023 [US1] Implement format_result(value: float) -> str in src/calculator.py: return int string if whole number, else float string
- [x] T024 [US1] Complete src/main.py: parse sys.argv[1:], call calculate, print formatted result to stdout
- [x] T025 [US1] Run `uv run pytest tests/unit/test_calculator.py -v` and verify all US1 tests pass
- [x] T026 [US1] Run `uv run pytest tests/integration/test_cli.py -v` and verify CLI tests pass

**Checkpoint**: User Story 1 complete - basic arithmetic works with integers

---

## Phase 4: User Story 2 - Decimal Number Support (Priority: P2)

**Goal**: Support decimal (floating-point) numbers in calculations

**Independent Test**: Run `uv run python -m src.main 3.5 + 2.5` and verify result `6.0`

### Tests for User Story 2

- [x] T027 [P] [US2] Write unit tests for decimal operations in tests/unit/test_calculator.py: test_add_decimals, test_subtract_decimals, test_multiply_decimals, test_divide_decimals
- [x] T028 [P] [US2] Write unit test for precision in tests/unit/test_calculator.py: test_floating_point_precision (0.1 + 0.2)
- [x] T029 [US2] Write integration test in tests/integration/test_cli.py: test_cli_decimal_addition, test_cli_decimal_division_result

### Implementation for User Story 2

- [x] T030 [US2] Verify parse_expression in src/parser.py handles decimal strings (float() already handles this - add explicit test)
- [x] T031 [US2] Update format_result in src/calculator.py to handle decimal display properly (already works with float)
- [x] T032 [US2] Run `uv run pytest -k "decimal or precision" -v` and verify all US2 tests pass

**Checkpoint**: User Story 2 complete - decimal numbers work correctly

---

## Phase 5: User Story 3 - Negative Number Support (Priority: P3)

**Goal**: Support negative numbers including double-negative expressions like `10 - -4`

**Independent Test**: Run `uv run python -m src.main -5 + 3` and verify result `-2`

### Tests for User Story 3

- [x] T033 [P] [US3] Write unit tests for negative operations in tests/unit/test_calculator.py: test_add_negative, test_subtract_negative_from_positive, test_multiply_negatives, test_divide_negative
- [x] T034 [P] [US3] Write parser tests in tests/unit/test_parser.py: test_parse_negative_first_operand, test_parse_negative_second_operand, test_parse_double_negative
- [x] T035 [US3] Write integration test in tests/integration/test_cli.py: test_cli_negative_first, test_cli_double_negative

### Implementation for User Story 3

- [x] T036 [US3] Update parse_expression in src/parser.py to handle negative number parsing (float() handles "-5" already)
- [x] T037 [US3] Verify calculate function in src/calculator.py works with negative inputs (no changes needed - float arithmetic handles this)
- [x] T038 [US3] Run `uv run pytest -k "negative" -v` and verify all US3 tests pass

**Checkpoint**: User Story 3 complete - negative numbers work correctly

---

## Phase 6: User Story 4 - Error Handling (Priority: P4)

**Goal**: Provide clear, user-friendly error messages for all invalid inputs

**Independent Test**: Run `uv run python -m src.main 10 / 0` and verify error message to stderr

### Tests for User Story 4

- [x] T039 [P] [US4] Write unit tests for error classes in tests/unit/test_errors.py: test_division_by_zero_error_message, test_invalid_number_error_message, test_invalid_operator_error_message, test_incomplete_expression_error_message
- [x] T040 [P] [US4] Write parser error tests in tests/unit/test_parser.py: test_parse_invalid_number, test_parse_invalid_operator, test_parse_incomplete_expression
- [x] T041 [US4] Write integration tests in tests/integration/test_cli.py: test_cli_division_by_zero_error, test_cli_invalid_number_error, test_cli_invalid_operator_error, test_cli_incomplete_expression_error

### Implementation for User Story 4

- [x] T042 [US4] Update parse_expression in src/parser.py to raise IncompleteExpressionError when args count != 3
- [x] T043 [US4] Update parse_expression in src/parser.py to raise InvalidNumberError when float() fails
- [x] T044 [US4] Update parse_expression in src/parser.py to raise InvalidOperatorError when operator not in {+, -, *, /}
- [x] T045 [US4] Update src/main.py to catch CalculatorError, print message to stderr, exit with code 1
- [x] T046 [US4] Run `uv run pytest -k "error" -v` and verify all US4 tests pass
- [x] T047 [US4] Manually test all error cases per contracts/cli-interface.md examples

**Checkpoint**: User Story 4 complete - all error cases handled gracefully

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Quality assurance and final validation

- [x] T048 [P] Add docstrings to all public functions in src/calculator.py following Google style
- [x] T049 [P] Add docstrings to all public functions in src/parser.py following Google style
- [x] T050 [P] Add docstrings to error classes in src/errors.py following Google style
- [x] T051 Run `uv run mypy src/` and fix any type errors
- [x] T052 Run `uv run ruff check .` and fix any linting issues
- [x] T053 Run `uv run ruff format .` to ensure consistent formatting
- [x] T054 Run `uv run pytest` and verify all tests pass (should be 100% pass rate)
- [x] T055 Run quickstart.md validation checklist manually
- [x] T056 Commit all changes with message "feat(calculator): implement CLI calculator with full test coverage"

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User Story 1 (P1): Can start after Phase 2
  - User Story 2 (P2): Can start after Phase 2 (independent of US1)
  - User Story 3 (P3): Can start after Phase 2 (independent of US1, US2)
  - User Story 4 (P4): Can start after Phase 2 (independent of US1, US2, US3)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

All user stories are **independent** and can be developed in parallel after Phase 2:
- **US1**: Basic arithmetic - no dependencies on other stories
- **US2**: Decimal support - no dependencies (builds on same functions)
- **US3**: Negative numbers - no dependencies (builds on same parser)
- **US4**: Error handling - no dependencies (adds error paths)

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Implementation follows test requirements
- Story complete when all story tests pass

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T003-T007)
- All tests for a user story marked [P] can run in parallel
- Implementation functions marked [P] can run in parallel (T017-T020)
- Different user stories can be worked on in parallel after Phase 2

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Write unit tests for add function in tests/unit/test_calculator.py"
Task: "Write unit tests for subtract function in tests/unit/test_calculator.py"
Task: "Write unit tests for multiply function in tests/unit/test_calculator.py"
Task: "Write unit tests for divide function in tests/unit/test_calculator.py"

# Launch all operation implementations together:
Task: "Implement add function in src/calculator.py"
Task: "Implement subtract function in src/calculator.py"
Task: "Implement multiply function in src/calculator.py"
Task: "Implement divide function in src/calculator.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test with `5 + 3`, `10 - 4`, `6 * 7`, `20 / 4`
5. Deploy/demo if ready - MVP is functional!

### Incremental Delivery

1. Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → **MVP Complete**
3. Add User Story 2 → Test with decimals → Enhanced
4. Add User Story 3 → Test with negatives → Full arithmetic
5. Add User Story 4 → Test error cases → Production ready
6. Polish → Type check, lint, format → Ship it!

### Full Sequential (Recommended)

Execute phases 1-7 in order. Each phase builds on the previous. Total estimated tasks: 56.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each phase or logical group
- Stop at any checkpoint to validate story independently
