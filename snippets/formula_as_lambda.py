"""Formula as a lambda expression"""
import render_antd as antd


def app():
    name = antd.Input(defaultValue="John")
    greeting = lambda: f"Hello {name()}"
    greeting_component = antd.TypographyText(greeting)
    return antd.Space([name, greeting_component])
