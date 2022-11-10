"""Use application hash as startup argument. Will only work on its own."""
import reflect as r
import reflect_html as html


def app():
    return html.h1(f"Hello {r.get_window().hash()}!")
