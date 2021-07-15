import zrd_login
import pdb
import talib

kite = zrd_login.kite

watchlist = ['ADANIGAS' , 'ASAINPAINT' , 'AXISBANK' , 'BAJAJFINANCE']

for name in watchlist:

    print(name)
    data = zrd_login.get_data(name = name, segment = 'NSE:', delta = 5, interval = '5minute', continuous = False, oi = False)

    data['ema9'] = talib.EMA(data['close'], timeperiod=15, ematype=0)
    data['ema21'] = talib.EMA(data['close'], timeperiod=15, ematype=0)

    last_candle = data.iloc[-2]

    if (last_candle['ema9'] > last_candle['ema21']):
        print(f"buy {name}")
        pdb.set_trace()
        kite.place_order(variety= kite.VARIETY_REGULAR, exchange = kite.EXCHANGE_NSE, tradingsymbol= name[4:], transaction_type= kite.TRANSACTION_TYPE_SELL, quantity = 1, 
        product= kite.PRODUCT_MIS, order_type= kite.ORDER_TYPE_MARKET, price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)


    if (last_candle['ema21'] > last_candle['ema9']):
        print(f"sell {name}")
        pdb.set_trace
        
