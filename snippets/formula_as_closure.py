"""Formula defined as a closure."""
from reflect_antd import InputNumber, Space, Select
from operator import add, sub, mul, truediv, mod

OPERATIONS = {"+": add, "-": sub, "*": mul, "/": truediv, "%": mod}


def app():
    a = InputNumber(defaultValue=2)
    b = InputNumber(defaultValue=3)
    operation = Select(
        [[Select.Option(label, key=label)] for label in OPERATIONS],
        defaultValue="+",
    )

    def formula():
        return OPERATIONS[operation()](a(), b())

    return Space([a, operation, b, "=", formula])
