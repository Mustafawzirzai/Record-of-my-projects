class Bird():
    def fly(self):
        pass

class penguin(Bird):
    def fly(self):
        print("these birds cannot fly!")

class Eagle(Bird):
    def fly(self):
        print("it flies ")

pen=penguin()
pen.fly()