from datetime import datetime as dt
# from logging import _level

class Player:
    
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__level', '__health', '__born']

    def __init__(self) -> None:
        self.__level = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    @property
    def level(self):
        return self.__level, f'{dt.now() - self.__born}'

    @level.setter
    def level(self, numeric):
        self.__level += Player.__typeTest(numeric)
        if self.__level >= 100: self.__level = 100

    # def get_level(self):
    #     return self.__level

    # def set_level(self, numeric):
    #     self.__level += numeric

    @classmethod
    def set_cls_field(cls, level=1, health=100):
        cls.__LVL = Player.__typeTest(level)
        cls.__HEALTH = Player.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError ('Must be int')




# x = Player()
# print(x.level)
# x.level = 5
# print(x.level)
# print(x.get_level())
# print(x.set_level(2))
# print(x.get_level())




# @property
# @method.setter
# @classmethod
# @staticmethod