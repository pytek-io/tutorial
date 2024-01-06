"""Use application hash as startup argument. Will only work on its own."""
import render as r
import render_html as html


def app(window: r.Window):
    return html.h1(lambda: f"Hello {window.hash()}!")
