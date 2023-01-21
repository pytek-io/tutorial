"""Simple autorun use. See the messages in your browser console."""
import reflect as r
import reflect_antd as antd


def app():
    name = antd.Input(defaultValue="John", key="name")
    r.autorun(lambda: print(f"{name} => {name()}"))
    return name
