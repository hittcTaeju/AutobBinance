# Position
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

# # buy
# symbol = "BTCUSDT"
# positions = exchange.fetch_positions(symbols=[symbol])
# pprint.pprint(positions[0]['info']['positionAmt'])
