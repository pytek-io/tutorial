"""Component property defined as component."""
from reflect_antd import Button
from reflect_ant_icons import SettingOutlined


def app():
    return Button("Settings", icon=SettingOutlined())
