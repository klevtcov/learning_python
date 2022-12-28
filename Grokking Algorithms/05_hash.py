''' Хэш таблицы'''

# Хэш функция получает строку и возвращает число, т.е. отображает строки на числа, 
# Хэш функция неизменно связывает название с одним индексом
# Время обращения к данным O(1)
# В python хэш-таблицы называются словарями

# book = dict()

# book['apple'] = 0.67
# book['milk'] = 1.49
# book['avocado'] = 1.49
# print(book) # {'apple': 0.67, 'milk': 1.49, 'avocado': 1.49}
# print(book['avocado']) # 1.49


phone_book = {}
phone_book['jenny'] = 8675309
phone_book['emergency'] = 911

print(phone_book['jenny']) # 8675309
print(phone_book.get('jennyfer')) # None


