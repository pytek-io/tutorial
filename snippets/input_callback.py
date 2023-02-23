"""Two input components kept in sync."""
import reflect_antd as antd

INITIAL_CELSIUS_VALUE = 100


def app():
    farenheit_to_celsius = lambda f: None if f is None else int((f - 32) * 5 / 9)
    celsius_to_farenheit = lambda c: None if c is None else int(c * 9 / 5 + 32)
    celsius = antd.InputNumber(
        defaultValue=INITIAL_CELSIUS_VALUE,
        onChange=lambda c: farenheit.set(celsius_to_farenheit(c)),
    )
    farenheit = antd.InputNumber(
        defaultValue=celsius_to_farenheit(INITIAL_CELSIUS_VALUE),
        onChange=lambda f: celsius.set(farenheit_to_celsius(f)),
    )
    return antd.Space([celsius, "°C", farenheit, "°F"])
