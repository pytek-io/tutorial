"""Formula as a lambda expression"""
import reflect_antd as antd
import reflect_html as html


def app():
    name = antd.Input(defaultValue="John")
    greeting = lambda: f"Hello {name()}"
    greeting_component = html.div(greeting)
    return antd.Space([name, greeting_component])
