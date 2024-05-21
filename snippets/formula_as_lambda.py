"""Formula as a lambda expression"""
import render_antd as antd


def app(_):
    name = antd.Input(defaultValue="John")
    greeting = lambda: f"Hello {name()}"
    greeting_component = antd.Typography.Text(greeting)
    return antd.Space([name, greeting_component])
