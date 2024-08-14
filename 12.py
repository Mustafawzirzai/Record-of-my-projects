class Book():
    def __init__(self,title,author,pages):
        self.__title=title
        self.__author=author
        self.__pages=pages

    def book_info(self):
        print(f"the author of {self.__title} book is {self.__author} and has {self.__pages} pages")

b1=Book("'succes story'","Abdullah Wahidi",200)
b1.book_info()
