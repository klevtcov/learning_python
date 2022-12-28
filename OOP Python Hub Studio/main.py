# from tkinter import Tk

# объект - единица информации в памяти
# экземпляр - конкретный объект какого-то класса
# класс - инструкция по созданию объектов определенного типа
# метод - функция в классе для воздействия на объект
# поля или свойства - переменные в классе
# артибуты - все имена в классе: переменных и методов
# инкапсуляция - защита данных, невозможность их менять напрямую. одно подчеркивание - позволяет обратиться напрямую, двойное - даже с явным обращением по имени не даст изменить данные
# del - исполняется всегда, когда удаляется объект, т.е. при выходе из программы, когда будет очищена память - метод будет отработан

# root = Tk()
# root.mainloop()

class Purse:
    
    def __init__(self, currency, name='Unknown') -> None:
        if currency not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.currency = currency
        self.name = name
    
    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Не достаточно средств')
            raise ValueError ('Не достаточно средств')
        self.__money = self.__money - howmany
        return howmany

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Кошелек удалён')


x = Purse('USD')
y = Purse('USD', 'Bill')
y.top_up_balance(10)
y.info()
x.top_up_balance(y.top_down_balance(7))
# x.__money = -200 не сработает, т.к. инкапсуляция
x.info()
y.info()
# del x







# x.money = 100
# print(x.info())
# print(y.info())

#     def show(self, name='Unknown'):
#         print('Hello ' + name)

# x = Purse()
# y = Purse()
# # print(type(x))
# x.show()
# y.show('Alice')