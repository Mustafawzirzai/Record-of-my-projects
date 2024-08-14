class School():
    def __init__(self,name):
        self.name=name
        self.students=[]

    def add_student(self,students):
        self.students.append(students)

    def remove_student(self,students):
        if students in self.students:
            self.students.remove(students)
        else:
            print("this student is not in the scholl")

s1=School("Habibia")
s1.add_student("ali")
s1.remove_student("ali")
print(s1.students)