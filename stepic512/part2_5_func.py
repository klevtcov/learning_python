''' Работа с функциями: functool и лямбда функции '''

# n, k = map(int, input().split()) # принимает да числа с ввода и суммирует
# print(n + k)

# x = input().split()
# # 100 50
# print(x)
# # ['100', '50']
# # множественное присваивание
# n, k = map(int, x) # map применяет функцию к каждому элементу второго аргумента
# n, k = (int(i) for i in x) # аналог
# print(n + k)
# # 150


# функция принимает список и оставляет только четные:

# x = input().split()
# # 10 11 12 13 14 15
# xs = (int(i) for i in x)
# def even(x):
#     return x % 2 == 0


# evens = filter(even, xs)
# for i in evens:
#     print(i)
# # 10 12 14

# evens = list(filter(even, xs))
# print(evens)
# # [10, 12, 14]


''' lambda функции '''

# x = input().split()
# # 10 11 12 13 14 15
# xs = (int(i) for i in x)

# # def even(x):
# #     return x % 2 == 0
# even = lambda x: x % 2 == 0
# # lambda "аргумент - что принимаем" : 'возвращаемое значение'
# evens = list(filter(even, xs))
# evens = list(filter(lambda x: x % 2 == 0, xs))
# print(evens)

''' использование при сортировки '''

# x = [
#     ('Guido', 'van', 'Rossum'),
#     ('Haskell', 'Curry'),
#     ('John', 'Backus')
# ]
# # берём словарь имён

# def length(name):
#     return len(' '.join(name))
# # функция возвращающая длинну имени

# name_length = [length(name) for name in x]
# # проверяем работоспособность функции на наших данных
# print(name_length)

# x.sort(key=length)
# # передаём функцию подсчёта символов  в качестве ключа в метод sort
# # наш массив отсортирован по длинне имени
# print(x)

# # с использованием lambda:
# x.sort(key=lambda name: len(' '.join(name)))


''' примеры '''

# x = ['abc', 'a', 'ab', 'abcd']
# Сортировка элементов списка по возрастанию:

# # 1
# x.sort(key=len)
# print(x)
# ['a', 'ab', 'abc', 'abcd']

# # 2
# new_x = sorted(x, key=len)
# print(new_x)
# ['a', 'ab', 'abc', 'abcd']
# В обратном порядке:

# # 1
# x.sort(key=len, reverse=True)
# print(x)
# ['abcd', 'abc', 'ab', 'a']

# # 2
# new_x = sorted(x, key=len, reverse=True)
# print(new_x)
# ['abcd', 'abc', 'ab', 'a']
# Разница между sort() и sorted() в том, что первый - сортирует список на месте, возвращая None. Второй - возвращает новый отсортированный список.

# Так же, можно сортировать словари.

# x = {1: 'a', 3: 'ab', 2: 'abc'}
#  По ключам:

# x = dict(sorted(x.items()))
# print(x)
# {1: 'a', 2: 'abc', 3: 'ab'}
# По значениям:

# x = dict(sorted(x.items(), key=lambda e:e[1]))
# print(x)
# {1: 'a', 3: 'ab', 2: 'abc'}


''' библиотека operator '''

# import operator as op

# print(op.add(4, 5)) # 9
# print(op.mul(4, 5)) # 20
# print(op.contains([1, 2, 3], 4)) # False

# x = [1, 2, 3]
# f = op.itemgetter(1) # f(x) == x[1]
# print(f(x)) # 2

# x = {'abc': 5, 'bcd': 7}
# f = op.itemgetter('abc') # f(x) == x[abc]
# print(f(x)) # 5

# f = op.attrgetter('sort') # f(x) == x.sort


# x = [
#     ('Guido', 'van', 'Rossum'),
#     ('Haskell', 'Curry'),
#     ('John', 'Backus')
# ]

# # Сортируем список по последнему элементу списка
# x.sort(key=op.itemgetter[-1])
# print(x)

# print(dir(op)) # вывод всех методов библиотеки

''' библиотека functools '''

# from functools import partial

# # передаём значение и основание, в данном случае - двоичная система
# x = int('1101', base=2)
# print(x) # 13

# Можно захардкодить аргументы в функцию и не указывать их больше
# int_2 = partial(int, base=2)
# x = int_2('1101')
# print(x) # 13


''' Сортируем даннеы по последнему элементу в строке/кортеже и т.д.'''
# import operator as op
# from functools import partial

# x = [
#     ('Guido', 'van', 'Rossum'),
#     ('Haskell', 'Curry'),
#     ('John', 'Backus')
# ]

# sort_by_last = partial(list.sort, key=op.itemgetter(-1))
# print(x)
# sort_by_last(x)
# print(x)

# y = ['abc', 'cba', 'abb']
# sort_by_last(y)
# print(y) # ['cba', 'abb', 'abc']

# ''' Пример map reduce '''

# from functools import reduce
 
# x = [1, 2, 3, 4, 5, 6, 7]
# print(list(map(lambda x: x + x, x))) # каждый элемент складывается сам на себя
# print(reduce(lambda x, y: x + y, x)) # первый и второй элемент складываются, на следующей итерации первым элементом становятся сложенные элементы, а вторым становится 3 элемент
# reduce(lambda x,y: x+y, range(1,10)) # сумма элементов от 1 до 9. Как будто вы суммируете нее 2 элемента а все 9.

# Вывод:
# [2, 4, 6, 8, 10, 12, 14]
# 28 


''' Задание '''

# Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте».
# Но иногда, когда нужно создавать много однотипных лямбда функций, еще удобнее будет создать функцию, которая будет их генерировать.

# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.

# ﻿Пример использования:

# mod_3 = mod_checker(3)

# print(mod_3(3)) # True
# print(mod_3(4)) # False

# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4)) # True


def mod_checker(x, mod=0):
    return lambda y : y % x == mod

# вариант решения от преподавателя
mod_checker = lambda x, mod=0: lambda y: y % x == mod