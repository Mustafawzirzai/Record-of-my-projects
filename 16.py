class Library():
    def __init__(self,name):
        self.name=name
        self.books=[]

    def add_books(self,book):
        self.books.append(book)

    def remove_books(self,book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("this book in not in your library")

lib=Library("my lib")
lib.add_books("math")
lib.remove_books("math")
print(lib.books)






