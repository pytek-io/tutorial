"""Features a simple async callback, requires httpx."""
import datetime
import json

import httpx
import reflect_antd as antd

import reflect as r

WORLD_TIME_URL = "http://worldtimeapi.org/api/timezone/Europe/London"


def app():
    time = r.create_observable("", key="time")

    async def on_click():
        async with httpx.AsyncClient() as client:
            time.set("refreshing...")
            reply = await client.get(WORLD_TIME_URL)
            time.set(
                str(
                    datetime.datetime.fromtimestamp(
                        json.loads(reply.content)["unixtime"]
                    )
                )
            )

    return antd.Space([antd.Button("Refresh", onClick=on_click), time])
