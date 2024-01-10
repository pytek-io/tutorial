"""Component property defined as component."""
import render_ant_icons as ant_icons
import render_antd as antd


def app(_):
    return antd.Button("Settings", icon=ant_icons.SettingOutlined())
