from tkinter import *
import random

class Whether_app():
    def __init__(self):

        self.degrees=random.randint(5,30)
        self.tomorrow=random.randint(5,35)

        self.window = Tk()
        self.window.geometry("300x300")
        self.window.config(bg="yellow")

        self.whether_label=Label(self.window,text="Whether:",bg="yellow",font=("arial",25))
        self.whether_label.pack()
        self.degree_label=Label(self.window,text=f"{self.degrees}'",width=2,height=1,bg="yellow",font=("arial",50))
        self.degree_label.pack()

        self.tomorrow_label=Label(self.window,text="tomorrow's\n prediction:",bg="yellow",font=("arial",25))
        self.tomorrow_label.pack()

        self.tomorrow_whether=Label(self.window,text=f"{self.tomorrow}'",width=2,height=1,bg="yellow",font=("arial",50))
        self.tomorrow_whether.pack()



w1=Whether_app()
w1.window.mainloop()
