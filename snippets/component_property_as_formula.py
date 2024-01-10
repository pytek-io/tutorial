"""Component property as a formula."""
import render_antd as antd


def app(_):
    level = antd.Slider(min=1, max=5, defaultValue=1, key="level", style={"width": 100})
    title = antd.Typography.Title("Lorem Ipsum", level=level)
    return antd.Space([level, title])
