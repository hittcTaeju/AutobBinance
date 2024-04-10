import datetime
import time
import pandas as pd
import ccxt
import pprint
import larry1

# API 정보 파일 열기
with open("./secondKey.key") as f:
    lines = f.readlines()
    api_key = lines[0].strip()
    secret = lines[1].strip()

binance = ccxt.binance(config={
    'apiKey': api_key,
    'secret': secret
})
symbol = "BTC/USDT"
btc =binance.fetch_ticker(symbol=symbol)
cur_price = btc['last']
print(cur_price)