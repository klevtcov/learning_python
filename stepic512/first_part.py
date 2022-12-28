# 1. Базовые принципы языка:

# fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
# fib(31)

# Реализуйте программу, которая принимает последовательность чисел и 
# выводит их сумму.

# Вашей программе на вход подается последовательность строк.
# Первая строка содержит число n (1 ≤ n ≤ 100).
# В следующих n строках содержится по одному целому числу.

# Выведите одно число – сумму данных n чисел.

# Моё решение:

# summa = 0
# for _ in range(int(input())):
#     summa += int(input())
# print(summa)

# print(sum([int(input()) for i in range(int(input()))]))

# Идентификатор объекта:

# x = [1, 2, 3]
# print(id(x))
# print(id([1, 2, 3]))
# print(id(x[0]))
# print(id(x[1]))
# print(id(x[2]))

# Ссылаются ли две переменные на один объект:

# x = [1, 2, 3]
# y = x
# y is x # True
# y is [1, 2, 3] #False

# x = [1, 2, 3]
# y = x
# print(y is x) #True
# x.append(4)
# print(x) # [1, 2, 3, 4]
# print(y) # [1, 2, 3, 4]

# Типы объектов:
# Тип объектов не может быть изменён после создания объекта
# (как и и дентификатор)
# Узнать тип можно командой type()
# x = [1, 2, 3]
# type(x) # output is <class 'list'>
# type(4) # output is <class 'int'>
# type(type(x) # output is <class 'type'>

# Immutable:
# Числа
# Boolean
# tuple - кортеж
# str - стока
# множества замороженные - frozenset

# Mutable: 
# Список - list[]
# Словари - dict{}
# Множества - set()

# Реализуйте программу, которая будет вычислять количество различных 
# объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.

# Вашей программе доступна переменная с названием objects, которая 
# ссылается на список, содержащий не более 100 объектов. Выведите 
# количество различных объектов в этом списке.

# ans = 0
# for obj in objects: # доступная переменная objects
#     ans += 1
# print(ans)

# Примечание:
# Количеством различных объектов называется максимальный размер 
# множества объектов, в котором любые два объекта являются различными.

# Рассмотрим пример:
# objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа 
# # соответствуют одинаковым объектам, а различные – различным

# Тогда все различные объекты являют собой множество {1, 2, 3}. 
# Таким образом, количество различных объектов равно трём.

# objects = [1, 2, 3, 1, 4, 5, 2]
# print(len(set(objects)))
# lst = []
# count = 0
# for x in objects:
#     if x not in lst:
#         lst.append(x)
#         count += 1
# print(count)

# print(len(set(map(id, objects))))
# print(len(set(id(i) for i in objects)))

# Функции и стек вызовов:
# Синтаксис:

# def function_name(argument1, argument2):
#     # function body
#     return argument1 + argument2
# x = function_name(2, 8)
# y = function_name(x, 21)
# print(y)
# print(type(function_name))
# print(id(function_name))

# def list_sum(lst):
#     result = 0
#     for element in lst:
#         result += element
#     return result

# def sum(a, b):
#     return a + b

# y = sum(14, 29)
# z = list_sum([1, 2, 3])
# print(y)
# print(z)

# x = [1, 2, 3]

# x.append(4)
# x.append(5)

# print(x) # [1, 2, 3, 4, 5]

# top = x.pop()
# print(top) # 5
# print(x) # [1, 2, 3, 4]

# top = x.pop()
# print(top) # 4
# print(x) # [1, 2, 3]

# x = print(4) # x = None
# x is None #True

# Напишите реализацию функции closest_mod_5, принимающую в 
# качестве единственного аргумента целое число x и 
# возвращающую самое маленькое целое число y, такое что:

# y больше или равно x
# y делится нацело на 5

# Моё решение:
# def closest_mod_5(x):
#     while x % 5:
#         x += 1
#     return x

# рекурсия:
# def closest_mod_5(x):
#     return x if x % 5 == 0 else closest_mod_5(x + 1)

# решение от математиков:
# def closest_mod_5(x):
#     return (x + 4) // 5 * 5

# Функции: примеры вызова функций:

# def printab(a, b):
#     print(a)
#     print(b)
# # Correct way to call a function
# printab(10, 20)
# printab(a=10, b=20)
# # keyword arguments always after non-keyword arguments
# printab(10, b=20)

