class Bank_account():
    def __init__(self,account_number,balance):
        self.__acc_num=account_number
        self.__bal=balance

    def deposit(self):
        print("deposit money")

    def withdraw(self):
        print("withdraw your money")
    def check_balance(self):
        print(f"your balance is {self.__bal}")

b1=Bank_account(150002,"50000$")
b1.check_balance()