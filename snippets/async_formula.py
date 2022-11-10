import anyio
import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    name = antd.Input(defaultValue="John")

    async def greeting():
        await anyio.sleep(1)
        return f"Hello {name()}"

    return antd.Space(
        [name, html.div(r.async_formula(greeting, html.div("Thinking...")))]
    )
