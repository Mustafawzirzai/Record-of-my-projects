class Rectangle():
    def area(self,length,width):
        area=width*length
        print(f"the area is {area}")

rec=Rectangle()
length_input=int(input("enter the length:"))
width_input=int(input("enter the width:"))
rec.area(length_input,width_input)

