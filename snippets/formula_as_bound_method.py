"""Formula defined as a bound method."""
import operator

import reflect_antd as antd

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
}


class Calculator:
    def __init__(self) -> None:
        self.a = antd.InputNumber(defaultValue=2)
        self.b = antd.InputNumber(defaultValue=3)
        self.operation = antd.Select(
            options=[{"title": label, "value": label} for label in OPERATIONS],
            defaultValue="+",
        )

    def value(self):
        return OPERATIONS[self.operation()](self.a(), self.b())


def app():
    calc = Calculator()
    return antd.Space([calc.a, calc.operation, calc.b, "=", calc.value])
