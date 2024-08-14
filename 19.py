class Company():
    def __init__(self,name):
        self.name=name
        self.employee=[]

    def add_new_employee(self,employee):
        self.employee.append(employee)

    def remove_a_employee(self,employee):
        if employee in self.employee:
            self.employee.remove(employee)
        else:
            print("this employee is not in your company")

s1=Company("Wahidi")
s1.add_new_employee("ali")
s1.remove_a_employee("ali")
print(s1.employee)