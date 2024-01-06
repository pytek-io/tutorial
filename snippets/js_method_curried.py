"""JavaScript callbacks"""
import datetime
import random

import render as r
import render_antd as antd

filter_dates = r.js_arrow(
    "filter_dates",
    "(today, holidays, date) => date.getTime() < today || date.getDay() in [0, 6] || holidays.includes(date.getTime())",
)


def to_js_timestamp(python_date: datetime.date) -> int:
    return int(datetime.datetime(*python_date.timetuple()[:3]).timestamp()) * 1000


def app():
    today = datetime.date.today()
    holidays = r.ObservableList()

    def populate_holidays():
        holidays.set(
            sorted(
                today + datetime.timedelta(days=random.randint(1, 11)) for _ in range(3)
            )
        )

    populate_holidays()
    return antd.Space(
        [
            antd.Button("Update", type="primary", onClick=populate_holidays),
            antd.DatePicker(
                disabledDate=lambda: filter_dates(
                    today, [to_js_timestamp(d) for d in holidays]
                ),
                format="DD-MM-YYYY",
                defaultValue=to_js_timestamp(today),
            ),
            antd.Typography.Text("Holidays:"),
            lambda: [
                antd.Typography.Text(str(holiday), delete=True) for holiday in holidays
            ],
        ]
    )
