"""Simple autorun use. See the messages in your browser console."""
import reflect_antd as antd

import reflect as r


def app():
    name = antd.Input(defaultValue="John", key="name")
    r.autorun(lambda: print(f"{name} => {name()}"))
    return name
