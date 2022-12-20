"""Use application hash as startup argument. Will only work on its own."""
import reflect_html as html

import reflect as r


def app():
    return html.h1(f"Hello {r.get_window().hash()}!")
