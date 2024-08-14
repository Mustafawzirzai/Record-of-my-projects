class Employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department

manager=Manager("ali",5555,"it")
print(manager.name)





