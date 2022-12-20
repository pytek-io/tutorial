"""Simple background async task updating display with realtime BTC quotes."""
import json

import reflect_antd as antd
import reflect_utils

import reflect as r

URI = "wss://test.deribit.com/ws/api/v2"
BTC_UPDATES_REQUEST = {
    "jsonrpc": "2.0",
    "method": "public/subscribe",
    "params": {"channels": ["deribit_price_index.btc_usd"]},
}


def app():
    btc_value = r.create_observable("connecting...", key="btc_update")

    async def update_btc_value():
        async with reflect_utils.ws_connection_manager(
            URI, dumps=json.dumps, loads=json.loads
        ) as connection:
            await connection.request_reply(BTC_UPDATES_REQUEST)
            async for update in connection:
                btc_value.set(f"{update['params']['data']['price']:,.2f}")

    r.get_window().start_soon(update_btc_value)
    return antd.Space(["BTC:", btc_value])
