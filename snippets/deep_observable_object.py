"""Features an example of deep observable data"""
import reflect as r
import reflect_antd as antd
import reflect_html as html


class Row:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


def app():
    style = {"width": 90}
    actual_row_values = [Row(2, 3)]
    row_content_observables = r.create_observable(
        actual_row_values, depth=3, key="values"
    )

    def create_new_row(row_content_observable):
        a = antd.InputNumber(value=row_content_observable.a, style=style, key="a")
        b = antd.InputNumber(value=row_content_observable.b, style=style, key="b")
        return antd.Space([a, "*", b, "=", lambda: a() * b()], style=dict(marginTop=10))

    return html.div(
        [
            antd.Button(
                "Add row",
                style=style,
                onClick=lambda: row_content_observables.append(Row(2, 3)),
            ),
            lambda: [
                create_new_row(row_content_value)
                for row_content_value in row_content_observables
            ],
        ],
        style={"display": "flex", "flexDirection": "column"},
    )
