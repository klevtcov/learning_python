''' Регулярные выражения '''
# import re

# Полезные ссылки по регулярным выражениям:
# https://www.debuggex.com/cheatsheet/regex/python﻿ - лист с подсказками синтаксиса сгруппированный и компактный
# Онлайн визуализация:
# https://www.debuggex.com/
# https://regex101.com/#python

# Статья - https://tproger.ru/translations/regular-expression-python﻿
# Шпаргалка - http://www.exlab.net/files/tools/sheets/regexp/regexp.pdf
# Тренировочный сайт - https://regexcrossword.com/


''' сырая строка raw '''

# x = 'hello\"world' # служебный обратный слеш
# print(x) # hello"world

# x = r'hello\"world'
# print(x) # hello\"world

# print(re.match) # проверяет подходит ли начало строки под наш шаблон
# print(re.search) # берёт строку и находит первую подстроку, подходящую под шаблон
# print(re.findall) # находит вссе подстроки строки, подходящие под шаблон
# print(re.sub) # заменяет все вхождения подстрок, подходящих под наш шаблон на другие даннеы

# pattern = r'abc'
# string = 'abc'
# match_object = re.match(pattern, string)
# print(match_object) # <re.Match object; span=(0, 3), match='abc'>

# pattern = r'abc'
# string = 'babc'
# match_object = re.search(pattern, string)
# print(match_object) # <re.Match object; span=(1, 4), match='abc'>

# [] можно указать множество подходящих символов
# pattern = r'a[abc]c'
# string = 'aac'
# match_object = re.match(pattern, string)
# print(match_object) # <re.Match object; span=(0, 3), match='aac'>

# string = 'abc, acc, acc'
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions) # ['abc', 'acc', 'acc']

# fixed_typos = re.sub(pattern, 'abc', string)
# print(fixed_typos) # abc, abc, abc


# Метасимволы в регулярных выражениях
# . ^ $ + ? { } [ ] \ | ( ) -- метасимволы

# pattern = r' english?' # так знак вопроса не попадёт в поиск, т.к. это метасимвол
# pattern = r' english\?' # а так попадёт
# string = 'Do you speak english?'
# match = re.search(pattern, string)
# print(match) # <re.Match object; span=(12, 21), match=' english?'>

# pattern = r'a[a-c]c'
# string = 'aсc'
# match_object = re.match(pattern, string)
# print(match_object) # None

# string = 'abc, acc, acc'
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions) # ['abc', 'acc', 'acc']

# fixed_typos = re.sub(pattern, 'abc', string)
# print(fixed_typos) # abc, abc, abc

# Поиск всех букв английского алфавита
# 'a[a-zA-Z]c'

# Не включает символы
# 'a[^a-zA-Z]c'
# подходят только a1c, a.c, a-c

#  Короткая запись часто используемых выражений
# \d ~ [0-9] – цифры
# \D ~ [^0-9] – не цифры
# \s ~ [ \t\n\r\f\v] – пробельные символы
# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] — буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]
# 'a.c' # точка - любой символ

# Буква ё не входит в диапазон а-я, а Ё не входит в А-Я

# import re
# regex1 = r"\b[а-яА-Я]+"
# regex2 = r"\b[а-яА-ЯёЁ]+"
# s = "Ежиха ела ёлку. Ёжик сел на ель."
# print(re.findall(regex1, s)) # ['Ежиха', 'ела', 'сел', 'на', 'ель']
# print(re.findall(regex2, s)) # ['Ежиха', 'ела', 'ёлку', 'Ёжик', 'сел', 'на', 'ель']

# Алфавит идет так эюяё ЁАБВ. Поэтому заглавные пишем так: [Ё-Я].
# regex1 = r"\b[а-яА-Я]+"
# regex2 = r"\b[а-ёЁ-Я]+"

# s = "Ежиха ела ёлку. Ёжик сел на ель."

# print(re.findall(regex1, s))
# print(re.findall(regex2, s))

# Повторения символа

# pattern = r'ab*a' # любое количество символов b, включая 0
# pattern = r'ab+a' # любое положительное количество символов b
# pattern = r'ab?a' # 0 или 1 вхождение символа b
# pattern = r'ab{2}a' # конкретное количество символов или диапазон {2,4} - от 2 до 4. {,3} - меньше или равно 3, {3,} - больше или равно 3
# string = 'aa, aba, abba'
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions) # * ['aa', 'aba', 'abba']
# print(all_inclusions) # + ['aba', 'abba']
# print(all_inclusions) # ? ['aa', 'aba']
# print(all_inclusions) # {2} ['abba']

# жадные метасимволы - [] вернёт наибольшее значение
# 'a[ab]+a'
# 'abaababa'
# match вернёт самую большую из возможных последовательностей

# pattern = r'a[ab]+a' # жадный, пытается взять максимальную последовательность
# string = 'abaaba'
# print(re.match(pattern, string)) # <re.Match object; span=(0, 6), match='abaaba'>
# print(re.findall(pattern, string)) # ['abaaba']

