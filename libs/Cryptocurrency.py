from dataclasses import dataclass

'''
"market": "USDT-OXT",
"korean_name": "오키드",
"english_name": "Orchid"
'''

# 코인 
@dataclass
class Cryptocurrency():

    market_name: str
    korean_name: str
    english_name: str

    def set_cur_price(self):
        pass

    def print(self):
        pass