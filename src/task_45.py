class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

book1 = Book("StardustMemories")
book2 = Book("GoldenWind")
print(Book.total_books)