from .upbitabstract import UpbitAbstract;
import pyupbit

class UpbitPackage(UpbitAbstract):

    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
        pyupbit.Upbit(self.access_key, self.secret_key)

    # 현재가 조회
    def get_current_price(self, ticker):
        super().get_tickers()
        print(ticker)
        """
        price = pyupbit.get_current_price("KRW-BTC")
        print(price)
        """

    # 티커 조회
    def get_tickers(self):
           super().get_tickers()
           tickers = pyupbit.get_tickers()
           print(tickers)
           print(type(tickers))
           """
           tickers = pyupbit.get_tickers()
           print(tickers)
           print(type(tickers))
           """

