from tkinter import *
class To_do():
    def __init__(self):
        self.tasks = []
        self.window = Tk()
        self.window.geometry("350x350")
        self.window.config(bg="#3C467E")

        self.tasks_label=Label(self.window,text="your tasks",font=("Arial",25),bg="#3C467E")
        self.tasks_label.pack()
        self.label = Label(self.window, text=self.tasks, bg="#DDDFCF", width=20,height=12)
        self.label.pack()

        self.add_task_label=Label(self.window,text="add your task here",bg="#3C467E")
        self.add_task_label.pack()

        self.entry_box=Entry(self.window,width=25)
        self.entry_box.pack()

        self.add_button = Button(self.window, text="Add task", command=self.add,bg="#B2834E")
        self.add_button.pack()

        self.remove_button = Button(self.window, text="remove",command=self.remove,bg="#B2834E")
        self.remove_button.pack()
    def add(self):
        task=self.entry_box.get()
        self.tasks.append(task)
        self.label_update()


    def remove(self):
        task=self.entry_box.get()
        self.tasks.remove(task)
        self.label_update()

    def label_update(self):
        self.label.config(text=str(self.tasks))
t1 = To_do()
t1.window.mainloop()
t1.add()

