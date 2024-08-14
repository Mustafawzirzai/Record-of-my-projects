from tkinter import *

class Login():
    def __init__(self):
        self.accounts=[]



        self.window=Tk()
        self.email_label=Label(self.window,text="Enter your email:",font=("arial",10,"bold"))
        self.email_label.pack()

        self.email_entry=Entry(self.window,width=25)
        self.email_entry.pack()

        self.password_label = Label(self.window, text="Enter the password:", font=("arial", 10, "bold"))
        self.password_label.pack()

        self.password_entry=Entry(self.window, width=25)
        self.password_entry.pack()
        self.login_button = Button(self.window, text="login", font=("arial", 11, 'bold'), bg="red", command=self.login)
        self.login_button.pack()

    def login(self):
        if (self.email_entry.get() == "abd@gmail.com" and self.password_entry.get()=="123456"):
            self.new_window=Tk()
            self.s_label=Label(self.new_window,text="user_name:Abdullah Wahidi\ncourse_id:Wahidi58\nprogram:software development"
                      ,font=("arial",10,'bold'),
                      bg="pink",height=5,
                      width=30)

            self.s_label.pack()
        else:
            self.another_win = Tk()

            self.u_label = Label(self.another_win, text="email or password in incorrect", font=("arial", 10, 'bold'),
                            bg="pink", height=2,
                            width=35)
            self.u_label.pack()
            self.window.destroy()



l1=Login()
l1.window.mainloop()
