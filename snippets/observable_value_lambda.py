"""Features an observable value automatically updated in the display."""
import render as r
import render_antd as antd


def app(_):
    value = r.ObservableValue(1, key="value")
    return antd.Space(
        [
            antd.Button("+", onClick=lambda: value.__iadd__(1)),
            antd.Button("-", onClick=lambda: value.__isub__(1)),
            antd.Badge(count=value),
        ]
    )
