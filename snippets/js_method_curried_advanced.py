"""Interdependent curried Javascript callbacks. Prevent users from selecting a duration smaller than 5 days."""
import datetime

import render as r
import render_antd as antd

NB_MILLIS_DAY = 24 * 60 * 60 * 1000
MINIMUM_DAYS = 5
compare_dates = r.js_arrow(
    "compare_dates",
    """(date1, min_duration, greater, date2) => {
        const [timestamp1, timestamp2] = [date1.getTime(), date2.getTime()]
        return greater ? (timestamp2 + min_duration > timestamp1) : (timestamp1 + min_duration > timestamp2);
    }""",
)


def app(_):
    start_value = r.create_observable(datetime.datetime.now())
    end_value = r.create_observable(
        datetime.datetime.now() + datetime.timedelta(days=7)
    )
    min_duration = NB_MILLIS_DAY * MINIMUM_DAYS
    return antd.Space(
        [
            antd.DatePicker(
                disabledDate=lambda: compare_dates(end_value(), min_duration, True),
                format="DD-MM-YYYY",
                value=start_value,
                placeholder="Start",
            ),
            antd.DatePicker(
                disabledDate=lambda: compare_dates(start_value(), min_duration, False),
                format="DD-MM-YYYY",
                value=end_value,
                placeholder="End",
            ),
        ]
    )
