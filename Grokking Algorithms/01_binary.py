# Бинарный поиск - сравниваем середину отсортированного списка с требуемым значением, 
# если не попали - сужаем поиск ещё в два раза - делим пополам следующий диапазон и т.д.

# low = 0
# high = len(list) - 1

# mid = (low + high) / 2
# guess = list[mid]
# if guess < item:
#     low = mid-1

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) / 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))



# def recursive_binary_search(list, item):
#     low = 0
#     high = len(list) - 1

#     mid = (low + high) / 2
#     guess = list[mid]
#     if guess == item:
#         return mid
#     if guess > item:
#         recursive_binary_search(list,)


''' Время выполнения алгоритма'''
# O(n) - nростой перебор - линейное время, количество попыток равняется длинне списка.
# O(log n) - Бинарный поиск - количество попыток степень двойки, логарифмическое время log(n)
# O(n * log n) - Эффективные алгоритмы сортировки, сортировка выбором
# O(n^2) - медленные алгоритмы сортировки, сортировка выбором
# O(n!) - очень медленный алгоритм сортировки, задача о комивояжере



