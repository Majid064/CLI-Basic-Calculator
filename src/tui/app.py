"""Terminal UI Calculator Application using Textual."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal
from textual.widgets import Button, Footer, Header, Static

from src.calculator import calculate, format_result
from src.errors import CalculatorError


class CalculatorApp(App[None]):
    """A beautiful terminal calculator TUI."""

    CSS_PATH = "styles.tcss"
    TITLE = "CLI Calculator"

    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("c", "clear", "Clear"),
        Binding("escape", "clear", "Clear", show=False),
        Binding("enter", "calculate", "Calculate"),
        Binding("=", "calculate", "=", show=False),
        Binding("backspace", "backspace", "Back", show=False),
        # Number keys
        Binding("0", "press_digit('0')", "0", show=False),
        Binding("1", "press_digit('1')", "1", show=False),
        Binding("2", "press_digit('2')", "2", show=False),
        Binding("3", "press_digit('3')", "3", show=False),
        Binding("4", "press_digit('4')", "4", show=False),
        Binding("5", "press_digit('5')", "5", show=False),
        Binding("6", "press_digit('6')", "6", show=False),
        Binding("7", "press_digit('7')", "7", show=False),
        Binding("8", "press_digit('8')", "8", show=False),
        Binding("9", "press_digit('9')", "9", show=False),
        Binding(".", "press_digit('.')", ".", show=False),
        # Operator keys
        Binding("+", "press_operator('+')", "+", show=False),
        Binding("-", "press_operator('-')", "-", show=False),
        Binding("*", "press_operator('*')", "*", show=False),
        Binding("/", "press_operator('/')", "/", show=False),
    ]

    def __init__(self) -> None:
        """Initialize the calculator app."""
        super().__init__()
        self.left_operand: str = ""
        self.operator: str = ""
        self.right_operand: str = ""
        self.result: str = ""
        self.error_message: str = ""

    def compose(self) -> ComposeResult:
        """Compose the UI layout."""
        yield Header()
        yield Container(
            Static("", id="display-expression"),
            Static("0", id="display-result"),
            Container(
                Horizontal(
                    Button("7", id="btn-7", classes="digit"),
                    Button("8", id="btn-8", classes="digit"),
                    Button("9", id="btn-9", classes="digit"),
                    Button("/", id="btn-div", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("4", id="btn-4", classes="digit"),
                    Button("5", id="btn-5", classes="digit"),
                    Button("6", id="btn-6", classes="digit"),
                    Button("*", id="btn-mul", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("1", id="btn-1", classes="digit"),
                    Button("2", id="btn-2", classes="digit"),
                    Button("3", id="btn-3", classes="digit"),
                    Button("-", id="btn-sub", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("C", id="btn-clear", classes="control"),
                    Button("0", id="btn-0", classes="digit"),
                    Button(".", id="btn-dot", classes="digit"),
                    Button("+", id="btn-add", classes="operator"),
                    classes="button-row",
                ),
                Horizontal(
                    Button("=", id="btn-equals", classes="equals"),
                    classes="button-row",
                ),
                id="button-container",
            ),
            id="calculator-body",
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        button_id = event.button.id
        if button_id is None:
            return

        if button_id == "btn-clear":
            self.action_clear()
        elif button_id == "btn-equals":
            self.action_calculate()
        elif button_id == "btn-dot":
            self._add_digit(".")
        elif button_id.startswith("btn-") and button_id[4:].isdigit():
            self._add_digit(button_id[4:])
        elif button_id in ("btn-add", "btn-sub", "btn-mul", "btn-div"):
            op_map = {"btn-add": "+", "btn-sub": "-", "btn-mul": "*", "btn-div": "/"}
            self._set_operator(op_map[button_id])

    def action_clear(self) -> None:
        """Clear the calculator state."""
        self.left_operand = ""
        self.operator = ""
        self.right_operand = ""
        self.result = ""
        self.error_message = ""
        self._update_display()

    def action_calculate(self) -> None:
        """Perform the calculation."""
        if not self.left_operand or not self.operator:
            return

        right = self.right_operand if self.right_operand else "0"

        try:
            left_val = float(self.left_operand)
            right_val = float(right)
            result_value = calculate(left_val, self.operator, right_val)
            self.result = format_result(result_value)
            self.error_message = ""
            # Set result as new left operand for chaining
            self.left_operand = self.result
            self.operator = ""
            self.right_operand = ""
        except CalculatorError as e:
            self.error_message = e.message
            self.result = ""
        except ValueError:
            self.error_message = "Invalid input"
            self.result = ""

        self._update_display()

    def action_backspace(self) -> None:
        """Delete the last character."""
        if self.right_operand:
            self.right_operand = self.right_operand[:-1]
        elif self.operator:
            self.operator = ""
        elif self.left_operand:
            self.left_operand = self.left_operand[:-1]
        self._update_display()

    def action_press_digit(self, digit: str) -> None:
        """Handle digit key press."""
        self._add_digit(digit)

    def action_press_operator(self, op: str) -> None:
        """Handle operator key press."""
        self._set_operator(op)

    def _add_digit(self, digit: str) -> None:
        """Add a digit to the current operand."""
        # Clear error state on new input
        if self.error_message:
            self.error_message = ""
            self.result = ""

        # If we have a result and no operator, start fresh
        if self.result and not self.operator:
            self.left_operand = ""
            self.result = ""

        if not self.operator:
            # Adding to left operand
            if digit == "." and "." in self.left_operand:
                return  # Already has decimal
            self.left_operand += digit
        else:
            # Adding to right operand
            if digit == "." and "." in self.right_operand:
                return  # Already has decimal
            self.right_operand += digit

        self._update_display()

    def _set_operator(self, op: str) -> None:
        """Set the operator."""
        # Clear error state
        if self.error_message:
            self.error_message = ""

        # Handle negative first operand
        if not self.left_operand and op == "-":
            self.left_operand = "-"
            self._update_display()
            return

        # If we have both operands, calculate first
        if self.left_operand and self.operator and self.right_operand:
            self.action_calculate()

        if self.left_operand:
            self.operator = op
            self.right_operand = ""
            self._update_display()

    def _update_display(self) -> None:
        """Update the display widgets."""
        # Build expression string
        parts = []
        if self.left_operand:
            parts.append(self.left_operand)
        if self.operator:
            parts.append(self.operator)
        if self.right_operand:
            parts.append(self.right_operand)

        expression = " ".join(parts)
        self.query_one("#display-expression", Static).update(expression)

        # Update result display
        result_widget = self.query_one("#display-result", Static)
        if self.error_message:
            result_widget.update(self.error_message)
            result_widget.add_class("error")
        else:
            display_value = self.result if self.result else "0"
            result_widget.update(display_value)
            result_widget.remove_class("error")


def main() -> None:
    """Run the calculator TUI."""
    app = CalculatorApp()
    app.run()


if __name__ == "__main__":
    main()
