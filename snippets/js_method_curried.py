"""JavaScript callbacks"""
from datetime import date, datetime, timedelta
from random import randint

from reflect import create_observable, memoize
from reflect.components import JSMethod
from reflect_antd import Button, DatePicker, Space, Typography

filter_dates = JSMethod(
    "filter_dates",
    """{
        return date.getTime() < today || date.getDay() in [0, 6] || holidays.includes(date.getTime());
    }
    """,
    "today",
    "holidays",
    "date",
)


def to_js_timestamp(python_date: date) -> int:
    return int(datetime(*python_date.timetuple()[:3]).timestamp()) * 1000


def app():
    today = date.today()
    start_value, trigger = create_observable(today), create_observable()

    @memoize()
    def holidays():
        trigger()
        return sorted(set(today + timedelta(days=randint(1, 11)) for _ in range(3)))

    return Space(
        [
            Button("Update", type="primary", onClick=trigger.set),
            DatePicker(
                disabledDate=filter_dates(
                    to_js_timestamp(today), [to_js_timestamp(d) for d in holidays()]
                ),
                format="DD-MM-YYYY",
                value=start_value,
                placeholder="Start",
            ),
        ]
        + [Typography.Text(str(holiday), delete=True) for holiday in holidays()]
    )
