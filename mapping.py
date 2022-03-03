"""Features a depth one mapping allowing to create self containing computation rows"""
from reflect import Mapping, make_observable
from reflect_antd import Button, InputNumber, Space
from reflect_html import div


def app():
    style = dict(width=90)
    actual_row_values = [{"a": 2, "b": 3}]
    row_content_values = make_observable(
        actual_row_values,
        depth=3,
        key="values",
    )

    def create_new_row(row_content_value):
        print("called create_new_row")
        a = InputNumber(value=row_content_value["a"], style=style, key="a")
        b = InputNumber(value=row_content_value["b"], style=style, key="b")
        return Space([a, "*", b, "=", lambda: a() * b()], style=dict(marginTop=10))

    return div(
        [
            Button(
                "Add row",
                style=style,
                onClick=lambda: row_content_values.append({"a": 2, "b": 3}),
            ),
            Mapping(create_new_row, row_content_values, key="mapping"),
        ],
        style={"display": "flex", "flexDirection": "column"},
    )
