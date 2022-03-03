"""Component property as a formula."""
from reflect_antd import Slider, Typography
from reflect_html import div


def app():
    level = Slider(min=1, max=5, defaultValue=1, key="level", style={"width": 100})
    title = Typography.Title("Lorem Ipsum", level=level)
    return div([level, title])
