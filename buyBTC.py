import pprint

import ccxt
with open("./binance.key") as f:
    lines = f.readlines()
    api_key =lines[0].strip()
    api_secret=lines[1].strip()

exchange =ccxt.binance(config={
    'apiKey':api_key,
    'secret':api_secret,
    'enableRateLimit':True,
    'options':{
        'defaultType':'future'
    }
})
symbol = "BTCUSDT"
positions = exchange.fetch_positions(symbols=[symbol])
now_price=positions[0]['info']['positionAmt']

# order = exchange.create_market_sell_order(
#     symbol="BTC/USDT",
#     amount=now_price
# )
# pprint.pprint(order)