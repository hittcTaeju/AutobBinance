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
position = {
    'type' :None,
    'amount' : 0
}

op_mode =True
#if now.hour == 12 and now.minute == and (20 <= now.second < 30):  # 목표가 갱신
long_target, short_target = larry1.cal_target(binance, symbol)
balance = binance.fetch_balance()
usdt = balance['total']['USDT']
#time.sleep(10)

while True:
    now = datetime.datetime.now()

    if now.hour == 8 and now.minute == 50 and (0 <= now.second < 10):#포지션 종료. 청산
        if op_mode and position['type'] is not None:
            position=larry1.exit_position(binance,symbol,position)
            op_mode=False

    #current price, 구매 가능 수량
    btc =binance.fetch_ticker(symbol=symbol)
    cur_price = btc['last']
    amount =larry1.cal_amount(usdt,cur_price)

    if op_mode and position['type'] is None:#진입
        position=larry1.enter_position(binance,symbol,cur_price,long_target,short_target,amount,position)

    print(now,cur_price,'long target: ',long_target,'short target: ',short_target,position)
    time.sleep(1)



