"""Component property as a simple callable."""

import render_antd as antd
import render as r

message_warning = r.js_arrow("message_warning", "render_antd.message.warning")


def on_click(window: r.Window):
    def result():
        window.call_js_method(message_warning("Please do not press this button!"))
        print(f"User disobeyed!")

    return result


def app(window: r.Window):
    return antd.Button(
        "Do not press this button", onClick=on_click(window), danger=True
    )
