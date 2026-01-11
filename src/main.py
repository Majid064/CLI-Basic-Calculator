"""CLI entry point for the calculator.

This module provides the main function that serves as the entry point
for the command-line calculator.
"""

import sys

from src.calculator import calculate, format_result
from src.errors import CalculatorError
from src.parser import parse_expression


def main() -> None:
    """Main entry point for the calculator CLI.

    Parses command-line arguments, performs the calculation,
    and prints the result to stdout. Errors are printed to stderr.
    """
    try:
        args = sys.argv[1:]
        left, operator, right = parse_expression(args)
        result = calculate(left, operator, right)
        print(format_result(result))
        sys.exit(0)
    except CalculatorError as e:
        print(e.message, file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
