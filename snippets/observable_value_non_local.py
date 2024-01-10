"""Features an observable value automatically updated in the display."""
import render as r
import render_antd as antd


def app(_):
    value = r.ObservableValue(0, key="value")

    def increment(increment):
        nonlocal value
        value.set(value() + increment)

    return antd.Space(
        [
            antd.Button("+", onClick=lambda: increment(1)),
            antd.Button("-", onClick=lambda: increment(-1)),
            antd.TypographyText(value),
        ]
    )
