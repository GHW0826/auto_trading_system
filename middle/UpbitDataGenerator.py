import libs.UnderlyingDataGenerator as udg
from typing import List
import upbit.upbitapi as up



class UpbitDataGenerator(udg.UnderlyingDataGenerator):

    def __init__(self, access_key, secret_key):
        self.upbit_api = up.UpbitApi(access_key, secret_key)

    def get_underlying_name(self) -> List[str]:
        super().get_underlying_name()
        print("UpbitDataGenerator.get_underlying_name")
        names = self.upbit_api.get_stock_code()
        return names

    def get_current_price(self) -> List[str]:
        print("UpbitDataGenerator.get_underlying_name")
        self.upbit_api.get_current_price()
        pass
    
    def print(self):
        pass