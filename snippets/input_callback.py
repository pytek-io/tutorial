"""Component property as a simple callable."""
from reflect import make_observable
from reflect_antd import InputNumber, Space


def farenheit_to_celsius(farenheit_value):
    return int((farenheit_value - 32) * 5 / 9)


def celsius_to_farenheit(celsius_value):
    return int(celsius_value * 9 / 5 + 32)


def app():
    INITIAL_CELSIUS_VALUE = 100
    celsius = make_observable(INITIAL_CELSIUS_VALUE)
    farenheit = make_observable(celsius_to_farenheit(INITIAL_CELSIUS_VALUE))

    return Space(
        [
            InputNumber(
                onChange=lambda c: farenheit.set(celsius_to_farenheit(c)), value=celsius
            ),
            "Celsius",
            InputNumber(
                onChange=lambda f: celsius.set(farenheit_to_celsius(f)), value=farenheit
            ),
            "Farenheit",
        ]
    )
