from reflect_antd import Input, Space
from reflect_html import div
from reflect import async_formula
import anyio


def app():
    name = Input(defaultValue="John")

    async def greeting():
        await anyio.sleep(1)
        return f"Hello {name()}"

    return Space([name, div(async_formula(greeting, div("Thinking...")))])
