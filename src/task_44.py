# task_44.py
class Book:
    total_books = 0

    def __init__(self,title):
        self.title = title
        Book.total_books += 1

book1 = Book("国語")
book2 = Book("算数")
print(Book.total_books)
