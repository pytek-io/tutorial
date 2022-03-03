"""Formula as a lambda expression"""
from reflect_antd import Input, Space
from reflect_html import div


def app():
    name = Input(defaultValue="John")
    greeting = lambda: f"Hello {name()}"
    greeting_component = div(greeting)
    return Space([name, greeting_component])
