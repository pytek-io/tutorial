"""Controlled inputs, changes to those are propagated upon commit invocation."""
import render as r
import render_antd as antd
import render_html as html


def app(_):
    style = {"width": 90}
    formula = lambda: f"{a() * b()}"
    with r.Controller() as controller:
        a = antd.InputNumber(defaultValue=2, style=style, key="a")
        b = antd.InputNumber(defaultValue=3, style=style, key="b")
    return html.div(
        [
            antd.Space([a, "*", b, "=", formula]),
            antd.Space(
                [
                    antd.Button("Cancel", onClick=controller.revert, style=style),
                    html.div("*", style={"color": "#FFFFFF"}),
                    antd.Button("OK", onClick=controller.commit, style=style),
                ],
                style={"marginTop": 10},
            ),
        ],
        style={"display": "flex", "flexDirection": "column"},
    )
