
# try:
#     x = [2, 1, 'hello', 3]
#     x.sort()
#     print(x)
# except TypeError:
#     print('Type error :(')

# print('I can catch')

# def f(x, y):
#     try:
#         return x / y
#     except TypeError:
#         print('Type error')
#     except ZeroDivisionError:
#         print('Zero division :(')

# f(5, [])
# print(f(5, 0))

# try:
#     print(f(5, 0))
# except ZeroDivisionError:
#         print('Zero division :(')

# def f(x, y):
#     try:
#         return x / y
#     except (TypeError, ZeroDivisionError) as e:
#         print(e)
#         print(type(e))
#         print(e.args)

# print(f(5, 0))
# print(f(5, []))

# def f(x, y):
#     try:
#         return x / y
#     except:
#         print('Error')
# print(f(5, 0))
# print(f(5, []))

# try:
#     15 / 0
#     # создаётся объект
# except ZeroDivisionError: # isinstance(объект, ZeroDivisionError) == True
#     print('Division by zero')

# print(ZeroDivisionError.mro())

# def devide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print('division by zero')
#     else:
#         print('result is', result)
#     finally:
#         print('finally')

# devide(2, 1)
# devide(2, 0)
# devide(2, [])

# Вашей программе будет доступна функция foo, которая может бросать исключения.

# Вам необходимо написать код, который запускает эту функцию, затем ловит исключения 
# ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

# Пример решения, которое вы должны отправить на проверку.
# Пример решения, которое вы должны отправить на проверку.

# try:
#     foo()
# except AssertionError:
#     print("AssertionError")
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")

# print(ZeroDivisionError.mro())


# Вам дано описание наследования классов исключений в следующем формате.
# <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
# Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

# Или эквивалентно записи:

# class Error1(Error2, Error3 ... ErrorK):
#     pass

# Антон написал код, который выглядит следующим образом.

# try:
#    foo()
# except <имя 1>:
#    print("<имя 1>")
# except <имя 2>:
#    print("<имя 2>")
# ...
# Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, 
# так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются 
# от каких. Помогите ему выйти из неловкого положения и напишите программу, которая будет 
# определять обработку каких исключений можно удалить из кода.

# Важное примечание:
# В отличие от предыдущей задачи, типы исключений не созданы.
# Создавать классы исключений также не требуется
# Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, 
# потому что мы уже ранее где-то поймали их предка.

# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов исключений.

# В следующих n строках содержится описание наследования классов. В i-й строке указано от каких 
# классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. 
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не 
# наследуется явно от одного класса более одного раза.

# В следующей строке содержится число m - количество обрабатываемых исключений.
# Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у 
# Антона в коде.
# Гарантируется, что никакое исключение не обрабатывается дважды.

# Формат выходных данных
# Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из 
# кода, не изменив при этом поведение программы. Имена следует выводить в том же порядке, 
# в котором они идут во входных данных.

# Пример теста 1
# Рассмотрим код

# try:
#    foo()
# except ZeroDivision :
#    print("ZeroDivision")
# except OSError:
#    print("OSError")
# except ArithmeticError:
#    print("ArithmeticError")
# except FileNotFoundError:
#    print("FileNotFoundError")

# По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение 
# FileNotFoundError можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError
# Sample Input:

# 4
# ArithmeticError
# ZeroDivisionError : ArithmeticError
# OSError
# FileNotFoundError : OSError
# 4
# ZeroDivisionError
# OSError
# ArithmeticError
# FileNotFoundError
# Sample Output:

# FileNotFoundError

# 4
# BaseException
# Exception : BaseException
# LookupError : Exception 
# KeyError : LookupError
# 2
# BaseException
# KeyError
# out:
# KeyError 

# dictionary = {}

# dictionary = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError'], 'OSError': [], 'FileNotFoundError': ['OSError']}
# usedClasses = set()
# status = False

# def chekKinship(item):
#     for i in usedClasses:
#         print('Item now is', item, 'dict i is ', i)
#         if dictionary[item] == i:
#             print(item)
#             break
#         elif dictionary[item] == []:
#             break
#         else:
#             chekKinship(dictionary[item])

# def lookingForParents(chld):
#     if dictionary[chld] in dictionary:
#         dictionary[chld]



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



# for _ in range(int(input())):
#     tmp = [i for i in input().split()]

#     if tmp[0] not in dictionary:
#         dictionary.update({tmp[0]: []})
#     if len(tmp) > 1:
#         for i in tmp[2:]:
#             dictionary[tmp[0]].append(i)


# for _ in range(int(input())):
#     tmp = input()
#     chekKinship(tmp)
#     usedClasses.update([tmp])

# print(usedClasses)


# for _ in range(int(input())):
#     tmp = input()
    
#     if tmp 

#     if tmp[0] not in dictionary:
#         dictionary.update({tmp[0]: []})
#     if len(tmp) > 1:
#         for i in tmp[2:]:
#             dictionary[tmp[0]].append(i)

# for _ in range(int(input())):
#     prnt, chld = input().split()
#     status = False
#     check_status(prnt, chld)

# for _ in range(int(input())):
#     tmp = [i for i in input().split()]
#     if tmp[0] not in dictionary:
#         dictionary.update({tmp[0]: []})
#     if len(tmp) > 1:
#         for i in tmp[2:]:
#             dictionary[tmp[0]].append(i)

# 4
# BaseException
# Exception : BaseException
# LookupError : Exception 
# KeyError : LookupError
# 2
# BaseException
# KeyError
# out:
# KeyError 


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


# '''Исключения - ловля и бросание'''

# from multiprocessing.sharedctypes import Value

# class BadName(Exception):
#     pass

# def greet(name):
#     if name[0].isupper():
#         return 'Hello, ' + name
#     else:
#         raise BadName(name + ' is inappropriate name')

# # print(greet('Anton'))
# # print(greet('anton'))

# while True:
#     try:
#         name = input('Please enter your name: ')
#         greeting = greet(name)
#         print(greeting)
#     except ValueError:
#         print('Please try again')
#     else:
#         break


# Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
# Также реализуйте новое исключение NonPositiveError.

# В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное 
# целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое 
# число, число добавлялось бы как в стандартный list.

# В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

# Примечание:
# Положительными считаются числа, строго большие нуля.


class PositiveList(list):
    
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError

class NonPositiveError(Exception):
    pass

