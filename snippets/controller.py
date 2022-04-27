"""Controlled inputs, changes to those are propagated upon commit invocation."""
from reflect import Controller
from reflect_antd import Button, Space, InputNumber
from reflect_html import div


def app():
    style = {"width": 90}
    a = InputNumber(defaultValue=2, style=style, key="a")
    b = InputNumber(defaultValue=3, style=style, key="b")
    formula = lambda: "{}".format(a() * b())
    with Controller() as controller:
        return div(
            [
                Space([a, "*", b, "=", formula]),
                Space(
                    [
                        Button("OK", onClick=controller.commit, style=style),
                        div("*", style={"color": "#FFFFFF"}),
                        Button("Cancel", onClick=controller.revert, style=style),
                    ],
                    style=dict(marginTop=10),
                ),
            ],
            style={"display": "flex", "flexDirection": "column"},
        )
