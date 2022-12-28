''' Метод k-ближайших соседей '''

# Метрический алгоритм для автоматической классификации объектов или регрессии.

# В случае использования метода для классификации объект присваивается тому классу,
# который является наиболее распространённым среди k соседей данного элемента, 
# классы которых уже известны. В случае использования метода для регрессии, 
# объекту присваивается среднее значение по k ближайшим к нему объектам, значения 
# которых уже известны.

# Как классифицироватъ этот фрукт? Один из способов - рассмотреть соседей
# этой точки. Возьмем ее трех ближайших соседей.
# Среди соседей больше апельсинов, чем грейпфрутов . Следовательно, этот
# фрукт, скорее всего, является апельсином. Поздравляем: вы только что
# применили алгоритм k ближайших соседей для классификации! В целом
# алгоритм работает по довольно простому принципу.

# Измеряем расстояние до ближайших объектов
# Используем формулу расстояния для вычисления степени родства двух объектов

# Классификация - распределение по категориям
# Регрессия - прогнозирование ответа