# lst = [10, 20]
# printab(*lst) # printab(lst[0], lst[1])

# args = {'a':  10, 'b': 20}
# printab(**args) # = printab(key1=args[key1],
#                 #           key2=args[key2])

# Correct
# def printab(a, b): # function with
#     print(a)       # two positional arguments
#     print(b)

# def printab(a, b=10): # one of arguments has
#     print(a)          # a default value
#     print(b)

# def printab(a=10, b=10):  # both argumets has
#     print(a)              # a default value
#     print(b)
# # Incortrect
# def printab(a=10, b): # non-default argument
#     print(a)          # follows default argument
#     print(b)

# Не ограниченное количество аргументов:

# def printab(a, b, *args):
#     print('positional argumen a ', a)
#     print('positional argumen b ', b)
#     print('additional argumens:',)
#     for arg in args:
#         print(arg)
# printab(10, 20, 30, 40, 50)
# # positional argumen a 10
# # positional argumen b 20
# # additional argumens:
# 30
# 40
# 50

# def s(a, *vs, b=10):
#    res = a + b
#    print('a + b is ', res)
#    for v in vs:
#        res += v
#        print('промежуточный ', res)
#    return res

# print(s(11, 10, 10))

# Рекурсивные функции

# def fib(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
# y = fib(6)
# print(y) #8

# Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
# Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
# Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).

# Пример:
# Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
# Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
# Различных сочетаний три, поэтому C(3, 2) = 3.

# Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом, а именно, ничего 
# не выбрать.
# Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать 
# пять.

# Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1).

# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

# Вашей программе на вход подается строка, содержащая два целых числа n и k (1 ≤ n ≤ 10, 0 ≤ k ≤ 10).
# Ваша программа должна вывести единственное число: C(n, k).

# Примечание:
# Считать два числа n и k вы можете, например, следующим образом:

# n, k = map(int, input().split())

# Моё решение:
# a, b = map(int, input().split())
# def uni(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     return uni(n - 1, k) + uni(n - 1, k - 1)
# print(uni(a, b))

# Пространство имён и области видимости

# builtin # встроенные имена
    # int, str, id, max, bool

# main # глобальные переменные
    # a = 1, def fun()

# local # локальные, объявленные внутри функций

# Local -> Enclosing -> Global -> Builtin # Области видимости


# Циклы и условный оператор:
# x = 0
# for i in range(5)
#     x = i * i
# print(x) # 16
# print(i) # 4

# ok_status = True
# vowels = ['a', 'u', 'i', 'e', 'o']

# def check(word):
#     global ok_status
#     for vowel in vowels:
#         if vowel in word:
#             return True
    
#     ok_status = False
#     return False

# print(check('ababaac')) # True
# print(ok_status) # True
# print(check('www')) #False
# print(ok_status) # False

# def f():
#     ok_status = True
#     vowels = ['a', 'u', 'i', 'e', 'o']

#     def check(word):
#         nonlocal ok_status
#         for vowel in vowels:
#             if vowel in word:
#                 return True
        
#         ok_status = False
#         return False

#     print(check('ababaac')) # True
#     print(ok_status) # True
#     print(check('www')) #False
#     print(ok_status) # False

# f()
# print(ok_status) # NameError

# Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку 
# создания пространств имен и добавление в них переменных.

# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

# Вашей программе на вход подаются следующие запросы:

# create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
# add <namespace> <var> – добавить в пространство <namespace> переменную <var>
# get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе 
# из пространства <namespace>, или None, если такого пространства не существует
# Рассмотрим набор запросов

# add global a
# create foo global
# add foo b
# create bar foo
# add bar a
# Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен, 
# созданной при выполнении данного кода

# a = 0
# def foo():
#   b = 1
#   def bar():
#     a = 2

# В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global. Далее мы 
# объявляем функцию foo, что влечет за собой создание локального для нее пространства имен внутри пространства 
# global. В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции foo 
# функцию bar, тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.
# Добавим запросы get к нашим запросам

# get foo a
# get foo c
# get bar a
# get bar b
# Представим как это могло бы выглядеть в коде

# a = 0
# def foo():
#   b = 1
#   get(a)
#   get(c)
#   def bar():
#     a = 2
#     get(a)
#     get(b)

# Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
# Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a, 
# но в пространстве global, внутри которого находится пространство foo, она объявлена. Аналогично, результатом 
# запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.

# Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве 
# global не была объявлена переменная с.

