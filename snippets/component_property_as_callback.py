"""Component property as a simple callable."""
import render_antd as antd


def on_click():
    antd.message.warning("Please do not press this button again!")
    print(f"User disobeyed!")


def app():
    return antd.Button("Do not press this button", onClick=on_click, danger=True)
