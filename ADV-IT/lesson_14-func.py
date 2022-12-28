

def napechatat_privetstvie(name):
    '''Print privetstvie'''
    print('Congratulations, ' + name + ', wish you all the best')
    print('Hello Hello Hello')


def summa(x, y):
    print(x + y)


def summa_count(x, y):
    return x + y

'''main program'''

print('------------')
napechatat_privetstvie('Vasya')
napechatat_privetstvie('Dima')

summa(10, 20)

x = summa_count(33, 22)
print(x)

def factorial(n):
    '''Calculate factorial of n'''
    otvet = 1
    for i in range(1, n + 1):
        otvet *= i
    return otvet

print(factorial(1))
print(factorial(5))

for i in range(1, 10 + 1):
    print(str(i) + '!\t = ' + str(factorial(i)))