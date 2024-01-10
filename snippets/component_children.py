"""Simple child/parent relationship example."""
import render_html as html


def app(_):
    str_child = html.div("Lorem Ipsum")
    int_child = html.div(100)
    float_child = html.div(1.234)
    parent = html.div([str_child, int_child, float_child])
    return parent