# pattern = r'a[ab]?a' # ? не жадный, хватает минимальной последовательности
# string = 'abaaba'
# print(re.match(pattern, string)) # <re.Match object; span=(0, 3), match='aba'>
# print(re.findall(pattern, string)) # ['aba', 'aba']

# Список всех файлов с картинками с сайта
# import requests
# import re

# site = 'https://stepik.org'
# pattern = r'https[\S.]+(?:png|jpg|gif)'
# string = requests.get(site).content
# m_o = re.findall(pattern, string.decode('utf-8'))
# print(m_o)

# pattern = r'/[\S.]+(?:png|jpg|gif)'
# m_o = re.findall(pattern, string.decode('utf-8'))
# for i in range(len(m_o)):
#     m_o[i] = site + m_o[i]
# print(m_o)


# Группировка символов

# pattern = r'(test)*'
# string = 'test'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 4), match='test'>
# string = 'testtest'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 8), match='testtest'>

# pattern = r'(test|text)*' # логическое или
# string = 'testtest'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 8), match='testtest'>
# string = 'testtext'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 8), match='testtext'>

# pattern = r'((abc)|(test|text)*)' # 
# string = 'abc'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 3), match='abc'>
# print(match.groups()) # ('abc', 'abc', None) есть совпадение в первой группе шаблона - всё регулярное выражение, вторая группа - шаблон 'abc', тоже присутствует, None для третьеё группы - второй части всей регулярки
# string = 'testtext'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 8), match='testtext'>
# print(match.groups()) # ('testtext', None, 'text') - всё, первая половина, вторая половина

# pattern = r'Hello (abc|test)' # 
# string = 'Hello abc'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 9), match='Hello abc'>
# print(match.group()) # Hello abc
# print(match.group(0)) # Hello abc
# print(match.group(1)) # abc

# Использование группы внутри регулярного выражения

# pattern = r'(\w+)-\1' # находим группу, которую уже собрали раньше, поиск повторяющихся значений \1 - номер группы, или номер открывающей скобки
# string = 'test-test'
# match = re.match(pattern, string)
# print(match) # <re.Match object; span=(0, 9), match='test-test'>
# string = 'test-text'
# match = re.match(pattern, string)
# print(match) # None

# pattern = r'(\w+)-\1' # находим группу, которую уже собрали раньше, поиск повторяющихся значений \1 - номер группы, или номер открывающей скобки
# string = 'test-test chow-chow'
# duplicates = re.sub(pattern, r'\1', string) # оставляем только первое слово из пары повторяющихся слов
# print(duplicates) # test chow

# pattern = r'(\w+)-\1' 
# string = 'test-test chow-chow'
# find_all = re.findall(pattern, string) 
# print(find_all) # ['test', 'chow']

# pattern = r'((\w+)-\2)' # меняем на 2, т.к. открывающая скобка вторая
# string = 'test-test chow-chow'
# find_all = re.findall(pattern, string) 
# print(find_all) # [('test-test', 'test'), ('chow-chow', 'chow')] - первое вхождение - всё регулярное выражение целиком, второе - повторяющееся вхождение

# игнрирование строчных и прописынх
# x = re.match(r'text', 'TEXT', re.IGNORECASE)
# print(x) # <re.Match object; span=(0, 4), match='TEXT'>

# x = re.match(r'(te)*xt', 'TEXT', re.IGNORECASE | re.DEBUG)
# print(x) # <re.Match object; span=(0, 4), match='TEXT'>

# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.

# моё решение
# import sys
# import re

# pattern = r'(cat)'

# for line in sys.stdin:
#     line = line.rstrip()
#     find_all = re.findall(pattern, line) 
#     # if len(find_all) > 1: # find_all возвращает список вхождений, можно просто посчитать длинну списка
#         # print(line)
#     counter = find_all.count('cat')
#     if counter > 1:
#         print(line)


# line = ['catcat', 'cat and cat', 'catac', 'cat', 'ccaatt']


# pattern = r'(cat)' 
# lines = ['catcat', 'cat and cat', 'catac', 'cat', 'ccaatt']
# for line in lines:
#     find_all = re.findall(pattern, line)
#     counter = find_all.count('cat')
#     if counter > 1:
#         print(line)

# решение из комментов

# if len(re.findall("cat", line)) > 1:
#     print(line)

# if re.search(r"cat.*cat", line):
#         print(line)

# if(re.match(r"(.*(cat).*){2,}",line)):
#         print(line)

# Выведите строки, содержащие "cat" в качестве слова.

# Моё решение
# pattern = r'\b(cat)\b' 
# lines = ['cat', 'catapult and cat', 'catcat', 'concat', 'Cat', '"cat"', '!cat?']

# import sys
# import re

# for line in sys.stdin:
#     line = line.rstrip()
#     if re.findall(r'\b(cat)\b', line):
#         print(line)

# Из комментов

# if re.search(r"\bcat\b", line):
#         print(line)

# print(*[line for line in sys.stdin if re.search(r"\bcat\b", line)], sep='') # наркоманы, не повторять в продакшене)


# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

# Моё решение

# import sys
# import re
# lines = ['zabcz', 'zzz', 'zzxzz', 'zz', 'zxz', 'zzxzxxz']
# for line in lines:
#     if re.search(r'z.{3}z', line):
#         print(line)

