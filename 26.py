class Ticket():
    def __init__(self,movie,seat_number,price):
        self.film=movie
        self.seat=seat_number
        self.price=price

    def movie(self):
        return f"{self.film}"

    def seat(self):
        return f"your seat number is {self.seat_}"
    def price(self):
        return f"this movie will cost u {self.price}"

t1=Ticket("Tiger",123,55)
print(t1.price)


