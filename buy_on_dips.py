from config import username, password, secret, enctoken
from kiteext import KiteExt
import pandas as pd
import datetime

date = datetime.datetime.today()
date = date.strftime("%d%m%Y")

kite = KiteExt()

kite.login_with_credentials(userid=username, password=password, secret=secret)

with open('enctoken.txt', 'w') as wr:
    wr.write(kite.enctoken)

stocks = ['NSE:NAHARPOLY','NSE:LIKHITHA']

depth = kite.quote(stocks)

for stock in stocks:
    symbol = stock
    symbol = symbol.replace('NSE:', '')    
    pre_close = depth[stock]['ohlc']['close']
    last_price = depth[stock]['last_price']
    percent_change = ((float(last_price) - float(pre_close)) / float(pre_close)) * 100
    print(symbol, percent_change, date)

    if percent_change < -1:
        print(f'placing buy order {symbol} date {date}')
        try:
            response = kite.place_order(variety=kite.VARIETY_REGULAR, 
                            tradingsymbol= symbol,
                            exchange= "NSE",
                            transaction_type= "BUY",
                            quantity= 1,
                            product= "CNC",
                            order_type= "LIMIT",
                            price= last_price,
                            validity= "DAY")
            print(response)
        except Exception as e:
            print(e)
  
kws = kite.kws()