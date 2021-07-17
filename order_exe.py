import zrd_login
import pdb
import talib

kite = zrd_login.kite

watchlist = ['ADANIGAS' , 'ASAINPAINT' , 'AXISBANK' , 'BAJAJFINANCE']

traded_scripts = []

while True:
    for name in watchlist:

        print(name)
        data = zrd_login.get_data(name= name , segment = 'NSE:' , delta = 5, interval = '5minute', continuous = False, oi = False)

        data['ema9'] = talib.EMA(data['close'], timeperiod=9, matype=0)
        data['ema21'] = talib.EMA(data['close'], timeperiod=21, matype=0)

        last_candle = data.iloc[-2]

        if last_candle['close'] > 500:
            continue

        try:
                if(last_candle['ema9'] > last_candle['ema21']) and (name not in traded_scripts):
                    print(f"buy {name}")
                    kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_BUY , quantity = 1 , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_MARKET , price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
                    traded_scripts.append(name)
				    

                if(last_candle['ema9'] < last_candle['ema21']) and (name not in traded_scripts):
                    print(f"buy {name}")
                    kite.place_order(variety = kite.VARIETY_REGULAR , exchange = kite.EXCHANGE_NSE , tradingsymbol = name , transaction_type = kite.TRANSACTION_TYPE_SELL , quantity = 1 , product = kite.PRODUCT_MIS , order_type = kite.ORDER_TYPE_MARKET , price=None, validity=None, disclosed_quantity=None, trigger_price=None, squareoff=None, stoploss=None, trailing_stoploss=None, tag=None)
                    traded_scripts.append(name)
                
        except Exception as e:
            pass  
