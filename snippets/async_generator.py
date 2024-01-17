"""Child defined as an async generator from BTC quotes."""
import json

import render_antd as antd
from demos.connection import ws_connection_manager

URI = "wss://test.deribit.com/ws/api/v2"
BTC_UPDATES_REQUEST = {
    "jsonrpc": "2.0",
    "method": "public/subscribe",
    "params": {"channels": ["deribit_price_index.btc_usd"]},
}


def app(_):
    async def btc_value():
        async with ws_connection_manager(
            URI, dumps=json.dumps, loads=json.loads
        ) as connection:
            await connection.request_reply(BTC_UPDATES_REQUEST)
            async for update in connection:
                yield f"{update['params']['data']['price']:,.2f}"

    return antd.Space(["BTC:", btc_value])
