class Flight():
    def __init__(self, flight_num,destination,):
        self.flight=flight_num
        self.des=destination
        self.passengers = []

    def add_passengers(self, passenger):
        self.passengers.append(passenger)

    def remove(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
        else:
            print("there is no such dish in our menu.")

    def display(self):
        print(self.passengers)


f1=Flight(101,"Dubai")
pas1=f1.add_passengers("ali")

f1.display()