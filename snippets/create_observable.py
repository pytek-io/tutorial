"""Features an observable value automatically updated in the display."""
from reflect import create_observable
from reflect_antd import Button, Space


def app():
    value = create_observable(0, key="value")

    def increment(inc_or_dec):
        nonlocal value
        value.set(value() + (1 if inc_or_dec else -1))

    return Space(
        [
            Button("+", onClick=lambda: increment(True)),
            Button("-", onClick=lambda: increment(False)),
            value,
        ]
    )
