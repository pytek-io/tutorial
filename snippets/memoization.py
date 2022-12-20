"""Features a simple memoization example"""
import reflect_antd as antd

import reflect as r


def app():
    a = antd.InputNumber(defaultValue=2)
    b = antd.InputNumber(defaultValue=3)

    @r.memoize()
    def expensive_computation():
        print("evaluated formula")
        return sum(i * i for i in range(a()))

    return antd.Space([a, b, lambda: expensive_computation() * b()])
