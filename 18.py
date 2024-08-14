class Team():
    def __init__(self,name):
        self.name=name
        self.members=[]

    def add_new_member(self,nem_member):
        self.members.append(nem_member)

    def remove_a_member(self,member):
        if member in self.members:
            self.members.remove(member)
        else:
            print("this member is not in your team")

s1=Team("Habibia")
s1.add_new_member("ali")

#s1.remove_a_member("ali")
print(f"the team members are {s1.members}")