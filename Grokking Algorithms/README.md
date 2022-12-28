# Грокаем алгоритмы (Адитья Бхаргава)

## 01 Бинарный поиск
Двоичный (бинарный) поиск (также известен как метод деления пополам или дихотомия) — классический алгоритм поиска элемента в отсортированном массиве (векторе), использующий дробление массива на половины.
* Определение значения элемента в середине структуры данных. Полученное значение сравнивается с ключом.
* Если ключ меньше значения середины, то поиск осуществляется в первой половине элементов, иначе — во второй.
* Поиск сводится к тому, что вновь определяется значение серединного элемента в выбранной половине и сравнивается с ключом.
* Процесс продолжается до тех пор, пока не будет найден элемент со значением ключа или не станет пустым интервал для поиска.


## 02 Сортировка выбором
* находим номер минимального значения в текущем списке
* производим обмен этого значения со значением первой неотсортированной позиции (обмен не нужен, если минимальный элемент уже находится на данной позиции)
* теперь сортируем хвост списка, исключив из рассмотрения уже отсортированные элементы

## 03 Рекурсия
Вызов функции (процедуры) из неё же самой, непосредственно (простая рекурсия) или через другие функции (сложная или косвенная рекурсия).

## 04 Быстрая сортировка
QuickSort является существенно улучшенным вариантом алгоритма сортировки с помощью прямого обмена (его варианты известны как «Пузырьковая сортировка» и «Шейкерная сортировка»), известного в том числе своей низкой эффективностью. Принципиальное отличие состоит в том, что в первую очередь производятся перестановки на наибольшем возможном расстоянии и после каждого прохода элементы делятся на две независимые группы (таким образом улучшение самого неэффективного прямого метода сортировки дало в результате один из наиболее эффективных улучшенных методов).
* Выбрать элемент из массива. Назовём его опорным.
* Разбиение: перераспределение элементов в массиве таким образом, что элементы, меньшие опорного, помещаются перед ним, а большие или равные - после.
* Рекурсивно применить первые два шага к двум подмассивам слева и справа от опорного элемента. Рекурсия не применяется к массиву, в котором только один элемент или отсутствуют элементы.

## 05 Хеш таблицы
Структура данных, реализующая интерфейс ассоциативного массива, а именно, она позволяет хранить пары (ключ, значение) и выполнять три операции: операцию добавления новой пары, операцию поиска и операцию удаления пары по ключу.
* Хэш функция получает строку и возвращает число, т.е. отображает строки на числа
* Хэш функция неизменно связывает название с одним индексом
* Время обращения к данным O(1)

## 06 Поиск в ширину. Графы
Один из методов обхода графа. Пусть задан граф G=(V,E) и выделена исходная вершина s. Алгоритм поиска в ширину систематически обходит все ребра G для «открытия» всех вершин, достижимых из s, вычисляя при этом расстояние (минимальное количество рёбер) от s до каждой достижимой из s вершины.
* Поместить узел, с которого начинается поиск, в изначально пустую очередь.
* Извлечь из начала очереди узел u и пометить его как развёрнутый.
* Если узел u является целевым узлом, то завершить поиск с результатом «успех».
* В противном случае, в конец очереди добавляются все преемники узла u, которые ещё не развёрнуты и не находятся в очереди.
* Если очередь пуста, то все узлы связного графа были просмотрены, следовательно, целевой узел недостижим из начального; завершить поиск с результатом «неудача».
* Вернуться к п. 2.

## 07 Алгори́тм Де́йкстры
Находит пути от одной из вершин графа до всех остальных с наименьшей стоимостью. Алгоритм работает только для графов без рёбер отрицательного веса. 
* Каждой вершине из V сопоставим метку — минимальное известное расстояние от этой вершины до a.
* Алгоритм работает пошагово — на каждом шаге он «посещает» одну вершину и пытается уменьшать метки.
* Работа алгоритма завершается, когда все вершины посещены.

## 08 Жадные алгоритмы
Greedy algorithm — алгоритм, заключающийся в принятии локально оптимальных решений на каждом этапе, допуская, что конечное решение также окажется оптимальным. 
* Задачи о пересекающихся множествах
* Задача коммивояжера

## 09 Динамическое программирование
Способ решения сложных задач путём разбиения их на более простые подзадачи. Он применим к задачам с оптимальной подструктурой, выглядящим как набор перекрывающихся подзадач, сложность которых чуть меньше исходной. В этом случае время вычислений, по сравнению с «наивными» методами, можно значительно сократить.
* Разбиение задачи на подзадачи меньшего размера.
* Нахождение оптимального решения подзадач рекурсивно, проделывая такой же трехшаговый алгоритм.
* Использование полученного решения подзадач для конструирования решения исходной задачи.

## 10 Метод k-ближайших соседей
В случае использования метода для классификации объект присваивается тому классу, который является наиболее распространённым среди k соседей данного элемента, 
классы которых уже известны. В случае использования метода для регрессии, объекту присваивается среднее значение по k ближайшим к нему объектам, значения 
которых уже известны.
* Алгоритм может быть применим к выборкам с большим количеством атрибутов (многомерным). Для этого перед применением нужно определить функцию расстояния.