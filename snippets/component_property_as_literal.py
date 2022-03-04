"""Component property defined as literal"""
from reflect_antd import Button
from reflect_html import div


def app():
    return div(
        [
            Button("Default", type="default", style={"marginRight": 20}),
            Button("Primary", type="primary", style={"marginRight": 20}),
            Button("Dashed", type="dashed", style={"marginRight": 20}),
            Button("Text", type="text", style={"marginRight": 20}),
            Button("Link", type="link", style={"marginRight": 20}),
        ]
    )
