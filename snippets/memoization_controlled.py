"""Controlled memoized formula example."""
import reflect as r
import reflect_antd as antd


def app():
    with r.Controller() as controller:
        a = antd.InputNumber(defaultValue=2)
        b = antd.InputNumber(defaultValue=3)

    @r.memoize(controller=controller)
    def expensive_computation():
        print("evaluated formula")
        return sum(i * i for i in range(a()))

    return antd.Space(
        [
            antd.Button("Update", onClick=controller.commit, style={"width": 90}),
            "a =",
            a,
            "b =",
            b,
            "f(a) * b =",
            lambda: expensive_computation() * b(),
        ]
    )
