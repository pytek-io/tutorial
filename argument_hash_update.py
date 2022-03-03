"""App hash kept in sync, allowing state to be recorded in browser history. Will only work on its own."""
from reflect_antd import Input, Row, Col
from reflect import get_window


def app():
    window = get_window()
    name = Input(value=window.hash)
    greeting = lambda: f"Hello {window.hash()}"
    col_name = Col(name)
    col_greeting = Col(greeting)
    return Row([col_name, col_greeting], gutter=10)
