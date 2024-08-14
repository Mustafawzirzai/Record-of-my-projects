from tkinter import *
class Counter_app():
    def __init__(self):
        self.window=Tk()
        self.window.title("counter app")
        self.window.geometry("200x200")

        self.counter=0

        self.label=Label(self.window,text=str(self.counter),font=("Helvetica", 48),bg="blue",width=3)
        self.label.pack()

        self.Up_button=Button(self.window,text="Up",command=self.increase_num,font=("Helvetica", 15))
        self.Up_button.pack()

        self.Down_button = Button(self.window, text="Down", command=self.decrease_num, font=("Helvetica", 15))
        self.Down_button.pack()

    def increase_num(self):
        self.counter=self.counter+1
        self.update_label()
    def decrease_num(self):
        if self.counter>=1:
            self.counter-=1
            self.update_label()


    def update_label(self):
        self.label.config(text=str(self.counter))


bb=Counter_app()
print(bb.window.mainloop())
