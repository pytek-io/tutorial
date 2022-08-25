"""Features an example of deep observable data"""
from reflect import create_observable
from reflect_antd import Button, InputNumber, Space
from reflect_html import div


class Row:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


def app():
    style = {"width": 90}
    actual_row_values = [Row(2, 3)]
    row_content_observables = create_observable(actual_row_values, depth=3, key="values")

    def create_new_row(row_content_observable):
        a = InputNumber(value=row_content_observable.a, style=style, key="a")
        b = InputNumber(value=row_content_observable.b, style=style, key="b")
        return Space([a, "*", b, "=", lambda: a() * b()], style=dict(marginTop=10))

    return div(
        [
            Button(
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
