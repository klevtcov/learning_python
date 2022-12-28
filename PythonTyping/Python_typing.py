''' Курс по типизации в Python '''

# Полезные материалы
# Бекпорты typing объектов для старых версий Python: https://pypi.org/project/typing-extensions/
# Тестирование аннотаций: https://mypy.readthedocs.io/en/stable/stubtest.html
# Генерация аннотаций: https://mypy.readthedocs.io/en/stable/stubgen.html
# Линтер для .pyi: https://pypi.org/project/flake8-pyi/
# Документация для stub пакетов: https://peps.python.org/pep-0561/

# Философия и устройство системы типов Python
# Типизация даёт нам понимание, можем ли мы совершить композицию двух функций.

# Какая бывает типизация:
# 1. С попытками приведения или без: 1 + 'a' - сильная/слабая
# 2. Когда проверяются наши действия? - статически/динамически
# 3. Пишем ли мы типы явно? - явная/ с выводом типов

# Динамическая типизация - проверка типов во время выполнения программы
# Статическая типизация - проверка до выполнения программы

''' Generic'''
# Описывает типы вложенных данных
# Задаёт тИповые аргументы

# def expects_list_of_str(items: list[str]) -> str:
#     return ','.join(items)

# expects_list_of_str(['a', 'b', 'c']) # ok
# expects_list_of_str([1, 2, 3]) # not ok

###

# from typing import Generic, TypeVar, reveal_type
# _ItemType = TypeVar('_ItemType')
# # TypeVar - позволяет создать переменную уровня типов.
# class Container(Generic[_ItemType]):
#     def __init__(self, item: _ItemType) -> None:
#         self.item = item

#     def get_item(self) -> _ItemType:
#         return self.item

# reveal_type(Container(1).get_item()) # int
# reveal_type(Container('a').get_item()) # str


''' Union / Optional '''
# Описывает "тип сумму" когда работает несколько разных типов

# from typing import Union, Optional
# assert int | str == Union[int, str] # или инт или строка
# assert int | None == Optional[int] # инт или нан

# def int_or_str(arg: int | str): # если принимает число - пишет число
#     if isinstance(arg, int):
#         print('int')
#     elif isinstance(arg, str):
#         print('str')
#     raise TypeError('nope')

# int_or_str(1) # ok
# int_or_str('a') # ok
# int_or_str(None) # not ok 


''' Any / Never '''

# Any - верхний тип, он равен всему. Любой объект может быть any.
# Never - нижний тип. НИкакой объект не может быть Never. Он равен ничему.

# import pickle # принимает что угодно и разворачивает его. может быть картинкой, данными, библиотекой и т.д.
# import sys
# from typing import Any, Never

# def unpickle(data: bytes) -> Any:
#     return pickle.loads(data)

# def exit_program(code: int) -> Never:
#     sys.exit(code)


''' Protocol '''

# Передаёт идею "утиной типизации" или "структурного наследования"
# Как 'interface' в TypeScript

# from typing import Protocol

# class Human:
#     def say(self) -> str:
#         return 'Hi!'
    
# class Duck:
#     def say(self) -> str:
#         return 'Quack'

# class CanSay(Protocol): # описываем протокол, что должен содержать класс
#     def say(self) -> str: ...

# def say_and_print(instance: CanSay) -> None: # описываем, что передаваемые данные должны удовлетворять условиям протокола
#     print(instance.say())

# say_and_print(Human()) # ok - Hi!
# say_and_print(Duck()) # ok - Quack
# say_and_print(1) # not ok - error

''' Алиасы stdlib, collections.abs, etc '''
# было -> стало
# typing.List[str] --> list[str]
# typing.Mapping[str, int] --> collections.abs.Mapping[str,int]


''' get_type_hints '''
# правильно получать аннотации из дефиниций
# from typing import get_type_hints

# class Point:
#     x: float
#     y: "float"

# print(Point.__annotations__)
# # {'x': <class 'float'>, 'y': 'float'}

# print(get_type_hints(Point))
# # {'x': <class 'float'>, 'y': <class 'float'>}


""" Утилиты """
# TYPE_CHECKING - всегда в тру
# get_overloads, clear_overloads

'''  Заслуживают упоминания '''
# ClassVar - если хотите указать, что переменная является классом
# Literal и Final - финал - классы, которые нельзя наследовать
# Callable и @overload

# from __future__ import annotations

''' Новинки '''
# assert_never
# assert_type - ничего не делает в рантайме, н опозволяет писать тесты на типизацию. используется в тайпчекерах
# dataclass_transform - можно задекарировать функцию или датакласс, чтоб он вёл себя как датакласс
# NotRequired / Required - обязательные/ не обязательные типы
# LiteralString - позволяет избавиться от sql инъекций

##########

# from typing import Union
# isinstance(1, Union[int, str]) # True. проверка на соответствие