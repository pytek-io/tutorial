"""Child defined as an async generator from BTC quotes."""
from json import dumps, loads

from reflect_antd import Space
from reflect_utils.common import ws_connection_manager

URI = "wss://test.deribit.com/ws/api/v2"
BTC_UPDATES_REQUEST = {
    "jsonrpc": "2.0",
    "method": "public/subscribe",
    "params": {"channels": ["deribit_price_index.btc_usd"]},
}

def app():

    async def btc_value():
        async with ws_connection_manager(URI, dumps=dumps, loads=loads) as connection:
            await connection.request_reply(BTC_UPDATES_REQUEST)
            async for update in connection:
                yield f"{update['params']['data']['price']:,.2f}"

    return Space(["BTC:", btc_value])
