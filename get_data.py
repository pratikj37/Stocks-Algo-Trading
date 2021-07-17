import zrd_login
import pdb
import talib

kite = zrd_login.kite

watchlist = ['ADANIGAS' , 'ASAINPAINT' , 'AXISBANK' , 'BAJAJFINANCE']


for name in watchlist:

    data = zrd_login.get_data(naem= name, segment = 'NSE:', delta= 5, interval= '5minute', continuous= False, oi = False)

    data['ema9'] = talib.EMA(data['close'], timeperiod=9, ematype=0)
    data['ema21'] = talib.EMA(data['close'], timeperiod=21, ematype=0)



    pdb.set_trace()

    