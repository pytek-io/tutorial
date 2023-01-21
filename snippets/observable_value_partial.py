"""Features an observable value automatically updated in the display."""
from functools import partial

import reflect as r
import reflect_antd as antd


def app():
    value = r.ObservableValue(0, key="value")
    return antd.Space(
        [
            antd.Button("+", onClick=partial(value.__iadd__, 1)),
            antd.Button("-", onClick=partial(value.__isub__, 1)),
            antd.TypographyText(value),
        ]
    )
