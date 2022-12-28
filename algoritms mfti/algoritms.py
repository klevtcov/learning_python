flag = False
n = int(input())
for i in range(n):
    x = int(input())
    flag = (x%10 == 0) or flag #перебираем числа до первого истинного


flag = True
n = int(input())
for i in range(n):
    x = int(input())
    flag = flag and (x%10 == 0) # до первого ложного высказывания

# Вложенные и последовательные if

# Выводим ДА если делится на 2 или на 3

x = int(input())
if x%2 == 0:
    print('yes')
if x%3 == 0:
    print('yes')

# а если надо учесть оба варианта
if x%2 == 0 or x%3 == 0:
    print('yes')


# Каскадная условная конструкция
# Отрезки A B C D расположены на прямой

x = int(input())
if x < 0:
    print('A')
elif x < 5:
    print('B')
elif x < 10:
    print('C')
else:
    print('D')

# Точки расположены в четвертях, но не лежат на осях

if y > 0:
    if x > 0:
        print('I четверть')
    else:
        print('IV четверть')
else:
    if x > 0:
        print('II четверть')
    else:
        print('III четверть')


# Системы счисления

x = 0b1111 '''  b - binary '''
y = 0o00732 ''' o - octo, восьмиричная '''
z = 0x12F3A0 ''' x 16-тиричная '''
t = int('Z7A', 36) ''' произвольная система, максимум до 36 '''

print(x)- вывод в 10-ной, по умолчанию

x = 127
print(bin(x)) - в двоичном
oct(x)
hex(x)

#  перевод в произвольную систему
base = 7
x = int(input())
while x > 0:
    digit = x % base
    print(digit, end='')
    x //= base


#  Однопроходные алгоритмы
поиск числа в последовательности

f = False
f = f or (x == y)

