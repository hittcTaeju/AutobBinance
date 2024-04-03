import pprint

import ccxt
with open("./binance.key") as f:
    lines = f.readlines()
    api_key =lines[0].strip()
    api_secret=lines[1].strip()

binance =ccxt.binance(config={
    'apiKey':api_key,
    'secret':api_secret,
    'enableRateLimit':True,
    'options':{
        'defaultType':'future'
    }
})

btc = binance.fetch_ticker("BTC/USDT")
pprint.pprint(btc['last'])