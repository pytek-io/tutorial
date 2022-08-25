"""Features a simple async callback, requires httpx."""
import json
from datetime import datetime

import httpx
from reflect import create_observable
from reflect_antd import Button, Space

WORLD_TIME_URL = "http://worldtimeapi.org/api/timezone/Europe/London"


def app():
    time = create_observable("", key="time")

    async def on_click():
        async with httpx.AsyncClient() as client:
            time.set("refreshing...")
            reply = await client.get(WORLD_TIME_URL)
            time.set(str(datetime.fromtimestamp(json.loads(reply.content)["unixtime"])))

    return Space([Button("Refresh", onClick=on_click), time])
