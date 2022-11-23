import reflect as r
import reflect_antd as antd

BUTTON_TYPES = ["Default", "Primary", "Dashed", "Text", "Link"]


def app():
    default_value = BUTTON_TYPES[0].lower()
    button_type = r.ObservableValue(default_value)
    return antd.Space(
        [
            antd.Select(
                value=button_type,
                options=[
                    {"label": value, "value": value.lower()} for value in BUTTON_TYPES
                ],
                style={"width": 100},
            ),
            antd.Button(
                "Reset",
                type=button_type,
                onClick=lambda: button_type.set(default_value),
            ),
        ]
    )
