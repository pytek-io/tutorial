"""Component property as a simple callable."""
from reflect_antd import Button, message


def on_click():
    message.warning("Please do not press this button again!")
    print(f"User disobeyed!")


def app():
    return Button("Do not press this button", onClick=on_click, type="danger")
