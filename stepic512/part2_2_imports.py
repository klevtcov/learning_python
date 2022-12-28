# # Работа с кодом: модули и импорт

# import exeptions
# import fib
# import sys
# import check

# print(exeptions.greet('Students'))

# print(fib.fib(5))

# print(sys.modules)
# print(type(check))

# print(id(check))
# import check
# print(id(check))

# for path in sys.path:
#     print(path)

'''Задание'''

# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.

# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.

# Примечание:
# Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.

''' моё решение'''

# import datetime

# date = input().split(' ')
# x = datetime.date(int(date[0]), int(date[1]), int(date[2]))

# days = datetime.timedelta(int(input()))
# result = str(x + days).split('-')

# print(int(result[0]), int(result[1]), int(result[2]))

'''решение из ответов'''

# import datetime
# inp = datetime.datetime.strptime(input(), "%Y %m %d")
# inp += datetime.timedelta(days=int(input())) 
# print(f'{inp.year} {inp.month} {inp.day}')

# import datetime
# d = datetime.date(*map(int, input().split())) + datetime.timedelta(days=int(input()))
# print(d.year, d.month, d.day)

# без звездочки это будет массив
# забей в интерпретатор, этот вывод массива, то есть если без звездочки, 
# то это (например) [1, 2, 3],  а со звездочкой: 1 2 3. Это просто сокращение, 
# смысл тот же, что и for i in range(len(a)): print(a[i], sep = ' ') 
# (например массив а = [1, 2, 3])

'''Можно импортировать отдельные блоки/функции, можно с освоими именами'''
# from exeptions import BadName as bn

'''Запрет на импорт отдельных компонентов при from X import * '''

# GREETING = 'Hello, '

# class BadName(Exception):
#     pass

# def greet(name):
#     if name[0].isupper():
#         return GREETING + name
#     else:
#         raise BadName(name + ' is inappropriate name')

# __all__ = ['BadName', 'greet'] - перечисляются импортирующиеся функции и классы
# или защитить функцию через нижнее подчеркивание - _GREETING

# import simplecrypt

# with open("encrypted.bin", "rb") as inp:
#     encrypted = inp.read()
#     # print(simplecrypt.decrypt(passwordss, encrypted))

# with open('passwords.txt', 'r') as passwrd:
#     passwordss = passwrd.readlines()
#     print(passwordss)

# for n in passwordss:
#     try:
#         n = n.strip()
#         print(simplecrypt.decrypt(n, encrypted))
#     except simplecrypt.DecryptionException:
#         print('exept')



# from simplecrypt import encrypt, decrypt

# encrypted = open("encrypted.bin", "rb").read()
# all_passwords = open("passwords.txt").readlines() # здесь нужно не забыть, что в каждый пароль попадёт лишний '\n'

# for password in all_passwords:
#     try:
#         # Сделаем попытку расшифровать сообщение. Это будет именно попытка, так как в случае неудачи:
#         # - мы не получим - НЕ ПОЛУЧИМ - ошибочно расшифрованное сообщение
#         # - ещё раз: мы не получим бессмысленный набор символов из-за неверно указанного пароля
#         # - мы поймаем исключение, которое прервёт работу нашей программы
#         # - программа завершит свою работу и следующей попытки расшифровать уже не произойдёт!
#         text = decrypt(password.strip(), encrypted).decode('utf8')# эта строчка выдаёт проблемы
#         print(text)
#         break # а зачем здесь брейк? Все поняли? **(см. ниже)
#     except:
#         continue # если всё-таки попытка расшифровки не удалась, то не нужно отчаиваться
#         # нужно просто завершить текущую итерацию в цикле и, игнорируя прерывание/исключение, попытаться ещё раз


