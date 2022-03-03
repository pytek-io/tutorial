"""Controlled memoized formula example."""
from reflect import memoize, Controller
from reflect_antd import Button, Space, InputNumber


def app():
    controller = Controller()
    a = InputNumber(defaultValue=2)
    b = InputNumber(defaultValue=3)

    @memoize(controller=controller)
    def expensive_computation():
        print("evaluated formula")
        return sum(i * i for i in range(a()))

    return Space(
        [
            Button("Update", onClick=controller.commit, style={"width": 90}),
            a,
            b,
            lambda: expensive_computation() * b(),
        ]
    )
