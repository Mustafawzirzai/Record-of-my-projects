class Animal():
    def speak(self):
        return "animal sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meeeow"

dog_1=Dog()
cat_1=Cat()
print(dog_1.speak())
print(cat_1.speak())
