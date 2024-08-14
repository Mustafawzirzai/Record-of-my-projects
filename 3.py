class car:
    def __init__(self,made,model,year):
        self.made=made
        self.mod=model
        self.year=year

    def car_info(self):
        print(f"this car which is a {self.year} {self.mod} was made in {self.made}")

car_1= car(made="China",model="Toyota",year="2005")
car_1.car_info()
