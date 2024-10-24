class Book:

    total_books=0
    def __init__(self,title):
        self.title=title
        Book.total_books+=1

book1=Book("あいうえ")
print(Book.total_books)
book2=Book("かきくけ")
print(Book.total_books)
book3=Book("さしすせ")
print(Book.total_books)