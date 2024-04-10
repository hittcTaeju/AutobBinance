import ccxt
import pandas as pd
import math


def cal_target(binance,symbol):
    # 목표가격 계산
    btc_ohlcv = binance.fetch_ohlcv(
        symbol=symbol,
        timeframe='1d',
        since=None,
        limit=10
    )
    df = pd.DataFrame(
        data=btc_ohlcv,
        columns=['datetime', 'open', 'high', 'low', 'close', 'volume']
    )
    df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
    df.set_index('datetime', inplace=True)
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    long_target = today['open'] + (yesterday['high'] - yesterday['low']) * 0.5
    short_target = today['open'] - (yesterday['high'] - yesterday['low']) * 0.5
    return (long_target,short_target)
def cal_amount(usdt_balance,cur_price,leverage):
    portion = 0.5
    usdt_trade = usdt_balance*portion*leverage
    amount = math.floor((usdt_trade*1000000)/cur_price)/1000000
    return amount
def enter_position(binance,symbol,cur_price,long_target,short_target,amount,position):
    if cur_price>long_target:#롱 진입
        position['type'] = 'long'
        position['amount'] = amount
        print("ENTER LONG")
        #print(symbol)
        binance.create_market_buy_order(symbol=symbol,amount=amount)

    elif cur_price<short_target: #숏진입
        position['type'] = 'short'
        position['amount'] = amount
        print("ENTER SHORT")
        binance.create_market_sell_order(symbol=symbol,amount=amount)

    return position
def exit_position(binance,symbol,position):
    amount = position['amount']
    if position['type'] =='long':
        binance.create_market_sell_order(symbol=symbol,amount=amount)
        position['type']=None
    elif position['type']=='short':
        binance.create_market_buy_order(symbol=symbol, amount=amount)
        position['type']=None
    position['amount']=0
    return position
#print(cal_target(symbol))