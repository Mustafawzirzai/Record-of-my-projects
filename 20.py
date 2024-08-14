class Zoo():
    def __init__(self,name):
        self.name=name
        self.animal=[]

    def add_animal(self,animal):
        self.animal.append(animal)

    def remove_animal(self,animal):
        if animal in self.animal:
            self.animal.remove(animal)
        else:
            print("this animal is not in your zoo")



a1=Zoo("Kabul national zoo")
a1.add_animal("lion")
a1.remove_animal("lion")
print(a1.animal)