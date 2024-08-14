class Student():
    def __init__(self,name,grade,age):
        self.__name=name
        self.__grade=grade
        self.__age=age

    def name(self):
        print(f"my name is {self.__name}.")
    def grade(self):
        print(f"i am in {self.__grade} class.")
    def age(self):
        print(f"i am {self.__age} years of age.")

    def student_details(self):
        print(f"my name is {self.__name}, i am in {self.__grade} class, i am {self.__age} years of age. ")

s1=Student("Abdullah","12th",20)
s1.student_details()
