"""Formula defined as a closure."""
import operator

import render_antd as antd

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
}


def app():
    a = antd.InputNumber(defaultValue=2)
    b = antd.InputNumber(defaultValue=3)
    operation = antd.Select(
        options=[{"title": label, "value": label} for label in OPERATIONS],
        defaultValue="+",
    )

    def formula():
        return OPERATIONS[operation()](a(), b())

    return antd.Space([a, operation, b, "=", formula])
