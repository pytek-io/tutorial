import render as r
import render_antd as antd


def app(_):
    value = r.ObservableValue(1, key="value")

    def increment(increment):
        nonlocal value
        value.set(value() + increment)

    return antd.Space(
        [
            antd.Button("+", onClick=lambda: increment(1)),
            antd.Button("-", onClick=lambda: increment(-1)),
            antd.Badge(count=value),
        ]
    )
