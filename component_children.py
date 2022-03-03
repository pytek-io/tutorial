"""Simple child/parent relationship example."""
from reflect_html import div


def app():
    str_child = div("Lorem Ipsum")
    int_child = div(100)
    float_child = div(1.234)
    parent = div([str_child, int_child, float_child])
    return parent