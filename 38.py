from tkinter import *

class Calculator_app():
    def __init__(self):
        self.window=Tk()
        self.window.config(bg="black")
        self.entry_box=Entry(self.window,width=30,font=("Arial",15),borderwidth=2,relief=SOLID,bg="pink")
        self.entry_box.grid(columnspan=5)
        self.clear_button = Button(self.window, width=8, height=2, text="C", bg="#68675C", command=self.clear,activebackground="#68675C")
        self.clear_button.grid(row=6,column=1,columnspan=2)

        self.row_val = 1
        self.column_val = 0
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        for button in self.buttons:
            self.action =lambda x=button:self.button_click(x) if x != "=" else self.calculate(x)
            self.buttoon=Button(self.window,text=button,bg="#68675C",width=8,height=2,command=self.action,font=("aril",12),activebackground="#68675C")
            self.buttoon.grid(row=self.row_val,column=self.column_val)

            self.column_val += 1
            if self.column_val > 3:
                self.column_val = 0
                self.row_val += 1
    def button_click(self,value):
        self.entry_box.insert(END,value)

    def calculate(self,value):
        try:
            result=eval(self.entry_box.get())
            self.entry_box.delete(0,END)
            self.entry_box.insert(END,result)

        except:
            self.entry_box.delete(0,END)
            self.entry_box.insert(END,"error")

    def clear(self):
        self.entry_box.delete(0,END)



c1=Calculator_app()
c1.window.mainloop()

