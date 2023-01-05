"""Use application hash as startup argument. Will only work on its own."""
import reflect_html as html

import reflect as r


def app(window: r.Window):
    return html.h1(lambda: f"Hello {window.hash()}!")