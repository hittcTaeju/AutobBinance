import datetime
import time
import pandas as pd
import ccxt
import pprint
import larry1

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
long_target, short_target = larry1.cal_target(binance, symbol)