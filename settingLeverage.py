import ccxt
import pprint

# API 정보 파일 열기
f = open("./binance.key")
lines = f.readlines()
api_key = lines[0].strip()
secret = lines[1].strip()
f.close()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future'
    }
})
symbol = "BTC/USDT"
balance = binance.fetch_balance()
usdt_balance = balance['USDT']

btc = binance.fetch_ticker("BTC/USDT")
leverage=5
# print(btc['last'])
# print(usdt_balance['free'])
# print(usdt_balance['free']/btc['last']*leverage)
# order = binance.create_market_buy_order(
#     symbol=symbol,
#     amount=usdt_balance['free']/btc['last']*leverage*0.5
# )