# Более формально, результатом работы get <namespace> <var> является

# <namespace>, если в пространстве <namespace> была объявлена переменная <var>
# get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, 
# если переменная не была объявлена
# None, если не существует <parent>, т. е. <namespace> – это global

# Формат входных данных
# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из 
# строчных латинских букв.

# Формат выходных данных
# Для каждого запроса get выведите в отдельной строке его результат.
# Sample Input:
# 9
# add global a
# create foo global
# add foo b
# get foo a
# get foo c
# create bar foo
# add bar a
# get bar a
# get bar b

# Sample Output:
# global
# None
# bar
# foo

# Моё решение:
# def get_from_dict(space, var):
    
#     if var in namespace.get(space):
#         print(space)
#         return space
#     elif space == 'global':
#         print('None')
#         return None
#     else:
#         get_from_dict(parents[space], var)       

# namespace = {'global': []}
# parents = {'global':'None'}

# for i in range(int(input())):
#     cmd, namesp, arg = input().split()
    
#     if cmd == 'add':
#         if namesp in namespace:
#             namespace[namesp].append(arg)
#             # print(namespace)
#         else:
#             namespace.update({namesp: [arg]})
#             # print(namespace)

#     if cmd == 'create':
#         if namesp in parents:
#             parents[namesp].append(arg)
#             # print(parents)
#         else:
#             parents.update({namesp: arg})
#             namespace.update({namesp: []})
#             # print(parents)

#     if cmd == 'get':
#         if namesp in namespace:
#             get_from_dict(namesp, arg)
#         else:
#             get_from_dict('global', arg)

# print(namespace)
# print(parents)

# Решение преподавателя:
# n = int(input())

# parent = {"global": None}
# vs = {"global": set()}

# for _ in range(n):
#     t, fst, snd = input().split()
#     if t == "create":
#         parent[fst] = snd
#         vs[fst] = set()
#     elif t == "add":
#         vs[fst].add(snd)
#     else:  # t == get
#         while fst is not None:
#             if snd in vs[fst]:
#                 break
#             fst = parent[fst]
#         print(fst)

# Решение из комментов:
# info = dict({'global':[None]})

# def create(namespace, parent):
#     info.update({namespace:[parent]})

# def add(namespace, var):
#     info[namespace].append(var)

# def get(namespace, var):
#     while namespace != None and var not in info[namespace][1:]:
#         namespace = info[namespace][0]
#     print(namespace)

# operations = {'create': create, 'add': add, 'get': get}
# for i in range(int(input())):
#     inp = input().split()
#     operations[inp[0]](inp[1], inp[2])

'''
###############################################
'''

# 1.5 Введение в классы

# class Dog():
#     '''Простая модель собаки'''

#     def __init__(self, name, age):
#         '''Инициализируем атрибуты - имя и возраст'''
#         self.name = name
#         self.age = age
#         print('Собака ' + self.name + ' создана')

#     def sit(self):
#         '''Собака будет садиться по команде'''
#         print(self.name.title() +  ' сел')
    
#     def jump(self):
#         '''Собака будет прыгать по команде'''
#         print(self.name.title() +  ' подпрыгнул')
    
#     def woof(self):
#         '''Собака будет гаркать по команде'''
#         print(self.name.title() +  ' гавкнул')


# my_dog = Dog('Topic', 4)
# my_dog_2 = Dog('Nick', 7)

# print(my_dog.age)
# print(my_dog.name)

# my_dog.jump()
# my_dog_2.sit()

# poppy = Dog('Poppy', 2)

# poppy.woof()


# class MyClass:
#     a = 10

#     def func(self):
#         print('Hello')

# # print(MyClass.a)
# # print(MyClass.func('a'))

# x = MyClass()
# print(type(x))
# print(type(MyClass))

# x = Counter()
# x.count = 0
# x.count += 1
# print(x.count)

# class Counter:
#     def __init__(self, start=0):
#         self.count = start

# Counter 
# x = Counter()
# x1 = Counter(10)
# print(x.count) # 0
# print(x1.count) # 10
# x.count += 1
# print(x.count) # 1


# class Counter:
#     def __init__(self):
#         self.count = 0
    
#     def inc(self):
#         self.count += 1

#     def reset(self):
#         self.count = 0

# Counter # class object
# x = Counter()
# x.inc() # Bound Method - связанный метод
# print(x.count) # 1
# Counter.inc(x) # x.inc == вызову функции Counter с методом inc с переменной х в качестве аргумента
# print(x.count) # 2
# x.reset()
# print(x.count) # 0


# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно 
# положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность 
# добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее вместимость.

# Класс должен иметь следующий вид

# При создании копилки, число монет в ней равно 0.
# Примечание:
# Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True.

''' Моё решение '''
# class MoneyBox:
#     def __init__(self, capacity, bank=0):
#         self.capacity = capacity
#         self.bank = bank

#     def can_add(self, v):
#         if self.capacity - self.bank >= v:
#             print('True' + ' Можно положить еще ' + str(self.capacity - self.bank) + ' монет')
#             return True
#         else:
#             print('False ' + ' Столько монет не войдёт, можно положить ещё ' + str(self.capacity - self.bank) + ' монет')
#             return False
#         # True, если можно добавить v монет, False иначе
''' Оптмизация из комментов'''
# return self.capacity - self.bank >= v

#     def add(self, v):
#         if self.can_add(v):
#             self.bank += v
#         else:
#             print('Не леззет. Можно положить только ' + str(self.capacity - self.bank))

#     def info(self):
#         print('В копилке ' + str(self.bank) + ' монет. Можно положить ещё ' + str(self.capacity - self.bank))
#         # положить v монет в копилку

# myMoneyBox = MoneyBox(10,1)
# myMoneyBox.info()

# Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой
# пятерки чисел из этой последовательности, затем сумму второй пятерки, и т. д.

# Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные 
# части. Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.

# Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму 
# пятерок последовательных элементов по мере их накопления.

# Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему 
# действительно необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой 
# была выведена сумма.

# Класс должен иметь следующий вид

# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]

# Обратите внимание, что во время выполнения метода add выводить сумму пятерок может потребоваться несколько 
# раз до тех пор, пока в буфере не останется менее пяти элементов.

# '''Моё решение'''

# class Buffer:
#     def __init__(self):
#         self.data = []
#
#     def add(self, *a):
#         self.data += a
#         while len(self.data) > 4:
#             print(sum(self.data[:5]))
#             self.data = self.data[5:]
#             del(self.data[:5]) # del работает быстрее, чем срез по списку
#
#     def get_current_part(self):
#         return(self.data)

# buf = Buffer()

'''Решение преподавателя'''
    # def add(self, *a):
    #     for i in a:
    #         self.part.append(i)
    #         if len(self.part) == 5:
    #             print(sum(self.part))
    #             self.part.clear()

'''Наследование классов'''

# class newClass(ParentClass1, ParentClass2):

# class MyList(list):
#     def even_lenght(self):
#         return len(self) % 2 == 0

# x = MyList()
# print(x) # []
# x.extend([1, 2, 3, 4, 5])
# print(x) # [1, 2, 3, 4, 5]
# print(x.even_lenght()) # False
# x.append(6)
# print(x.even_lenght()) # True

# class D: pass
# class E: pass           #object
# class B(D, E): pass   #D  #E 
# class C: pass           #B     #C
# class A(B, C): pass         #A

# issubclass(A, A) #True
# issubclass(C, D) #False
# issubclass(A, D) #True
# issubclass(C, object) #True
# issubclass(object, C) #False

# x = A
# isinstance(x, A) #True
# isinstance(x, B) #True
# isinstance(x, object) #True
# isinstance(x, str) #False

# isinstance - когда надо узнать является ли объект экземпляром 
# какого-то класса, issubclass - когда надо узнать является 
# ли он подклассом класса

# print(A.mro()) # Method resolution order
# [<class '__main__.A'>, <class '__main__.B'>, 
# <class '__main__.D'>, <class '__main__.E'>, 
# <class '__main__.C'>, <class 'object'>]

'''Проверка на четность длинны объекта'''
# class EvenLenghtMixin:
#     def even_lenght(self):
#         return len(self) % 2 == 0

# class MyList(list, EvenLenghtMixin):
#     pass

# class MyDict(dict, EvenLenghtMixin):
#     pass

# x = MyDict()
# x['key'] = 'value'
# x['another key'] = 'anothervalue'
# print(x.even_lenght()) #True


# '''Расширение функционала стандартного метода'''
# class EvenLenghtMixin:
#     def even_lenght(self):
#         return len(self) % 2 == 0
    
