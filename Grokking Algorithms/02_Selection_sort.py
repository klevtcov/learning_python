# Selection sort – сортировка выбором

# Массивы - чтение O(1), запись O(n)
# Списки - чтение O(n), запись O(1)

# Перебираем список, находим наименьший/наибольший элемент, добавляем его в новый список, удаляя из изначального
# Повторяем

def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr) # ищет индекс наименьшего элемента
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))


