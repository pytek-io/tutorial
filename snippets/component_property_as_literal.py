"""Component property defined as literal"""
import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Button("Default", type="default", style={"marginRight": 20}),
            antd.Button("Primary", type="primary", style={"marginRight": 20}),
            antd.Button("Dashed", type="dashed", style={"marginRight": 20}),
            antd.Button("Text", type="text", style={"marginRight": 20}),
            antd.Button("Link", type="link", style={"marginRight": 20}),
        ]
    )