# class MyList(list, EvenLenghtMixin):
#     def pop(self): #заменяем стандартный метод pop
#         x = super(MyList, self).pop()
#         '''super - указание на родетеля передаваемого класса,'''
#         ''' т.е. браться будет list.pop'''
#         print('Last value is ', x)
#         return x
#     '''т.е. стандартный pop, но +вывод в консоль'''

# ml = MyList([1, 2, 4, 17])
# z = ml.pop() # Last value is 17
# print(z) # 17
# print(ml) # [1, 2, 4]

''' Задача на наследование '''
# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
# Или эквивалентно записи:
# class Class1(Class2, Class3 ... ClassK):
#     pass

# Класс A является прямым предком класса B, если B отнаследован от A:
# class B(A):
#     pass

# Класс A является предком класса B, если
# A = B;
# A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C
# Например:
# class B(A):
#     pass

# class C(B):
#     pass
# # A -- предок С

# Вам необходимо отвечать на запросы, является ли один класс предком другого класса

# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.

# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. 
# Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или 
# косвенно), что класс не наследуется явно от одного класса более одного раза.

# В следующей строке содержится число q - количество запросов.

# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

# Sample Input:
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A

# Sample Output:
# Yes
# Yes
# Yes
# No

# dictionary = {'classA': ['classB', 'classC', 'classD', 'classG', 'classH'], 'classB': ['classC', 'classE', 'classG', 'classH', 'classK', 'classL'], 'classC': ['classE', 'classD', 'classH', 'classK', 'classL'], 'classE': ['classD', 'classF', 'classK', 'classL'], 'classD': ['classG', 'classH'], 'classF': ['classK'], 'classG': ['classF'], 'classH': ['classL'], 'classK': ['classH', 'classL'], 'classL': []}

'''Моё решение'''

# dictionary = {}
# status = False

# def check_status(prnt, chld):
#     global status
#     if prnt == chld:
#         status = True
#     get_values(chld)
#     print('Yes' if status else 'No')

# def get_values(k):
#     global status
#     for i in dictionary[k]:
#         if i == prnt:
#             status = True
#         else:
#             get_values(i)
#     return status


# for _ in range(int(input())):
#     tmp = [i for i in input().split()]
#     if tmp[0] not in dictionary:
#         dictionary.update({tmp[0]: []})
#     if len(tmp) > 1:
#         for i in tmp[2:]:
#             dictionary[tmp[0]].append(i)

# for _ in range(int(input())):
#     prnt, chld = input().split()
#     status = False
#     check_status(prnt, chld)

'''Решение преподавателя'''

# n = int(input())

# parents = {}
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]

# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))

# q = int(input())
# for _ in range(q):
#     a, b = input().split()
#     print("Yes" if is_parent(b, a) else "No")

'''Задача на стек'''
# Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо 
# поддерживать добавление элемента на вершину стека, удаление с вершины стека, и необходимо 
# поддерживать операции сложения, вычитания, умножения и целочисленного деления.

# Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент 
# (top1), затем снимается следующий верхний элемент (top2), и затем как результат операции 
# сложения на вершину стека кладется элемент, равный top1 + top2.

# Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) 
# и целочисленного деления (top1 // top2).

# Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.

# Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop.
# Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента.

'''Моё решение, идентичное преподавателю'''
# class ExtendedStack(list):
#     def sum(self): 
#         print(self)
#         self.append(int(self.pop()) + int(self.pop()))
#         print(self)

#     def sub(self):
#         self.append(int(self.pop()) - int(self.pop()))

#     def mul(self):
#         self.append(int(self.pop()) * int(self.pop()))

#     def div(self):
#         self.append(int(self.pop()) // int(self.pop()))

'''задача 3'''

# Одно из применений множественного наследование – расширение функциональности класса каким-то 
# заранее определенным способом. Например, если нам понадобится логировать какую-то информацию 
# при обращении к методам класса.

# Рассмотрим класс Loggable:
# import time

# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))

# У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то 
# сообщение, добавляя при этом текущее время.
# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при 
# добавлении элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только 
# что добавленного элемента.

# Примечание
# Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот класс, 
# и он будет содержать метод log, описанный выше.

'''Мо1 решение'''
# class LoggableList(list, Loggable):
#     def append(self, data):
#         self.log(data)
#         return super(LoggableList, self).append(data) # super().append(data)

'''Решение преподавателя'''
# class LoggableList(list, Loggable):
#     def append(self, x):
#         list.append(self, x)
#         self.log(x)

