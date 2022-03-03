"""Features a simple memoization example"""
from reflect import memoize
from reflect_antd import Space, InputNumber


def app():
    a = InputNumber(defaultValue=2)
    b = InputNumber(defaultValue=3)

    @memoize()
    def expensive_computation():
        print("evaluated formula")
        return sum(i * i for i in range(a()))

    return Space([a, b, lambda: expensive_computation() * b()])
