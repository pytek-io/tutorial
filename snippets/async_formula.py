import anyio
import render as r
import render_antd as antd
import render_html as html


def app(_):
    name = antd.Input(defaultValue="John")

    async def greeting():
        await anyio.sleep(1)
        return f"Hello {name()}"

    return antd.Space(
        [
            name,
            html.div(
                r.AsyncCachedEvaluation(greeting, loading_value="Thinking...")
            ),
        ]
    )
