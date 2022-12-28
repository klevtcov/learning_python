
# a = input().split(' ')
# print(int(a[0]) + int(a[1]))


# a,b = input().split(' ')


# file = open('input.txt', 'r')
# with file:
#     a = file.read().split(' ')
# file.close()

# file_out = open('output.txt', 'w')
# file_out.write(str(int(a[0]) + int(a[1])))
# file_out.close()

# a = set(input())
# b = input()
# jewels = 0

# for i in a:
#     for j in b:
#         if i == j:
#             jewels += 1

# print(jewels)

# first_word = input()
# second_word = input()

# correct 
# absent
# present

# first_word = list(input())
# second_word = list(input())

# result = []
# word_range = len(first_word)

# for i in range(word_range):
#     result += '1'

# for i in range(word_range):
#     if second_word[i] != '0':
#         if second_word[i] == first_word[i]:
#             result[i] = 'correct'
#             second_word[i] = '0' 
#             first_word[i] = '0'

# for i in range(word_range):
#     if second_word[i] != '0':            
#         if second_word[i] in first_word:
#             result[i] = 'present'
#             el = first_word.index(second_word[i])
#             first_word[el] = '0'
#             second_word[i] = '0'
#         else:
#             result[i] = 'absent'
#             second_word[i] = '0'            

# for n in result:
#     print(n)




# 2
# ceo,1
# co_founder,1
# 3
# arcady_volozh,ceo,6,100
# elon_musk,ceo,5,0
# ilya_segalovich,co_founder,6,10

# from tempfile import tempdir

import sqlite3

base = sqlite3.connect("patrypart.db", check_same_thread=False)
sql = base.cursor()

def check_db_exists():
    """Проверяет наличие основной таблицы, если её нет - создаёт"""
    sql.execute("""CREATE TABLE IF NOT EXISTS vacancies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vacancy_name TEXT,
            number_of_vacancies INT)""")
    base.commit()

    sql.execute("""CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_name TEXT,
            vacancy_name TEXT,
            tasks  INT,
            penalties INT)""")
    base.commit()

check_db_exists()

def clear_base():
    sql.execute(f'delete from vacancies')
    sql.execute(f'delete from candidates')
    base.commit()

clear_base()

vacancies_numbers = int(input())
for n in range(vacancies_numbers):
    input_data = input().split(',')
    sql.execute(f'INSERT INTO vacancies (vacancy_name, number_of_vacancies) VALUES(?, ?)', (input_data[0], input_data[1]))
    base.commit()  

results_number = int(input())
for n in range(results_number):
    input_data = input().split(',')
    sql.execute(f'INSERT INTO candidates (candidate_name, vacancy_name, tasks, penalties) VALUES(?, ?, ?, ?)', (input_data[0], input_data[1], input_data[2], input_data[3]))
    base.commit()



# print(vacansions)
# print(results)





# list.index(x)

# print(results)

# for i in range(len(vacancies_numbers)):
#     for j in range(vacansions[i]):
        




# print(vacansions)
# print(candidats_results)
