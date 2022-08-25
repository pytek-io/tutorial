"""Interdependent curried Javascript callbacks. Prevent users from selecting a duration smaller than 5 days."""
from datetime import datetime, timedelta

from reflect import create_observable
from reflect.components import JSMethod
from reflect_antd import DatePicker, Space

NB_MILLIS_DAY = 24 * 60 * 60 * 1000
MINIMUM_DAYS = 5


compare_dates = JSMethod(
    "compare_dates",
    """{
        const [timestamp1, timestamp2] = [date1.getTime(), date2.getTime()]
        return greater ? (timestamp2 + min_duration > timestamp1) : (timestamp1 + min_duration > timestamp2);
    }""",
    "date1",
    "min_duration",
    "greater",
    "date2",
)


def app():
    start_value = create_observable(datetime.now())
    end_value = create_observable(datetime.now() + timedelta(days=7))
    min_duration = NB_MILLIS_DAY * MINIMUM_DAYS
    return Space(
        [
            DatePicker(
                disabledDate=lambda: compare_dates(end_value(), min_duration, True),
                format="DD-MM-YYYY",
                value=start_value,
                placeholder="Start",
            ),
            DatePicker(
                disabledDate=lambda: compare_dates(start_value(), min_duration, False),
                format="DD-MM-YYYY",
                value=end_value,
                placeholder="End",
            ),
        ]
    )
