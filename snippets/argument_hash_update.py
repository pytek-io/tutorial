"""App hash kept in sync, allowing state to be recorded in browser history. Will only work on its own."""
import render as r
import render_antd as antd


def app():
    hash_argument = r.get_window().hash
    name = antd.Input(value=hash_argument)
    greeting = lambda: f"Hello {hash_argument()}"
    col_name = antd.Col(name)
    col_greeting = antd.Col(greeting)
    return antd.Row([col_name, col_greeting], gutter=10)
