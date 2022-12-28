''' API '''

# import requests
# city = input('City?')
# api_url = 'https://api.openweathermap.org/data/2.5/weather'

# params = {
#     'q': city, #'Saint Petersburg',
#     'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7',
#     'units': 'metric'
# }

# res = requests.get(api_url, params = params)
# # print(res.status_code) # 200
# # print(res.headers['Content-Type']) # application/json; charset=utf-8
# # print(res.json())
# data = res.json()
# main_temp = data['main']['temp']

# print(f'Current temperature in {city} is {main_temp}°С')


''' Задания '''

# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли 
# интересный математический факт об этом числе.

# Для каждого числа выведите Interesting, если для числа существует интересный 
# факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют 
# числа во входном файле.

# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true

# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true

# Пример входного файла:
# 31
# 999
# 1024
# 502

# Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring

# while True:
#     inp = input()
#     if inp == '':
#         break

# requests.get(f'http://******.com/{i}/****')
# f'http://numbersapi.com/{i}/math?json'

# import requests
# import json

# with open('dataset_24476_3 (3).txt') as f:
#     numbers = f.read().splitlines()

# for number in numbers:
#     url = f'http://numbersapi.com/{number}/math?json=true'
#     res = requests.get(url)
#     data = res.json()
#     # print(data['found'])
#     print('Interesting' if data['found'] else 'Boring')


### Другие решения

# with open('dataset_24476_3.txt') as file:
#     for num in file:
#         response = re.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()
        
#         print('Interesting') if response['found'] else print('Boring')

# ###

# import requests
# import json

# def is_interesting(x):
#     url = "http://numbersapi.com/"; + str(x) + "/math?json=true"
#     resp = requests.get(url).text
#     js = json.loads(resp)
#     return js["found"]

# with open("input.txt") as fi:
#     for line in fi:
#         print("Interesting" if is_interesting(line.rstrip()) else "Boring")

####
# В этой задаче вам необходимо воспользоваться API сайта artsy.net

# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год 
# рождения, выведите их имена в лексикографическом порядке.

# Работа с API Artsy

# Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения 
# доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ 
# (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

# Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API 
# https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать 
# приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

# После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, 
# как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.

import requests
import json
import artsy_token

client_id = artsy_token.client_id
client_secret = artsy_token.client_secret

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

artists = []
with open('dataset_24476_4 (2).txt') as f:
    artists = f.read().splitlines()
artist_normal_names = {}

# Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, как 
# осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
for artist in artists:
    url = f'https://api.artsy.net/api/artists/{artist}'
    r = requests.get(url, headers=headers)
    # разбираем ответ сервера
    j = json.loads(r.text)
    artist_normal_names[j['sortable_name']] = j['birthday']

# print(artist_normal_names)
# artist_normal_names = 

for artist in sorted(artist_normal_names.items(), key=lambda x: (x[1], x[0])):
    print(artist[0])


# Примечание:
# В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

# Пример входных данных:
# 4d8b92b34eb68a1b2c0003f4
# 537def3c139b21353f0006a6
# 4e2ed576477cc70001006f99

# Пример выходных данных:
# Abbott Mary
# Warhol Andy
# Abbas Hamra

# Примечание для пользователей Windows
# При открытии файла для записи на Windows по умолчанию используется кодировка CP1251, в то время как для записи имен на 
# сайте используется кодировка UTF-8, что может привести к ошибке при попытке записать в файл имя с необычными символами. 
# Вы можете использовать print, или аргумент encoding функции open.

