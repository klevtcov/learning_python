class A:
    def a(self):
        print('A')

class B:
    def a(self):
        print('B')

class C(B):
    def a(self):
        print('C')

class D(C, A):
    def a(self):
        # super().a()
        super(C, self).a()
        # super(D, self).a() это по умолчанию, откуда начинает искать
        print(self.__class__.__mro__) 
        '''отображает все наследования и очередность прохода'''

D().a()
print(D.__mro__)

class Verification:

    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
        self.__lenPassword()

    def __lenPassword(self):
        if len(self.password) < 8:
            raise ValueError ('слабый пароль')

    def save(self):
        with open('users', 'a') as r:
            r.write(f'{self.login, self.password}'+'\n')


