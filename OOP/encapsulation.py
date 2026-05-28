# Encapsulation

class Bank:
    def __init__(self):
        self.__balance = 1000  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        print("Balance:", self.__balance)

b = Bank()
b.deposit(500)
b.get_balance()