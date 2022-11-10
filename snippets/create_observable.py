"""Features an observable value automatically updated in the display."""
import reflect as r
import reflect_antd as antd


def app():
    value = r.create_observable(0, key="value")

    def increment(inc_or_dec):
        nonlocal value
        value.set(value() + (1 if inc_or_dec else -1))

    return antd.Space(
        [
            antd.Button("+", onClick=lambda: increment(True)),
            antd.Button("-", onClick=lambda: increment(False)),
            value,
        ]
    )
