import libs.UnderlyingDataGenerator as udg


# 기본 전략
class BasicStrategy():

    def __init__(self, data_generator: udg.UnderlyingDataGenerator):
        self.data_generator = data_generator

    # 전체 시세 받아오기
    def get_underlying_info(self):
        # 전체 자산 이름 불러오기
        self.names = self.data_generator.get_underlying_name()
        # print(self.names)
        self.data_generator.get_current_price()
        pass

    # 저장
    def set_underlying_info(self):
        pass

    # 출력
    def print(self):
        pass


    def exec(self):

        self.get_underlying_info()

        self.set_underlying_info()

        self.print()