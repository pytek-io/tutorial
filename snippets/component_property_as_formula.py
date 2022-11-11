"""Component property as a formula."""
import reflect_antd as antd


def app():
    level = antd.Slider(min=1, max=5, defaultValue=1, key="level", style={"width": 100})
    title = antd.Typography.Title("Lorem Ipsum", level=level)
    return antd.Space([level, title])
