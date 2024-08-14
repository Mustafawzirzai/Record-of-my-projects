class Account():
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self):
        print("deposit money")

    def withdraw(self):
        print("withdraw your money")

a1=Account(5000)

