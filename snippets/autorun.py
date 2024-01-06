"""Simple autorun use. See the messages in your browser console."""
import render as r
import render_antd as antd


def app():
    name = antd.Input(defaultValue="John", key="name")
    r.autorun(lambda: print(f"{name} => {name()}"))
    return name
