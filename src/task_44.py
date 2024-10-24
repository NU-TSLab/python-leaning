class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

b1 = Book("数学")
b2 = Book("英語")
print(Book.total_books) 