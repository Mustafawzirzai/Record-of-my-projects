class Laptop():
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.__model=model
        self.__price=price

    def discount(self):
        print(f"this {self.__brand} whose model is {self.__model} will cost you {self.__price} and after discount "
              f"it will cost u {(self.__price)*0.80}")

l1=Laptop("acer","aspire 5",800)
l1.discount()