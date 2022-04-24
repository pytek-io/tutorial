"""App hash kept in sync, allowing state to be recorded in browser history. Will only work on its own."""
from reflect_antd import Input, Row, Col
from reflect import get_window


def app():
    hash_argument = get_window().hash
    name = Input(value=hash_argument)
    greeting = lambda: f"Hello {hash_argument()}"
    col_name = Col(name)
    col_greeting = Col(greeting)
    return Row([col_name, col_greeting], gutter=10)
