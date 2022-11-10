"""Component property defined as component."""
import reflect_ant_icons as ant_icons
import reflect_antd as antd


def app():
    return antd.Button("Settings", icon=ant_icons.SettingOutlined())
