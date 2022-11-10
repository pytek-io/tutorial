"""Component property defined as literal"""
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Button("Default", type="default", style={"marginRight": 20}),
            antd.Button("Primary", type="primary", style={"marginRight": 20}),
            antd.Button("Dashed", type="dashed", style={"marginRight": 20}),
            antd.Button("Text", type="text", style={"marginRight": 20}),
            antd.Button("Link", type="link", style={"marginRight": 20}),
        ]
    )
