# import colorama
#
# print(colorama.Back.BLACK,colorama.Fore.RED)
# print('Привет')

# инкапсуляция

# 3 публичный доступ,защищенный,приватный


class BankAccount:
    def __init__(self, name, balance,key):
        self.name = name
        self.__balance = balance
        self._key = key

class Bank:
    def __init__(self, name, balance, key):
        self.name = name
        self.__balance = balance
        self._key = key

    def say(self):
        self._saykey()
    def _saykey(self):
        print(self._key,self.__balance)

    def set_balance(self,new_balance):
        if new_balance>= 0:
            self.__balance = new_balance
            print(f"Balance has changed :{new_balance}")
        else:
            print("Balance can not be changed ")

    def get_balance(self):
        return self.__balance
b=Bank('John', 100, 2525)
b.name=11
b.key=11111111111
b.Lname='python'
b.say()
b.balance = 99
b.set_balance(101)