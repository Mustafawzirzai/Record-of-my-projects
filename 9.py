class Vehicle():
    def Drive(self):
        print("differnt")

class Bike(Vehicle):
    def Drive(self):
        print("drive with handels")

class Truck(Vehicle):
    def Drive(self):
        print("drive with steering wheel")


bike=Bike()
truck=Truck()
bike.Drive()