from abc import *
from typing import List

class UnderlyingDataGenerator(metaclass=ABCMeta):

    @abstractmethod
    def get_underlying_name(self) -> List[str]:
        print("UnderlyingDataGenerator.get_underlying_name")
        pass

    @abstractmethod
    def get_current_price(self) -> List[str]:
        print("UnderlyingDataGenerator.get_underlying_name")
        pass

    def print(self) -> None:
        pass