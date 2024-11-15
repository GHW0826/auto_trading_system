from configparser import ConfigParser
import pyupbit


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
upbit = pyupbit.Upbit(access_key, secret_key)

tickers = pyupbit.get_tickers()
print(tickers)
print(type(tickers))