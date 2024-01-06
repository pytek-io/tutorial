"""Features an observable value automatically updated in the display."""
import render as r
import render_antd as antd


def app():
    value = r.ObservableValue(0, key="value")
    return antd.Space(
        [
            antd.Button("+", onClick=lambda: value.__iadd__(1)),
            antd.Button("-", onClick=lambda: value.__isub__(1)),
            antd.TypographyText(value),
        ]
    )
