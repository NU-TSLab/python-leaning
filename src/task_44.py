class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

book1 = Book("a")
print(book1.title)
book2 = Book("s")
book3 = Book("d")
print(Book.total_books)