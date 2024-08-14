import math
class Circle:
    def area(self,radius):
        area = 2*math.pi*radius
        print(area)

first_area=Circle()
radius_input=int(input("enter the radius"))
first_area.area(radius_input)


