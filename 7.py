width=int(input("enter the width"))
hieght=int(input("enter the hieght"))

class Shape():
    def area(self):
        print(width*hieght)

class Square(Shape):
    pass
class Rectangle(Shape):
    pass
square=Square()
square.area()