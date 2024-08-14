class Hotel():
    def __init__(self,name):
        self.name=name
        self.available_rooms=[101,102,103]
        self.is_ocu="no"


    def check(self,room_num):
        if self.is_ocu == "no" and room_num in self.available_rooms:
            print("this room is available")
        else:
            print("sorry this room is already taken!")

    def book(self,room_num):
        if room_num in self.available_rooms:
            self.available_rooms.remove(room_num)
            self.is_ocu =="yes"
            print("enjoy!!")
        else:
            print("sorry, this room is not available!")



hotel=Hotel("Wahidi luxury hotel")
hotel.book(103)
hotel.book(100)



