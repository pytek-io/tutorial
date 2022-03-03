"""Simple Javascrip callback definition."""
from reflect.components import JSMethod
from reflect_antd import Space, InputNumber

amount_formatter = JSMethod(
    "amount_formatter",
    "return `$ ${value}`.replace(/\B(?=(\d{3})+(?!\d))/g, ',')",
    "value",
)


def app():
    amount_input = InputNumber(defaultValue=1000, formatter=amount_formatter)
    return Space([amount_input, lambda: amount_input()])
