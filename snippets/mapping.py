"""Features a mapping allowing to create self containing computation rows"""

import render as r
import render_antd as antd
import render_html as html


def app():
    style = {"width": 90}
    actual_row_values = [{"a": 2, "b": 3}]
    row_content_values = r.ObservableList[r.DictOfObservables](
        actual_row_values, key="values", constructor=r.DictOfObservables
    )

    def create_new_row(row_content_value):
        print("called create_new_row", row_content_value)
        a = antd.InputNumber(value=row_content_value["a"], style=style, key="a")
        b = antd.InputNumber(value=row_content_value["b"], style=style, key="b")
        return antd.Space([a, "*", b, "=", lambda: a() * b()], style={"marginTop": 10})

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
