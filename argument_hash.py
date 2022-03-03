"""Use application hash as startup argument. Will only work on its own."""
from reflect import get_window
from reflect_html import h1


def app():
    return h1(
        f"Hello {get_window().hash()}!",
    )
