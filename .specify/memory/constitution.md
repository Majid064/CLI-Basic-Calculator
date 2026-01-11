<!--
  Sync Impact Report
  ====================
  Version change: (none) → 1.0.0

  Added principles:
  - I. Type Safety First
  - II. uv Package Management
  - III. Test-First Development
  - IV. Simplicity & YAGNI
  - V. Clean Code Standards

  Added sections:
  - Technology Stack (new section)
  - Development Workflow (new section)
  - Governance (filled from template)

  Templates status:
  - .specify/templates/plan-template.md ✅ compatible (Constitution Check section aligns)
  - .specify/templates/spec-template.md ✅ compatible (requirements structure aligns)
  - .specify/templates/tasks-template.md ✅ compatible (phase structure aligns)

  Deferred items: None
-->

# Python Calculator Constitution

## Core Principles

### I. Type Safety First

All Python code MUST use type hints for function parameters, return values, and class attributes. This is non-negotiable.

- Every function signature MUST include type annotations for all parameters and return type
- Use `typing` module constructs (`Optional`, `Union`, `List`, `Dict`, etc.) where appropriate
- Class attributes MUST be annotated using class-level type hints or `dataclasses`
- Run type checking (mypy or similar) as part of the validation process
- No `Any` type unless explicitly justified and documented

**Rationale**: Type hints improve code readability, enable IDE support, catch errors early, and serve as living documentation.

### II. uv Package Management

All dependency management MUST use uv (Astral's Python package manager). pip, poetry, and other tools are not permitted for this project.

- Project MUST be initialized with `uv init`
- Dependencies MUST be added via `uv add <package>`
- Development dependencies MUST use `uv add --dev <package>`
- Virtual environments MUST be managed through uv
- Lock file (`uv.lock`) MUST be committed to version control

**Rationale**: uv provides fast, deterministic builds and modern Python project management with pyproject.toml.

### III. Test-First Development

Tests SHOULD be written before implementation when practical. Red-Green-Refactor cycle is encouraged.

- Unit tests MUST cover all calculator operations
- Edge cases (division by zero, overflow, invalid input) MUST have explicit test coverage
- Use pytest as the testing framework
- Tests MUST be runnable via `uv run pytest`

**Rationale**: Test-first development ensures requirements are clear and implementation is verifiable.

### IV. Simplicity & YAGNI

Start with the simplest solution that works. Do not add features or abstractions until needed.

- Calculator operations MUST be implemented as simple functions first
- Avoid class hierarchies unless complexity demands it
- No premature optimization
- No unused code or commented-out code in the main branch

**Rationale**: A calculator is a well-understood domain; over-engineering adds maintenance burden without benefit.

### V. Clean Code Standards

Code MUST be readable, maintainable, and follow Python conventions.

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Maximum function length: aim for < 20 lines
- Use docstrings for public functions (Google style or NumPy style)
- Run linting (ruff or flake8) before commits

**Rationale**: Clean code reduces bugs, eases onboarding, and improves long-term maintainability.

## Technology Stack

This section defines the authoritative technology choices for the project.

| Concern | Choice | Notes |
|---------|--------|-------|
| Language | Python 3.11+ | Modern Python with full type hint support |
| Package Manager | uv | Astral's fast Python package manager |
| Project Config | pyproject.toml | Standard Python project configuration |
| Testing | pytest | Industry standard, integrates with uv |
| Type Checking | mypy | Static type analysis |
| Linting | ruff | Fast, comprehensive Python linter |
| Formatting | ruff format | Consistent code formatting |

## Development Workflow

### Code Review Requirements

- All changes MUST pass type checking (`uv run mypy src/`)
- All changes MUST pass linting (`uv run ruff check .`)
- All changes MUST pass tests (`uv run pytest`)
- Pull requests SHOULD include tests for new functionality

### Quality Gates

Before merging any code:

1. ✅ Type hints present on all new functions
2. ✅ mypy passes with no errors
3. ✅ ruff check passes
4. ✅ All pytest tests pass
5. ✅ Code reviewed

## Governance

This constitution is the authoritative source for project standards. All development decisions MUST align with the principles defined here.

### Amendment Process

1. Propose changes via pull request to this file
2. Document rationale for the change
3. Obtain approval from project maintainers
4. Update version number according to semver rules

### Versioning Policy

- **MAJOR**: Removal or redefinition of core principles
- **MINOR**: New principles or sections added
- **PATCH**: Clarifications, typo fixes, non-semantic changes

### Compliance

- All code reviews MUST verify adherence to these principles
- Deviations MUST be documented with explicit justification
- See `CLAUDE.md` for runtime development guidance

**Version**: 1.0.0 | **Ratified**: 2026-01-10 | **Last Amended**: 2026-01-10
