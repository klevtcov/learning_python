from logging import root
from class3 import Verification
from tkinter import Tk, Button

class V2(Verification):
    
    def __init__(self, login, password, age) -> None:
        # Verification.__init__(self, login, password) '''простое наследование'''
        super().__init__(login, password)
        self.__save()
        self.age = age


    def __save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}'+'\n' == i:
                    raise ValueError ('Такой есть')
        # Verification.save(self)        
        super().save()

    def show(self):
        return self.login, self.password


x = V2('Kenny4', '123456789', 33)
print(x.show())

# root = Tk()
# root.mainloop()

# class My_app(Tk):

#     def __init__(self) -> None:
#         Tk.__init__(self)
#         self.geometry('400x400')
#         self.setUI()

#     def setUI(self):
#         Button(self, text='OK').pack()

        
# root = My_app()
# root.mainloop()