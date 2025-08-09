class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

book1 = Book("sugoi hon")
book2 = Book("totemo ii hon")

print(Book.total_books)