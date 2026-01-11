"""Integration tests for CLI calculator."""

import subprocess
import sys


def run_calculator(*args: str) -> tuple[str, str, int]:
    """Run the calculator CLI with given arguments.

    Args:
        *args: Command-line arguments to pass to the calculator.

    Returns:
        Tuple of (stdout, stderr, return_code).
    """
    result = subprocess.run(
        [sys.executable, "-m", "src.main", *args],
        capture_output=True,
        text=True,
        cwd=".",
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


# T016: Integration tests for User Story 1
class TestCLIBasicArithmetic:
    """Integration tests for basic arithmetic operations."""

    def test_cli_addition(self) -> None:
        """Test CLI addition: 5 + 3 = 8."""
        stdout, stderr, code = run_calculator("5", "+", "3")
        assert code == 0
        assert stdout == "8"
        assert stderr == ""

    def test_cli_subtraction(self) -> None:
        """Test CLI subtraction: 10 - 4 = 6."""
        stdout, stderr, code = run_calculator("10", "-", "4")
        assert code == 0
        assert stdout == "6"
        assert stderr == ""

    def test_cli_multiplication(self) -> None:
        """Test CLI multiplication: 6 * 7 = 42."""
        stdout, stderr, code = run_calculator("6", "*", "7")
        assert code == 0
        assert stdout == "42"
        assert stderr == ""

    def test_cli_division(self) -> None:
        """Test CLI division: 20 / 4 = 5."""
        stdout, stderr, code = run_calculator("20", "/", "4")
        assert code == 0
        assert stdout == "5"
        assert stderr == ""


# T029: Integration tests for User Story 2 (Decimal Support)
class TestCLIDecimalSupport:
    """Integration tests for decimal number support."""

    def test_cli_decimal_addition(self) -> None:
        """Test CLI decimal addition: 3.5 + 2.5 = 6."""
        stdout, stderr, code = run_calculator("3.5", "+", "2.5")
        assert code == 0
        # Whole number results display without decimal per spec
        assert stdout == "6"
        assert stderr == ""

    def test_cli_decimal_division_result(self) -> None:
        """Test CLI division with decimal result: 10 / 4 = 2.5."""
        stdout, stderr, code = run_calculator("10", "/", "4")
        assert code == 0
        assert stdout == "2.5"
        assert stderr == ""

    def test_cli_floating_point_addition(self) -> None:
        """Test CLI with 0.1 + 0.2."""
        stdout, stderr, code = run_calculator("0.1", "+", "0.2")
        assert code == 0
        # Accept either exact or floating-point representation
        assert stdout.startswith("0.3")
        assert stderr == ""


# T035: Integration tests for User Story 3 (Negative Numbers)
class TestCLINegativeNumbers:
    """Integration tests for negative number support."""

    def test_cli_negative_first(self) -> None:
        """Test CLI with negative first operand: -5 + 3 = -2."""
        stdout, stderr, code = run_calculator("-5", "+", "3")
        assert code == 0
        assert stdout == "-2"
        assert stderr == ""

    def test_cli_double_negative(self) -> None:
        """Test CLI with double negative: 10 - -4 = 14."""
        stdout, stderr, code = run_calculator("10", "-", "-4")
        assert code == 0
        assert stdout == "14"
        assert stderr == ""

    def test_cli_negative_multiplication(self) -> None:
        """Test CLI with negative multiplication: -6 * -7 = 42."""
        stdout, stderr, code = run_calculator("-6", "*", "-7")
        assert code == 0
        assert stdout == "42"
        assert stderr == ""

    def test_cli_negative_division(self) -> None:
        """Test CLI with negative division: -20 / 4 = -5."""
        stdout, stderr, code = run_calculator("-20", "/", "4")
        assert code == 0
        assert stdout == "-5"
        assert stderr == ""


# T041: Integration tests for User Story 4 (Error Handling)
class TestCLIErrorHandling:
    """Integration tests for error handling."""

    def test_cli_division_by_zero_error(self) -> None:
        """Test CLI division by zero error."""
        stdout, stderr, code = run_calculator("10", "/", "0")
        assert code == 1
        assert stdout == ""
        assert "Cannot divide by zero" in stderr

    def test_cli_invalid_number_error(self) -> None:
        """Test CLI invalid number error."""
        stdout, stderr, code = run_calculator("abc", "+", "5")
        assert code == 1
        assert stdout == ""
        assert "not a valid number" in stderr
        assert "abc" in stderr

    def test_cli_invalid_operator_error(self) -> None:
        """Test CLI invalid operator error."""
        stdout, stderr, code = run_calculator("5", "$", "3")
        assert code == 1
        assert stdout == ""
        assert "not a valid operator" in stderr
        assert "$" in stderr

    def test_cli_incomplete_expression_error(self) -> None:
        """Test CLI incomplete expression error."""
        stdout, stderr, code = run_calculator("5", "+")
        assert code == 1
        assert stdout == ""
        assert "Incomplete expression" in stderr
