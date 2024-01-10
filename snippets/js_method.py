"""Simple Javascript callback definition."""
import render as r
import render_antd as antd

amount_formatter = r.js_arrow(
    "amount_formatter",
    "(value) => `$ ${value}`.replace(/\\B(?=(\\d{3})+(?!\\d))/g, ',')",
)


def app(_):
    amount_input = antd.InputNumber(defaultValue=1000, formatter=amount_formatter)
    return antd.Space([amount_input, amount_input.evaluate])
