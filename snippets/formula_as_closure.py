"""Formula defined as a closure."""
import operator

import reflect_antd as antd

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
        options=[[{"children": label, "key": label}] for label in OPERATIONS],
        defaultValue="+",
    )

    def formula():
        return OPERATIONS[operation()](a(), b())

    return antd.Space([a, operation, b, "=", formula])
