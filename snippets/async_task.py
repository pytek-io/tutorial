"""Simple background async task updating display with realtime BTC quotes."""
import json

import render as r
import render_antd as antd
from demos.connection import ws_connection_manager

URI = "wss://test.deribit.com/ws/api/v2"
BTC_UPDATES_REQUEST = {
    "jsonrpc": "2.0",
    "method": "public/subscribe",
    "params": {"channels": ["deribit_price_index.btc_usd"]},
}


def app(window: r.Window):
    btc_value = r.ObservableValue("connecting...", key="btc_update")

    async def update_btc_value():
        async with ws_connection_manager(
            URI, dumps=json.dumps, loads=json.loads
        ) as connection:
            await connection.request_reply(BTC_UPDATES_REQUEST)
            async for update in connection:
                btc_value.set(f"{update['params']['data']['price']:,.2f}")

    window.start_soon(update_btc_value)
    return antd.Space(["BTC:", btc_value])