# import sys
# import re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'z.{3}z', line):
#         print(line)

# Из комментов
#     if re.search(r"z...z", line):
#         print(line)

# sys.stdout.writelines(filter(re.compile('z...z').search, sys.stdin))


# Выведите строки, содержащие обратный слеш "\".

# import sys
# import re
# lines = ['\w denotes word character', 'No slashes here']
# for line in lines:
#     if re.search(r'\\', line):
#         print(line)

# import sys
# import re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\\', line):
#         print(line)

# # другие решения 
# print(*filter(lambda line: "\\" in line, sys.stdin), sep='') # наркоманы)  

# for line in stdin.read().splitlines(): # без регулярок
#     if '\\' in line:
#         print(line)


# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

# import sys
# import re
# lines = ['blabla is a tandem repetition', '123123 is good too', 'go go', 'aaa']
# for line in lines:
#     if re.match(r'\b(\w+)\1\b', line):
#         print(line)

# import sys
# import re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.match(r'\b(\w+)\1\b', line):
#         print(line)

# из комментов

#     if re.search(r"\b(\w+)\1\b", line):
#         print(line)

#     if re.search(r"(\b.*\B)\1\b", line): # B - не содержит пробел, т.е. смотрим любые символы внутри слова
#         print(line) 

# sys.stdout.writelines(filter(re.compile(r"\b(\w+)\1\b").search, sys.stdin))


# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.

# import sys
# import re
# lines = ['I need to understand the human mind', 'humanity']
# for line in lines:
#     print(re.sub(r'human', r'computer', line))

# import sys
# import re
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'human', r'computer', line))


# # Другие решения

# print(re.sub(r'human', 'computer', sys.stdin.read()), end='')

# print(*[re.sub(r'human', 'computer', line) for line in sys.stdin], sep='')

# for line in sys.stdin:
#     print(re.sub('human', 'computer', line.rstrip()))


# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

# import sys
# import re
# answer = []
# lines = ['There’ll be no more "Aaaaaaaaaaaaaaa"', 'AaAaAaA AaAaAaA']
# for line in lines:
#     print(re.sub(r'(\b[a|A*]+)\b', r'argh', line, count=1))

# import sys
# import re
# for line in sys.stdin:
#     print(re.sub(r'(\b[a|A*]+)\b', r'argh', line.strip(), count=1))


# Другие решения
# for line in sys.stdin:
#     line = line.strip()
#     line = re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE)
#     print(line)

# [print(re.sub(r'\b[aA]+\b', 'argh', line.rstrip(), 1)) for line in sys.stdin]


# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.

# import sys
# import re
# lines = ['this is a text', '"this\' !is. ?n1ce,']
# for line in lines:
#     print(re.sub(r'\b([\w])([\w])', r'\2\1', line.rstrip()))

# import sys
# import re
# for line in sys.stdin:
#     print(re.sub(r'\b([\w])([\w])', r'\2\1', line.rstrip()))

# Другие решения
# line = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)


#  В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
#  Буквой считается символ из группы \w.

# import sys
# import re
# lines = ['attraction', 'buzzzz']
# for line in lines:
#     line = line.rstrip()
#     while(re.findall(r'(\w+)\1', line)):
#         line = re.sub(r'(\w+)\1', r'\1', line)
#     print(line)

# import sys
# import re
# for line in sys.stdin:
#     line = line.rstrip()
#     while(re.findall(r'(\w+)\1', line)):
#         line = re.sub(r'(\w+)\1', r'\1', line)
#     print(line)

# Другие решения
# line = re.sub(r"(\w)\1+", r"\1", line) # берём символ w, его повторение \1 любое количество раз +

# sys.stdout.write(re.sub(r"(\w)\1+", r"\1", sys.stdin.read()))


# Задача со звёздочкой
# Выведите строки, содержащие двоичную запись числа, кратного 3.
# '0', '10010', '00101', '01001', 'Not a number', '1 1', '0 0'
# Вывод - 0 10010 01001

# import sys
# import re
# lines = ['0', '10010', '00101', '01001', 'Not a number', '1 1', '0 0']
# for line in lines:
#     line = line.rstrip()
#     if re.fullmatch(r'(1(01*0)*1|0)*', line):
#         print(line)

# import sys
# import re
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.fullmatch(r'/^((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+)?1)(10*1)*(1(0+)?)|(0(0+)?)))$/', line):
#         print(line)


# В основном подсчитайте количество ненулевых битов 
# нечетных позиций и ненулевых четных битов позиции справа. 
# Если их разность делится на 3, то число делится на 3.

# (^[10]*$)

# /^((((0+)?1)(10*1)*0)(0(10*1)*0|1)*(0(10*1)*(1(0+)?))|(((0+)?1)(10*1)*(1(0+)?)|(0(0+)?)))$/

# Из ответов
# pattern = "^(0|(1(01*0)*1))*$"
# pattern = re.compile(pattern)
# for line in sys.stdin:
#     line = line.rstrip()
#     if pattern.match(line):
#         print(line)
