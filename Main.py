import sys
from configparser import ConfigParser
from upbit.upbitpackage import UpbitPackage
from upbit.upbitapi import UpbitApi
from ui.app import MyApp
from PyQt5.QtWidgets import *

config = ConfigParser()
config.read('config.ini')

access_key = config['secret']['access_key']
secret_key = config['secret']['secret_key']

print(access_key)
print(secret_key)
print("Hello World")

### 거래할 코인 symbol
coin = "KRW-XRP" 


### 업비트 연동
"""
upbit = pyupbit.Upbit(access_key, secret_key)
tickers = pyupbit.get_tickers()
print(tickers)
print(type(tickers))
"""

a = UpbitApi(access_key, secret_key)
a.get_stock_code()
print("====================")
a.get_candle()
print("====================")
a.get_trade_history()
print("====================")
a.get_current_price()
print("====================")


app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())