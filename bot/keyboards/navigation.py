"""Navigation keyboards for the bot."""

from typing import List


def _build_keyboard(button_rows: List[List[str]]) -> List[List[str]]:
    """Simple helper to build a keyboard representation.

    The functions in this module return a list of rows, where each row is a
    list of button labels.  It is a lightweight stand‑in for a real Telegram
    keyboard object so that the project does not require any external
    dependencies.  The structure can later be converted to a framework
    specific keyboard markup.
    """

    return button_rows


def main_menu() -> List[List[str]]:
    """Return the main menu keyboard."""
    return _build_keyboard([
        ["Start", "Help"],
        ["Settings"],
    ])


def back_menu() -> List[List[str]]:
    """Return a keyboard with a single Back button."""
    return _build_keyboard([["Back"]])


def yes_no_menu() -> List[List[str]]:
    """Return a keyboard with Yes and No options."""
    return _build_keyboard([["Yes", "No"]])
