
# r (read) - открыть для чтения (по умолчанию)
# w (write) - открыть для записи, содержимое файла стирается
# a (append) - открыть для записи, запись ведется в конец
# b (binary) - открыть в бинарном ержиме
# r+ - открыть для чтения и записи
# w+ - открыть для чтения и записи, содержимое файла стирается

'''открытие файла и работа с ним'''

# f = open('test.txt', 'r')
# x = f.read(5) # читает первые 5 символов
# print(x)
# y = f.read()
# print(y)

# x = f.read()

# print(repr(x)) # представление х в виде строки
#  'First line\nSecond line\nThird Line\n'

# x = x.splitlines()
# print(repr(x)) # представление х в виде строки
# #  ['First line', 'Second line', 'Third Line']

# x = f.readline()
# print(repr(x))
# # 'First line\n'

# x = f.readline()
# print(repr(x))
# # 'Second line\n'


# x = f.readline()
# x = x.rstrip() # rstrip - убирает символы справа, без аргументов - служебные и пробелы
# # lstrip - слева
# print(repr(x))
# # 'First line'

"""Итератор по файлу для считывания построчно, не держит файл в памяти, берёт только нужную строку"""

# for line in f:
    # print(repr(line))
# 'First line\n'
# 'Second line\n'
# 'Third Line\n'

    # line = line.rstrip()
    # print(repr(line))
    # 'First line'
    # 'Second line'
    # 'Third Line'

# x = f.read()
# print(repr(x))
# # ''


# f.close()

'''Работа с файлом, запись в файл'''

# f = open('test1.txt', 'w')
# f.write('Hello')
# f.write('world')
# Helloworld

# f.write('Hello\n')
# f.write('world')
# Hello
# world

# f = open('test1.txt', 'w')
# lines = ['Line 1', 'Line 2', 'Line 3']
# contents = '\n'.join(lines)
# join принимает список и вставляет указанный символ между всеми элементами списка
# f.write(contents)
# Line 1
# Line 2
# Line 3

# f.close()

'''Дозапись в файл, метод append'''

# f = open('test_append', 'a')
# f.write('Hello\n')

# f.close()


'''Открытие файла с помощью менеджера контекста with'''


# with open('test.txt') as f, open('test_copy.txt', 'w') as w:
#     for line in f:
#         w.write(line)
#         line = line.strip()
#         print(line)

'''задание'''

# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

# Пример входного файла:
# ab
# c
# dde
# ff

# ﻿Пример выходного файла:
# ff
# dde
# c
# ab

'''моё решение'''

# lines = []

# f = open('dataset_24465_4.txt', 'r')
# x = f.read()
# x = x.splitlines()
# lines += x
# f.close()

# reversed_lines = []
# for i in range(len(lines) -1, -1, -1):
#     reversed_lines.append(lines[i])

# wr = open('tset.txt', 'w')
# contents = '\n'.join(reversed_lines)
# wr.write(contents)
# wr.close()

# with open('tset.txt') as f:
#     for line in f:
#         print(line)

'''Моё решение с доработкой после чтения комментов'''

# with open('test.txt') as f, open('tset.txt', 'w') as w:
#     lines = []
#     for line in f:
#         lines.append(line)
#     lines.reverse()

#     for line in lines:
#         w.write(line)

# lines = []

# f = open('test.txt', 'r')
# x = f.read()
# x = x.splitlines()
# lines += x
# f.close()

# lines.reverse()

# wr = open('tset.txt', 'w')
# contents = '\n'.join(lines)
# wr.write(contents)
# wr.close()

# with open('tset.txt') as f:
#     for line in f:
#         print(line)

        #     for line in f:
#         w.write(line)
#         line = line.strip()
#         print(line)

'''решение от других участников'''

# with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
#     fw.writelines(fr.readlines()[::-1])



# lines = open("input.txt").readlines()
# with open("output.txt", "w") as out:
#     out.writelines(reversed(lines))


'''Работа с операционной системой'''

# import os
# import os.path

# c
# # c:\code\learning\python\stepic512 выводит текущую директорию
# print(os.listdir())
# # выводит список файлов в дериктории
# print(os.listdir('part_two'))
# выводит содержимое указанной папки

# print(os.path.exists('check.py'))
# # True/False - наличие файла или директории в директории

# print(os.path.isfile('exeptions.py'))
# print(os.path.isfile('part_two'))

# print(os.path.isdir('exeptions.py'))
# print(os.path.isdir('part_two'))


# print(os.path.abspath('check.py'))

# print(os.getcwd())
# os.chdir('part_two')
# # можно сменить текущую директорию
# print(os.getcwd())


# os.walk - генерирует список из трёх элементов - адрес директории, вложенные директории, вложенные файлы
# и рекурсивно их обходит
# print(os.getcwd())
# for current_dir, dirs, files in os.walk('.'):
#     print(current_dir, dirs, files)


'''Копирование файлов'''

# import os
# import os.path
# import shutil

# shutil.copy('part_two/files.py', 'part_two/files_copy.py')
# shutil.copytree('part_two/tests', 'part_two/tests/test2')

#  if file.endswith(".py")
#  if file[-3:] == '.py'

'''Задание'''

# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все 
# директории, в которых есть хотя бы один файл с расширением ".py". 

# Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в 
# лексикографическом порядке.

# Для лучшего понимания формата задачи, ознакомьтесь с примером.

'''Мой решение'''

# import os
# import os.path

# answer = []

# for current_dir, dirs, files in os.walk('main'):
#     for file in files:
#         if file.endswith('.py'):
#             answer.append(current_dir)
#             break

# answer.sort()
# for item in answer:
#     print(item)


'''решения из ответов'''

# import os

# result = [cur_dir for cur_dir, dirs, files in os.walk("main") if any((fl.endswith(".py")
#     for fl in files))]

# with open("py_dirs.txt", "w") as w:
#     w.write("\n".join(sorted(result)))

###

# import os

# for cur_dir, subdirs, files in os.walk("main"):
#     for file in files:
#         if file.endswith(".py"):
#             print(cur_dir)
#             break

###

# import os
# with open('res.txt', 'w') as w:
#     w.write('\n'.join([p for p, d, f in os.walk('main') if any([i[-3:] == '.py' for i in f])]))

