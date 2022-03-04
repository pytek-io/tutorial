"""Formula defined as a bound method."""
from reflect_antd import InputNumber, Space, Select
from operator import add, sub, mul, truediv, mod

OPERATIONS = {"+": add, "-": sub, "*": mul, "/": truediv, "%": mod}


class Calculator:
    def __init__(self) -> None:
        self.a = InputNumber(defaultValue=2)
        self.b = InputNumber(defaultValue=3)
        self.operation = Select(
            [[Select.Option(label, key=label)] for label in OPERATIONS],
            defaultValue="+",
        )

    def value(self):
        return OPERATIONS[self.operation()](self.a(), self.b())


def app():
    calc = Calculator()
    return Space([calc.a, calc.operation, calc.b, "=", calc.value])
