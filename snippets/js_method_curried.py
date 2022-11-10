"""JavaScript callbacks"""
import datetime
import random

import reflect as r
import reflect_antd as antd

filter_dates = r.JSMethod(
    "filter_dates",
    """{
        return date.getTime() < today || date.getDay() in [0, 6] || holidays.includes(date.getTime());
    }
    """,
    "today",
    "holidays",
    "date",
)


def to_js_timestamp(python_date: datetime.date) -> int:
    return int(datetime.datetime(*python_date.timetuple()[:3]).timestamp()) * 1000


def app():
    today = datetime.date.today()
    start_value, trigger = r.create_observable(today), r.create_observable()

    @r.memoize()
    def holidays():
        trigger()
        return sorted(
            set(
                today + datetime.timedelta(days=random.randint(1, 11)) for _ in range(3)
            )
        )

    return antd.Space(
        [
            antd.Button("Update", type="primary", onClick=trigger.set),
            antd.DatePicker(
                disabledDate=filter_dates(
                    to_js_timestamp(today), [to_js_timestamp(d) for d in holidays()]
                ),
                format="DD-MM-YYYY",
                value=start_value,
                placeholder="Start",
            ),
        ]
        + [antd.Typography.Text(str(holiday), delete=True) for holiday in holidays()]
    )
