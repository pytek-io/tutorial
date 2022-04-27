"""Two input components kept in sync."""
from reflect_antd import InputNumber, Space

INITIAL_CELSIUS_VALUE = 100


def app():
    farenheit_to_celsius = lambda f: int((f - 32) * 5 / 9)
    celsius_to_farenheit = lambda c: int(c * 9 / 5 + 32)
    celsius = InputNumber(
        defaultValue=INITIAL_CELSIUS_VALUE,
        onChange=lambda c: farenheit.set(celsius_to_farenheit(c)),
    )
    farenheit = InputNumber(
        defaultValue=celsius_to_farenheit(INITIAL_CELSIUS_VALUE),
        onChange=lambda f: celsius.set(farenheit_to_celsius(f)),
    )
    return Space([celsius, "°C", farenheit, "°F"])
