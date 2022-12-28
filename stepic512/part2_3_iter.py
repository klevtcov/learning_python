''' 2.3 Итераторы и генераторы '''

# lst = [1, 2, 3, 4, 5]
# book = {
#     'title' : 'The Lamponiers',
#     'author' : 'Stephen King',
#     'year_published' : 1990
# }
# string = 'Hello, world!' 

# for i in string:
#     print(i)

# iterator = iter(book)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# it = iter(book)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break

''' Свой итератор  '''

# from random import random

# class RandomIterator:
#     def __iter__(self):
#         return self

#     def __init__(self, k):
#         self.k = k
#         self.i = 0
    
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration

# x = RandomIterator(3)
# # print(next(x)) # next(x) -- x.__next__() x -- iterator
# # print(next(x))
# # print(next(x))
# # print(next(x))

# for x in RandomIterator(10):
#     print(x)


# class DoubleElementListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0

#     def __next__(self):
#         if self.i < len(self.lst):
#             self.i += 2
#             return self.lst[self.i - 2] , self.lst[self.i - 1]
#         else:
#             raise StopIteration


# class MyList(list):
#     def __iter__(self):
#         return DoubleElementListIterator(self)

# for pair in MyList([1, 2, 3, 4]):
#     print(pair)


''' Генераторы  '''

# from random import random

# class RandomIterator:
#     def __iter__(self):
#         return self

#     def __init__(self, k):
#         self.k = k
#         self.i = 0
    
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration

# def random_generator(k):
#     for i in range(k):
#         yield random()

# gen = random_generator(5)
# print(type(gen))


# class MyNoFilter2:
#     def __init__(self, lst):
#         self.lst = lst

#     def __iter__(self):
#         for x in self.lst:
#             yield x

#  делает то же самое, что и следующий код:
# class MyNoFilter1:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         while True:
#             if self.i < len(self.lst):
#                 self.i += 1
#                 return self.lst[self.i - 1]
#             else:
#                 raise StopIteration


# def simple_gen():
#     print('Checkpoint 1')
#     yield 1
#     print('Checkpoint 2')
#     return 'No more elements'
#     yield 2
#     print('Checkpoint 3')

# gen = simple_gen()

# x = next(gen)
# print(x)
# y = next(gen)
# print(y)
# z = next(gen)

# from random import random

# def random_generator(k):
#     for i in range(k):
#         yield random()

# gen = random_generator(3)

# for i in gen:
#     print(i)

'''Моё решение'''

# class multifilter:
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         return pos >= neg

#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         return pos >= 1

#     def judge_all(pos, neg):
#         # допускает элемент, если его допускают все функции (neg == 0)
#         return neg == 0

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#         self.pos = 0 
#         self.neg = 0

#         # iterable - исходная последовательность
#         # funcs - допускающие функции
#         # judge - решающая функция


#     def __iter__(self):
#         # возвращает итератор по результирующей последовательности
#         for i in self.iterable:
#             pos, neg = 0, 0
#             for func in self.funcs:
#                 if func(i):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(pos, neg):
#                 yield i
        

# 2) __iter__ у нас генератор! пробегаемся по нашему списку self.iterable, внутри цикла for первым делом создаем переменные pos,neg=0,0

#  2.1) *funcs - представляет собой кортеж функций, по которому не трудно пробежаться и выполнить каждую функцию над каждым элементом списка. 
# От результата каждой функции(true,false) зависит какую из переменных pos и neg мы увеличиваем.

#  2.2)После того как мы пробежались по функциям *funcs - проверяем значение функции и если оно правдиво, то "Елдим))"(yield) значение из списка.


# def mul2(x):
#     return x % 2 == 0

# def mul3(x):
#     return x % 3 == 0

# def mul5(x):
#     return x % 5 == 0

# a = [i for i in range(31)] # [0, 1, 2, ... , 30]

# multi = multifilter(a, mul2, mul3)
# # print(multi)


# print(list(multifilter(a, mul2, mul3, mul5))) 
# # # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# # # [0, 6, 10, 12, 15, 18, 20, 24, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# # # [0, 30]

'''Решение из комментов'''
# class multifilter:
    
#     judge_half = lambda fx: sum(fx) >= len(fx)/2
#     judge_any = lambda fx: any(fx)
#     judge_all = lambda fx: all(fx)

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
        
#     def __iter__(self):
#         return ( x for x in self.iterable if self.judge( [f(x) for f in self.funcs ] ) )


''' Задача 2'''
# Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится только на единицу и на само себя.
# Например, число 2 является простым, так как делится только на 1 и 2. Также простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел.
# Число 4, например, не является простым, так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как оно имеет ровно один делитель – 1.

# Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.

''' Моё решение'''

# import itertools

# def primes():
#     a = 1
#     while True: 
#         a += 1
#         count = 0
#         for el in range(2, a+1):
#             if a % el == 0:
#                 count +=1
#         if count == 1:
#             yield a


# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


''' Из коментов '''
# def primes():
    
#     k = 2
#     while True:
#         if all(k % i for i in range(2, int(k ** 0.5) + 1)):
#             yield k
#         k += 1


''' Четные исключаем, они по определению не простые '''
# def primes():
#     yield 2
#     k = 3
#     while True:
#         if all(k % i for i in range(2, int(k ** 0.5) + 1)): # перебираем до корня из числа +1
#             yield k
#         k += 2 # идём по нечётным

'''' решение преподавателя '''
# Пример правильного решения.

# Реализуем функцию генератор, которая бесконечно перебирает все числа, и если число простое, 
# возвращает его, используя конструкцию yield.

# В данном решении используется наблюдение: если у числа x , есть какой-либо делитель отличный от 1 и x, 
# то этот делитель обязательно не больше чем sqrt{x} 
# Поэтому проверяем все числа от 2 до sqrt{x}, если хотя бы одно из них является делителем нашего числа -- то наше число не простое.

# def primes():
#     i = 2
#     while True:
#         is_prime = True
#         divisor = 2
#         while divisor ** 2 <= i:
#             if i % divisor == 0:
#                 is_prime = False # non-trivial divisor
#                 break

#             divisor += 1

#         if is_prime:
#             yield i

#         i += 1


'''  list comprehension  '''

# x = [-2, -1, 0, 1, 2]
# # y = [i*i for i in x]
# y = [i*i for i in x if i > 0]

# Что взять, откуда взять, при каких условия

# for i in x:
#     y.append(i*i)

# print(y)


# z = [(x, y) for x in range(3) for y in range(3) if y >= x]
# # аналогично
# for x in range(3):
#     for y in range(3):
#         if y >= x:
#             z.append((x,y))
# print(z)

# с круглыми скобками получится генератор
# z = ((x, y) for x in range(3) for y in range(3) if y >= x)
# print(z)

# for i in z:
#     print(i)

# Кроме списков и генераторов, такой же синтаксис в Python 3 возможен для сетов и словарей!

# {ord(x) for x in 'spaam'}    # генерируем set {112, 115, 109, 97}

# {x:ord(x) for x in 'spaam'}  # генерируем dictionary {'s': 115, 'm': 109, 'p': 112, 'a': 97}

# Если список содержит последовательно пары key value, то так можно преобразовать в словарь:

# d = ['Dota', 'sucks', 'Python', 'rules', 'Saperavi', 'depends']
# dictus = {d[x]: d[x+1] for x in range(0, len(d), 2)}

a = [i for i in range(5)][1:]
print(a)
b = [i + 1 for i in range(4)]
print(b)
c = [i for i in range(4)]
print(c)
d = list(i + 1 for i in range(4))
print(d)

