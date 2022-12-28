''' Алгори́тм Де́йкстры '''

# (англ. Dijkstra’s algorithm) — алгоритм на графах, изобретённый нидерландским учёным Эдсгером Дейкстрой в 1959 году. 
# Находит кратчайшие пути от одной из вершин графа до всех остальных. Алгоритм работает только для графов без рёбер отрицательного веса. 

# Работает только с направленными ациклическими графами Directed Acyclic Graph
# Не работает с графами с отрицательными весами. Для них есть алгоритм Беллмана-Форда

# Каждому ребру присваивается вес. Графы с весами - взвешенные графы

# Для реализации алгоритма нужны 3 хеш-таблицы

#          ___A___
#         /   |   \1 
#        /6   |    \
#  start      |3    end
#        \2   |    /
#         \___B___/5 
# 

graph = {}

graph['start'] = {} # создаё м узел
graph['start']['a'] = 6 # задаём стоимость перехода до следующего узла
graph['start']['b'] = 2 

print(graph['start'].keys()) # вывод всех соседей первого узла - dict_keys(['a', 'b'])

print(graph['start']['a']) # выводл весов рёбер - 2

# зададим другие узлы и их соседей
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {} # у конечного узла нет соседей

infinity = float('inf') # бесконечность в пайтоне!
costs = {} # хеш-таблица со стоимостью перехода от начального узла
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {} # таблица для родителей
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

processed = [] # массив для уже обработанных узлов

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs: # перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed: # если это узел с наименьшей стоимостью и ещё не был обработан
            lowest_cost = cost # он назначается новым узлом
            lowest_cost_node = node # с наименьшей стоимостью
    return lowest_cost_node


node = find_lowest_cost_node(costs) # ищем узел с наименьшей стоимостью среди необработанных
while node is not None: # если завершена обработка всех узлов - обработка завершена
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # перебрать всех соседей текущего узла
        new_cost = cost + neighbors[n] # если к соседу быстрее добраться через текущий узел
        if costs[n] > new_cost: # сравниваем стоимость
            costs[n] = new_cost # обновляем стоимость для этого узла
            parents[n] = node # текущий узел становится новым родителем для соседа
    processed.append(node) # узел помечается как обработанный
    node = find_lowest_cost_node(costs) # ищем следующий узел для обработки и повторяем цикл

