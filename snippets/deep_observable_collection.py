"""Features an example of nested observable data"""
import reflect as r
import reflect_antd as antd

DIMENSION_STYLE = {"width": 70}
MATERIAL_STYLE = {"width": 120}
PRICE_STYLE = {"width": 60}
ROW_STYLE = {"marginTop": 8}
WOODS = [
    {"value": "w_0134", "label": "Walnut"},
    {"value": "w_0143", "label": "Chestnut"},
]
PRICES = {"w_0134": 0.789, "w_0143": 0.345}
DEFAULT_VALUES = {"l": 200, "w": 300, "m": WOODS[0]["value"]}
COL_SPANS = [4, 4, 8, 8]


def create_new_row(content_obs):
    length = antd.InputNumber(value=content_obs["l"], style=DIMENSION_STYLE)
    width = antd.InputNumber(value=content_obs["w"], style=DIMENSION_STYLE)
    wood = antd.Select(options=WOODS, value=content_obs["m"], style=MATERIAL_STYLE)
    price = antd.TypographyText(
        lambda: f"{length() * width() * PRICES[wood()] / 100.0: .2f}", style=PRICE_STYLE
    )
    return antd.Space([length, width, wood, price])


def app():
    rows = [DEFAULT_VALUES.copy()]
    rows_obs = r.ObservableList[r.DictOfObservables](rows, key="row_content")
    return antd.Space(
        [
            r.Mapping(create_new_row, rows_obs),
            antd.Button(
                "+",
                style=DIMENSION_STYLE,
                onClick=lambda: rows_obs.append(DEFAULT_VALUES.copy()),
            ),
        ],
        direction="vertical",
    )
