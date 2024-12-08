from abc import *


class UpbitAbstract(metaclass=ABCMeta):
    access_key = 'access_key'
    secret_key = 'secret_key'


    # 현재가 조회
    @abstractmethod
    def get_current_price(self, ticker):
        pass

    # 티커 조회
    @abstractmethod
    def get_tickers(self):
        pass

