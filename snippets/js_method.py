"""Simple Javascrip callback definition."""
import reflect_antd as antd

import reflect.components as r

amount_formatter = r.JSMethod(
    "amount_formatter",
    "return `$ ${value}`.replace(/\\B(?=(\\d{3})+(?!\\d))/g, ',')",
    "value",
)


def app():
    amount_input = antd.InputNumber(defaultValue=1000, formatter=amount_formatter)
    return antd.Space([amount_input, lambda: amount_input()])
