"""Simple autorun use. See the messages in your browser console."""
from reflect import autorun
from reflect_antd import Input


def app():
    name = Input(defaultValue="John", key="name")
    autorun(lambda: print("{} => {}".format(name, name())))
    return name
