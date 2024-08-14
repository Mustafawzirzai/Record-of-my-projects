class Rasturant():
    def __init__(self,name):
        self.name=name
        self.menu=[]

    def add_to_menu(self,new_dish,):
        self.menu.append(new_dish)



    def remove(self,item_name):
        if item_name in self.menu:
            self.menu.remove(item_name)
        else:
            print("there is no such dish in our menu.")

    def display(self):
        print(f"this is our menu {self.menu}}")

ras=Rasturant("Wahidi")
dish1=ras.add_to_menu("Kabab")
ras.display()