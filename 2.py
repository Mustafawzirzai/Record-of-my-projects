class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"hello {self.name}")
person_1=person(name="ali",age="25")
print(person_1.name)
print(person_1.age)
person_1.greet()
