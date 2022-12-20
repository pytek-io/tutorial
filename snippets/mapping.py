"""Features a depth one mapping allowing to create self containing computation rows"""
import reflect_antd as antd
import reflect_html as html
from typing import Dict

import reflect as r


def app():
    style = dict(width=90)
    actual_row_values = [{"a": 2, "b": 3}]
    row_content_values = r.ObservableList[r.ObservableDict](actual_row_values, key="values")

    def create_new_row(row_content_value):
        print("called create_new_row", row_content_value)
        a = antd.InputNumber(value=row_content_value["a"], style=style, key="a")
        b = antd.InputNumber(value=row_content_value["b"], style=style, key="b")
        return antd.Space([a, "*", b, "=", lambda: a() * b()], style=dict(marginTop=10))

    return html.div(
        [
            antd.Button(
                "Add row",
                style=style,
                onClick=lambda: row_content_values.append({"a": 2, "b": 3}),
            ),
            r.Mapping(
                create_new_row,
                row_content_values,
                key="mapping",
                evaluate_argument=False,
            ),
        ],
        style={"display": "flex", "flexDirection": "column"},
    )


app()
