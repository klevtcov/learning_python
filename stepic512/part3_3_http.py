''' Обзорно об интернете: http-запросы, html-страницы и requests '''

# url - uniform resource locator
# http, ftp - протокол
# домен
#  /путь

# Request:
# методы:
# Get - запрос на получение данных
# Post - изменяет запрашиваемые данные - пароли, данные и т.д.

# Response
#    Header - версия протокола, код ответа, адрес
#    Body

# html - язык разметки

# import requests

# res = requests.get('http://docs.python.org/3.5/')
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.content)
# print(res.text)

# res = requests.get('http://docs.python.org/3.5/_static/py.png')
# with open('python.png', 'wb') as f:
#     f.write(res.content)

# res = requests.get('http://yandex.ru/search/',
#                     params={'text': 'Stepic'})
# print(res.status_code)
# print(res.headers['Content-Type'])
# print(res.url)
# print(res.text)

# Задание
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
# yes

# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample1.html
# no

# https://stepic.org/media/attachments/lesson/24472/sample1.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html
# yes

# Решается за один цикл и одну функцию. Шаги следующие:
# Переходим по начальной ссылке
# Ищем регулярным выражением все ссылки на странице
# Для каждой ссылки вызываем функцию, которая:
#   Переходит по ссылке
#   Ищем регулярным выражением все ссылки на странице
#   Проверяет, есть ли среди них искомая
# Если искомая ссылка найдена - печатаем Yes, если дошли до конца массива и ничего не нашли - печатаем No

# - получил 2 урла, записал их в переменные,
# - сделал запрос по первому урлу, с помощью регулярки нашел все урлы и 
# записал их в список
# - прошелся по списку и сделал запросы по каждому из них, ответы также 
# обработал регуляркой и поместил в список
# - проверил вхождение нужного мне урла в список

# url1 = 'https://stepic.org/media/attachments/lesson/24472/sample0.html'
# url2 = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'

# import requests
# import re

# url1 = input()
# url2 = input()

# pattern = re.compile(r'(https?:\/\/?[\da-z\.-]+\.[a-z\.]{2,6}[\/\w \.-]*\/?)')
# res = requests.get(url1)
# match_url1 = re.findall(pattern, res.text)
# match_url2 = []
# flag = False
# for url in match_url1:
#     res2 = requests.get(url)
#     match_url2.extend(re.findall(pattern, res2.text))
# if url2 in match_url2:
#     flag = True
# if flag: 
#     print('Yes')
# else:
#     print('No')


# Решения из комментов
# import re
# import requests

# start_url = input()
# end_url = input()

# found = False

# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')

# resp = requests.get(start_url).text
# for url in link_pattern.findall(resp):
#     cur_resp = requests.get(url).text
#     if end_url in link_pattern.findall(cur_resp):
#         found = True
#         break

# print("Yes" if found else "No")

###
# что значит это выражение (.*?)
# ? после *, + или ? уменьшает "жадность". По-умолчанию, модуль re ищет 
# фрагмент максимальной длины, удовлетворяющий регулярному выражению. 
# Если же добавить знак "?", то жадность будет уменьшена и будет искаться 
# фрагмент минимальной длины.
###

# import requests, re

# urls = [input() for cmd in range(2)]
# p = 'No'

# for i in re.findall(r'<a.*href="(.*)">', requests.get(urls[0]).text):
#     if urls[1] in re.findall(r'<a.*href="(.*)">', requests.get(i).text):
#         p = 'Yes'
#         break
# print(p)

### 

# import requests
# import re

# def test(a, b):
#     for f in re.findall(r'<a href="(.*)">', requests.get(a).text):
#         if b in re.findall(r'<a href="(.*)">', requests.get(f).text):
#             return 'Yes'
#     return 'No'

# print(test(input(), input()))

###

# import requests, re
# a, b = input(), input()
# c = re.findall(r'<a href="(.+)">', requests.get(a).text)
# if any(b in requests.get(i).text for i in c):
#   print('Yes')
# else:
#   print('No')

###


''' Задание '''

# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида 
# <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.

# Сайтом в данной задаче будем называть имя домена вместе с именами 
# поддоменов. То есть, это последовательность символов, которая следует 
# сразу после символов протокола, если он есть, до символов порта или 
# пути, если они есть, за исключением случаев с относительными ссылками 
# вида
# <a href="../some_path/index.html">.

# Сайты следует выводить в алфавитном порядке.

# import requests
# import re

# urls = []
# url = input().strip()
# pattern = re.compile(r'(?:<a.+?href.*?=.*?[\'\"])(?:.+?:\/\/)?([\w\-\.]+)')
# res = requests.get(url)
# urls.extend(re.findall(pattern, res.text))

# set_url = set()

# for i in urls:
#     if i != ['..']:
#         set_url.update(i)

# print(sorted(set_url))

# Решение из интернета
# import re
# import urllib.request
# from urllib.parse import urlparse

# url = input()


# def get_links():
#     try:
#         fp = urllib.request.urlopen(url)
#         mybytes = fp.read()
#         mystr = mybytes.decode("utf8")
#         fp.close()
#         links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', mystr)
#     except:
#         return []
#     else:
#         return links


# def parse_link(link):
#     parsed_uri = urlparse(link)
#     res = parsed_uri.netloc
#     try:
#         return res[:res.index(':')]
#     except:
#         return res
#     else:
#         return res[:res.index(':')]


# links = get_links()

# unsorted = list(map(parse_link, links))

# for link in sorted(list(set(unsorted))):
#     print(link)

# Решение из комментов

# import requests
# import re

# page = requests.get(input())

# url_pattern = re.compile(r'<a.*?href=["|\'](.*?:\/\/)?(\w.*?)([/|:].*)?["|\'].*')
# links = sorted(set([link[1] for link in url_pattern.findall(page.text)]))
# print(*links, sep='\n')

###

# import re
# import requests

# resp = requests.get(input()).text
# sites = set()
# for site in re.findall(r'<a.*?href=".*?:\/\/((?:\w|-)+(?:\.(?:\w|-)+)+)', resp):
#     sites.add(site)

# for site in sorted(sites):
#     print(site)
