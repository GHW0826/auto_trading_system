import sys
from configparser import ConfigParser
from upbit.upbitpackage import UpbitPackage
from upbit.upbitapi import UpbitApi
from ui.app import MyApp
from PyQt5.QtWidgets import *
import middle.UpbitDataGenerator as upbitdg
import libs.BasicStrategy as bs

config = ConfigParser()
config.read('config.ini')

access_key = config['secret']['access_key']
secret_key = config['secret']['secret_key']

print(access_key)
print(secret_key)
print("Hello World")

### 거래할 코인 symbol
# coin = "KRW-XRP" 

# a = UpbitApi(access_key, secret_key)
# a.get_stock_code()
# print("====================")
# a.get_candle()
# print("====================")
# a.get_trade_history()
# print("====================")
# a.get_current_price()
# print("====================")

upbitdatagenerator = upbitdg.UpbitDataGenerator(access_key, secret_key)
strategy = bs.BasicStrategy(upbitdatagenerator)
strategy.get_underlying_info()

app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())