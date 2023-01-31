"""Simple Javascript callback definition."""
import reflect as r
import reflect_antd as antd

amount_formatter = r.js_arrow(
    "amount_formatter",
    "(value) => `$ ${value}`.replace(/\\B(?=(\\d{3})+(?!\\d))/g, ',')",
)


def app():
    amount_input = antd.InputNumber(defaultValue=1000, formatter=amount_formatter)
    return antd.Space([amount_input, lambda: amount_input()])
