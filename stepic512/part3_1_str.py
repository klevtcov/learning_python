''' Стандартные методы и функции для строк '''

# print('abc' in 'abcda') # True
# print('abce' in 'abcda') # False

# print('cabcd'.find('abc')) # индекс первого вхождения 1, или вернёт -1
# print(str.find.__doc__)
# # можно задать начало поиска, вернёт индекс изначалььной строки
# print('cabcd'.find('abc', 1))

# print('cabcd'.index('abc')) # индекс первого вхождения или ValueError

# s = 'The man in black fled across the desert, and the gunslinger followed'
# print(s.startswith('The man in black')) # True
# print(s.startswith('The woman', 'The dog', 'The man')) # any, True при любом из списка

# s = 'image.png'
# print(s.endswith('.png')) # True

# s = 'abacaba'
# print(s.count('aba')) # 2 количество вхождений

''' правосторонние аналоги, читающие строку с конца '''

# s = 'abacaba'
# print(s.find('aba')) # 0 - первое найденное вхождение 
# print(s.rfind('aba')) # 4 - первое найденое вхождение с конца стартует с 4-го индекса


# s = 'The man in black fled across the desert, and the gunslinger followed'
# print(s.lower()) # the man in black fled across the desert, and the gunslinger followed
# print(s.upper()) # THE MAN IN BLACK FLED ACROSS THE DESERT, AND THE GUNSLINGER FOLLOWED
# print(s.count('the')) # 2
# print(s.lower().count('the')) # 3

# s = '1,2,3,4'
# print(s) # 1,2,3,4
# print(s.replace(',', ', ')) # 1, 2, 3, 4
# print(s.replace.__doc__) # есть аргумент ан количество замен
# print(s.replace(',', ', ', 2)) # 1, 2, 3,4

# s = '1 2 3 4'
# print(s.split(' ')) # ['1', '2', '3', '4']
# print(s.split.__doc__) # есть аргумент ан количество разделений
# print(s.split(' ', 2)) # ['1', '2', '3 4']


# s = '   1, 2 3, 4    '
# # убирает ведущие пробельные символы
# print(repr(s.rstrip())) # '   1, 2 3, 4'
# print(repr(s.lstrip())) # '1, 2 3, 4    '
# print(repr(s.strip())) # '1, 2 3, 4'

# numbers = map(str, [1, 2, 3, 4, 5])
# print(repr(' '.join(numbers))) # '1 2 3 4 5'

''' форматирование '''
# capital = 'London is the capital of Great Britain'
# template = '{} is the capital of {}'
# print(template.format('London', 'Great Britain')) # London is the capital of Great Britain
# print(template.format('Vaduz', 'Liechtenstein')) # Vaduz is the capital of Liechtenstein
# template = '{1} is the capital of {0}' # указываем на каких места должны стоять аргументы
# print(template.format('London', 'Great Britain')) # Great Britain is the capital of London
# template = '{capital} is the capital of {country}' # именованные аргументы
# print(template.format(capital='London', country='Great Britain')) # London is the capital of Great Britain

# import requests

# template = 'Response from {0.url} with code {0.status_code}'
# res = requests.get('https://docs.python.org/3.5/')
# print(template.format(res)) # Response from https://docs.python.org/3.5/ with code 200

# res = requests.get('https://docs.python.org/3.5/random')
# print(template.format(res)) # Response from https://docs.python.org/3.5/random with code 404


# from random import random
# x = random()
# print(x) # 0.3473576926639479
# print('{:.3}'.format(x)) # 0.347

''' более актуальное на сегодня - f-строки https://shultais.education/blog/python-f-strings '''


''' задание '''

# Вашей программе на вход подаются три строки s, a, b, состоящие из строчных 
# латинских букв.
# За одну операцию вы можете заменить все вхождения строки a в строку s на 
# строку b.

# Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной 
# операции строка s перейдет в строку "baba", после выполнения двух и 
# операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

# Необходимо узнать, после какого минимального количества операций в 
# строке s не останется вхождений строки a. Если операций потребуется 
# более 1000, выведите Impossible.

# Выведите одно число – минимальное число операций, после применения 
# которых в строке s не останется вхождений строки a, или Impossible, 
# если операций потребуется более 1000.

# ababa, a, b - 1
# ababa, b, a - 1
# ababa, c, c - 0
# ababac, c, c - impossible




# s = input()
# a = input()
# b = input()

# counter = 0
# while a in s:
#     s = s.replace(a, b)
#     counter += 1
#     if counter > 1000:
#         print('Impossible')
#         break
# if counter < 1001:
#     print(counter)
# print(s.replace(',', ', ')) # 1, 2, 3, 4

''' решение из комментов '''

# s = input()
# a = input()
# b = input()

# if a not in s:
#     print(0)
# elif a in b:
#     print("Impossible")
# else:
#     ans = 0
#     while a in s:
#         s = s.replace(a, b)
#         ans += 1

#     print(ans)




# Вашей программе на вход подаются две строки s и t, состоящие из 
# строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
# Пример:
# s = "abababa"
# t = "aba"
# 3 
# Вхождения строки t в строку s:
# aba baba
# ab aba ba
# abab aba

# s = input()
# t = input()
# count = 0
# for i in range(len(s)):
#     if s[i::].startswith(t):
#         count += 1
# print(count)


