''' Распространённые форматы текстовых файлов: CSV, JSON '''

# import csv

# with open('example.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# with open('example.tsv') as f:
#     reader = csv.reader(f, delimiter='\t')
#     for row in reader:
#         print(row)

# students = [
#     ['Greg', 'Dean', 70, 80, 90, 'Good job, Greg'],
#     ['Wirt', 'Wood', 80, 80.2, 80, 'Nicely done']
# ]

# with open('example.csv', 'a') as f:
#     writter = csv.writer(f)
#     # writter = csv.writer(f, quoting=csv.QUOTE_ALL) # все значения будут в кавычках
#     # writter = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC) # все не числовые значения будут в кавычках
#     # writter.writerows(students)
#     for student in students:
#         writter.writerow(student)


# Информация хорошо закрепляется, в связке с:
# Работа с файлами в формате CSV - https://pyneng.readthedocs.io/ru/latest/book/17_serialization/csv.html
# Работа с файлами в формате CSV, JSON, YAML - https://pyneng.readthedocs.io/ru/latest/book/17_serialization/index.html#csv-json-yaml
# Подробнее про JSON - https://python-scripts.com/json

''' задание '''
# Вам дана частичная выборка из датасета зафиксированных преступлений, 
# совершенных в городе Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.

# Вам необходимо узнать тип преступления, которое было зафиксировано 
# максимальное число раз в 2015 году.

# Как решать задачу - надо разбираться самим. Помогли комментарии, спасибо за них!
# Использовал модули/методы:
# -  csv метод csv.DictReader() считывание данных (это второй способ чтения csv , 
# наряду с csv.reader())
# -  time метод time.strptime() разбор строки, представляющей время, для дальнейшей 
# сортировки данных по году
# -  collections метод collections.Counter() подсчет количества преступлений по 
# их видам

# Не претендую на истину в последней инстанции, но я с помощью этого решил задачу.


# import csv
# import collections

# result = []
# with open('crimes.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if '2015' in row['Date']:
#             result.append(row['Primary Type'])
# cnt = collections.Counter(result)
# print(cnt.most_common(1)[0][0])

### Другие решения

# from collections import Counter as c
# import csv

# with open('Crimes.csv') as f:
#     data = csv.reader(f)
#     print(c( row[5] for row in data if '2015' in row[2] ))


# import csv

# with open("Crimes.csv") as f:
#      reader = csv.reader(f)
#      crimes = []
#      for row in reader:
#          if "2015" in row[2]:
#              crimes.append(row[5])
#      print(max(crimes, key=crimes.count))


# import csv
# with open("Crimes.csv") as f:
#     file = csv.reader(f)
#     primary = [row[5] for row in file if "2015" in row[2]]
#     p_count = [primary.count(i) for i in primary]
#     print(primary[p_count.index(max(p_count))])

###


''' JSON '''

# import json

# student1 = {
#         "first_name": "Oleg",
#         "last_name": "Dean",
#         "certificate": True,
#         "scores": [70, 80, 90],
#         "description": "Good job, Greg"
#         }

# student2 = {
#         "first_name": "Wirl",
#         "last_name": "Wood",
#         "certificate": True,
#         "scores": [80, 80.2, 80],
#         "description": "Nicely Done"
#         }

# data = [student1, student2]
# print(json.dumps(data, indent=4, sort_keys=True))
# with open('students.json', 'w') as f:
#     json.dump(data, f, indent=4, sort_keys=True)

# data_json = json.dumps(data, indent=4, sort_keys=True)
# data_again = json.loads(data_json)
# print(sum(data_again[0]['scores']))

# with open('students.json', 'r') as f:
#     data_again = json.load(f)
#     print(sum(data_again[1]['scores']))

# https://youtu.be/rIhygmw9HZM хороший урок по json

''' Задание '''
# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]



# https://github.com/mxmaslin/stepik/blob/master/Python%20-%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%B8%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5/3.5%20%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%91%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D1%8B%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D1%85%20%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%20CSV%2C%20JSON%204.md
# import json

# initial = json.loads(input())

# with_children = {element['name']: [] for element in initial}

# for eli in initial:
#     for elc in with_children:
#         if elc in eli['parents']:
#             with_children[elc].append(eli['name'])

# for element in with_children:
#     with_children[element] = set(with_children[element])

# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)
#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited

# for element in sorted(with_children.keys()):
#     print(element, ':', len(dfs(with_children, element)))

## ещё решение
# import json

# def test(x, c):
#     for i in z:
#         if x in i['parents']:
#             c.add(i['name'])
#             c = test(i['name'], c)
#     return (c)

# z = json.loads(input())
# z.sort(key=(lambda x: x['name']))
# for i in z:
#     print(i['name'], ':', len(test(i['name'], c = set()))+ 1)


